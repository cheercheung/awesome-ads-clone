#!/usr/bin/env python3 -I
"""Assemble passed clips into the final ad, mix sound, and build the comparison video.

usage: python3 -I assemble.py SPEC.json

SPEC.json (paths are relative to the spec file):
{
  "size": [540, 960], "fps": 24,
  "clips": [                                  # in order; hard cuts between them
    {"file": "clips/A_v5.mp4", "start": 0.0, "dur": 8.0},
    {"file": "clips/D_v2.mp4", "start": 1.0, "dur": 0.5,
     "crop": "iw*0.8:ih*0.8:(iw-iw*0.8)/2:0"}  # optional ffmpeg crop expression
  ],
  "out": "Product_rebuild_final.mp4",
  "audio": {                                  # optional; omitted = keep clip audio as is
    "clip_db": -12,                           # generated room tone; null mutes it
    "voiceover": [{"file": "vo/line1.wav", "at": 0.0}],
    "vo_db": 0,
    "music": "music.mp3", "music_db": -18
  },
  "compare": {                                # optional
    "reference": "../reference.mp4", "creator": "creator.jpg", "product": "product.png",
    "out": "Compare_original_vs_rebuild.mp4", "audio": "reference",   # or "rebuild"
    "labels": {"reference": "lbl_original.png", "rebuild": "lbl_rebuild.png",
               "creator": "lbl_creator.png", "product": "lbl_product.png"}   # optional PNGs
  }
}
Intermediate files go to a temporary folder that is removed afterwards.
"""
import json, os, subprocess, sys, tempfile

if len(sys.argv) != 2:
    sys.exit(__doc__)
spec_path = os.path.abspath(sys.argv[1])
base = os.path.dirname(spec_path)
spec = json.load(open(spec_path, encoding="utf-8"))
W, H = spec.get("size", [540, 960])
FPS = spec.get("fps", 24)


def p(rel):
    return rel if os.path.isabs(rel) else os.path.join(base, rel)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("ffmpeg failed:\n" + " ".join(cmd) + "\n" + r.stderr[-2000:])


def has_audio(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                        "stream=index", "-of", "csv=p=0", f], capture_output=True, text=True)
    return bool(r.stdout.strip())


def duration(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", f], capture_output=True, text=True)
    return float(r.stdout.strip())


NORM = f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1"
ENC_V = ["-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS)]
ENC_A = ["-c:a", "aac", "-ar", "48000", "-ac", "2"]

with tempfile.TemporaryDirectory() as tmp:
    parts = []
    for i, c in enumerate(spec["clips"]):
        src, dur = p(c["file"]), float(c["dur"])
        vf = (f"crop={c['crop']}," if c.get("crop") else "") + NORM
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(c.get("start", 0)), "-t", str(dur), "-i", src]
        if has_audio(src):
            amap = "0:a"
        else:
            cmd += ["-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=stereo"]
            amap = "1:a"
        out = os.path.join(tmp, f"part{i:02d}.mp4")
        run(cmd + ["-vf", vf, "-af", "aresample=48000", "-map", "0:v", "-map", amap,
                   "-t", str(dur)] + ENC_V + ENC_A + [out])
        parts.append(out)

    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{x}'\n" for x in parts)
    cut = os.path.join(tmp, "cut.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst] + ENC_V + ENC_A + [cut])
    total = duration(cut)

    final = p(spec["out"])
    a = spec.get("audio")
    if not a:
        run(["ffmpeg", "-v", "error", "-y", "-i", cut, "-c", "copy", final])
    else:
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", cut]
        clip_db = a.get("clip_db", -12)
        chains = [f"[0:a]volume={-90 if clip_db is None else clip_db}dB[c]"]
        labels = ["[c]"]
        k = 1
        for j, v in enumerate(a.get("voiceover", [])):
            cmd += ["-i", p(v["file"])]
            ms = int(round(float(v.get("at", 0)) * 1000))
            chains.append(f"[{k}:a]aresample=48000,adelay={ms}|{ms},volume={a.get('vo_db', 0)}dB[v{j}]")
            labels.append(f"[v{j}]")
            k += 1
        if a.get("music"):
            cmd += ["-i", p(a["music"])]
            chains.append(f"[{k}:a]aresample=48000,atrim=0:{total},volume={a.get('music_db', -18)}dB[m]")
            labels.append("[m]")
        fc = ";".join(chains) + f";{''.join(labels)}amix=inputs={len(labels)}:duration=first:normalize=0[a]"
        run(cmd + ["-filter_complex", fc, "-map", "0:v", "-map", "[a]", "-c:v", "copy"] + ENC_A + [final])
    print(f"final: {final}  {duration(final):.2f} s")

    cmp_ = spec.get("compare")
    if cmp_:
        ref = p(cmp_["reference"])
        T = max(duration(ref), duration(final))
        HC = H // 2
        lab = cmp_.get("labels") or {}
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", ref, "-i", final,
               "-loop", "1", "-t", f"{T:.3f}", "-i", p(cmp_["creator"]),
               "-loop", "1", "-t", f"{T:.3f}", "-i", p(cmp_["product"])]
        idx = {}
        for name in ("reference", "rebuild", "creator", "product"):
            if lab.get(name):
                idx[name] = 4 + len(idx)
                cmd += ["-i", p(lab[name])]

        def tag(stream, name, out):
            if name in idx:
                return f"{stream}[{idx[name]}:v]overlay=(W-w)/2:14[{out}]"
            return f"{stream}null[{out}]"

        card = f"fps={FPS},scale={W}:{HC}:force_original_aspect_ratio=decrease,pad={W}:{HC}:(ow-iw)/2:(oh-ih)/2:color=0x1a1a1a,setsar=1"
        fc = ";".join([
            f"[0:v]{NORM},tpad=stop_mode=clone:stop_duration={T:.3f}[o0]", tag("[o0]", "reference", "o"),
            f"[1:v]{NORM},tpad=stop_mode=clone:stop_duration={T:.3f}[r0]", tag("[r0]", "rebuild", "r"),
            f"[2:v]{card}[c0]", tag("[c0]", "creator", "c"),
            f"[3:v]{card}[p0]", tag("[p0]", "product", "pp"),
            "[c][pp]vstack[cp]", "[o][r][cp]hstack=inputs=3[v]",
        ])
        use = "1:a" if cmp_.get("audio") == "rebuild" or not has_audio(ref) else "0:a"
        fc += f";[{use}]apad[a]"
        run(cmd + ["-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", f"{T:.3f}"]
            + ENC_V + ENC_A + [p(cmp_["out"])])
        print(f"compare: {p(cmp_['out'])}  {duration(p(cmp_['out'])):.2f} s")
