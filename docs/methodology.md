# The seven-step ad rebuild method

Keep the ad's narrative structure: the first thing that earns attention, the action that demonstrates the product, and the timing and order of the cuts. Write a new execution around your own creator, product, setting, and approved claims.

Start with a reference video you can use, product photos and a sentence explaining the product, and creator photos or a casting brief. Work from [this agent brief](agent-brief.md). The examples assume a short vertical ad, but the clip planning method also applies to other formats.

## 1. Read the reference

Pull frames at 4 fps for the first pass, then inspect more densely around ambiguous cuts, fast hand motions, and reveals. Save the first frame of every shot. Record action, camera, product state, text, and sound by timestamp. Use native audio analysis or a supplied transcript for sound. When neither is available, mark that part of the reference as unknown. For additional help with dialogue, sound cues, or a draft action log, see the [optional Gemini reader](gemini-video-reader.md).

```sh
mkdir -p work/reference-frames
ffmpeg -hide_banner -i reference.mp4 -an -vf fps=4 work/reference-frames/frame-%05d.jpg
```

Summarize the source ad in functional terms. Identify the hook, the offer if present, the proof, and what changes at each cut. If a video reader and sampled frames disagree about a visual event, inspect the event at the source frame rate and use the visible evidence.

## 2. Write the target

Make a swap map for creator, product, clothes, location, on-screen copy, and sound. Check that your product can actually perform the reference action before preserving that beat. Write a target sheet for each clip with visible must-show details, exclusions, and timestamps for the actions.

| Target | Check |
| --- | --- |
| Product state | The lid stays on until the hand lifts it at 1.5 seconds. |
| Identity and wardrobe | The same creator wears the green T-shirt through the cut. |
| Exclusion | Keep the reference creator, room, branding, and claims out of the final. |

## 3. Plan clips and choose how to constrain them

Use hard cuts as clip boundaries. Split a long or difficult continuous shot at a stable pose or product state. The next clip can begin at the last usable frame of the preceding clip. Allow about half a second to one second of trim room when the model permits. For each clip, record the source range, planned length, start-frame source, required references, trim window, and estimate. Review the plan and budget together.

| Need | Input to try |
| --- | --- |
| Simple action, all visible facts already in frame 0 | Confirmed start frame and timed action text. |
| Precise grip, pose, garment layer, or product state | Choose or edit an image to show that exact state before generating video. |
| Complex motion or interaction | Add an authorized motion reference if supported, or split the action at a stable state. |
| Exact end state | Use a compatible end frame if supported. Place both frames side by side to check continuity. |
| Legible offer text, captions, or interface | Use approved copy and place it in post-production. |

## 4. Build and check the start frames

Use EvoLink MCP to find an image model with the needed generation or edit capability and estimate the exact request. Build the start frame, then compare it with the target sheet and the reference geometry. Inspect the actual creator, outfit, product state, hand placement, and framing. Mark each criterion pass or fail and correct misses while they are still in a still image.

## 5. Check the video inputs and get a quote

For every input, record what it controls. Check the inputs against the target and against each other. A packshot can contradict a worn or hidden product. A motion clip may bring along an unwanted person or room. A first frame and a last frame may be impossible to join with a continuous camera move.

Write only the motion, timing, camera, physical behavior, sound, and exclusions that need text. Use `get_model` and `estimate_cost` for the chosen input mode and exact parameters. After approval, preserve those parameters and pass through the `pricing_quote` when provided. If a quote has expired or input changes, estimate again. Where final pricing depends on token usage, explain the unresolved cost and wait for an explicit decision. [MCP tool reference](https://evolink.ai/docs/en/mcp/tools).

## 6. Generate, inspect, and repair

Generate one clip first. Save its task ID, reported charge, actual output, and verdict. Compare frame 0, the proof action, and the end state with the target. Keep the exact trim range that passes. When a detail fails, change the relevant input, constrain it more directly, or split the clip. Recheck any other clip that used the same input or rule.

Poll the original task instead of generating a second clip when a request is still processing. Download completed results promptly. Start the rest of the shots once the first clip validates the approach.

## 7. Assemble and check the whole ad

Use local FFmpeg to trim the passed clip versions, normalize dimensions, frame rate, and audio, and join them in order. Add approved on-screen copy in post. The [Python 3 assembly helper](../tools/assemble.py) accepts a JSON edit plan with per-clip trim windows. Paths are relative to that JSON file. For example, save this as `work/edit.json` and run `python3 -I tools/assemble.py work/edit.json`.

```json
{
  "size": [540, 960],
  "fps": 24,
  "clips": [
    {"file": "clips/hook.mp4", "start": 0.35, "dur": 3.5},
    {"file": "clips/proof.mp4", "start": 0.10, "dur": 4.0}
  ],
  "out": "rebuild.mp4"
}
```

For a private three-panel comparison, add `"compare": {"reference": "reference.mp4", "creator": "creator.jpg", "product": "product.png", "audio": "rebuild", "out": "comparison.mp4"}` at the top level of the edit plan. This uses the rebuild's audio for the comparison.

Review the actual export. Confirm the hook, product proof, cut times, continuity, readable copy, and audio transitions. Check each export window for reference material and unintended claims. Aim for cuts within roughly 0.2 seconds and overall length within roughly 0.3 seconds of the intended timing when the brief calls for a close match. Record every meaningful deviation. Deliver the export, a private reference/rebuild comparison when you can use the reference in it, and the clip verdicts and costs.

The default audio deliverable is usable clip audio or silence with a planned sound pass. If dialogue or music is part of the concept, use audio you have permission to use and check the resulting cut by listening. The [Romper case](../cases/c7-romper-talking-head/README.md) documents a run with generated dialogue.

## What to record on every clip

| Field | Example |
| --- | --- |
| Intended proof | At 1.5 s the finger presses the nozzle and a fine mist appears. |
| Visual inputs | Start frame shows the uncapped bottle and finger on the nozzle. |
| Acceptance | Mist dissipates, bottle stays rigid, key label stays legible. |
| Actual result | Two sprays appear. First puff disappears earlier than intended. |
| Edit decision | Keep the accepted window and record the visual defect. |
| Cost | Store the quote, submitted task ID, and settled or reported charge separately. |
