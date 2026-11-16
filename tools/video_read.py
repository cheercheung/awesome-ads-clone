#!/usr/bin/env python3
"""Read an MP4 through the optional EvoLink Gemini-native API."""
import argparse
import base64
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ENDPOINT = "https://direct.evolink.ai/v1beta/models/gemini-3.8-flash:generateContent"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--prompt", type=Path, default=Path(__file__).with_name("prompt_scan.txt"))
    parser.add_argument("--target", type=Path)
    args = parser.parse_args()

    key = os.environ.get("EVOLINK_API_KEY", "").strip()
    if not key:
        parser.error("set EVOLINK_API_KEY for this optional API request")
    if args.video.suffix.lower() != ".mp4":
        parser.error("supply an MP4 file")
    if args.output.exists() or args.output.with_suffix(args.output.suffix + ".usage.json").exists():
        parser.error("choose a new output filename to preserve the previous result")

    prompt = args.prompt.read_text(encoding="utf-8")
    if "{{TARGET}}" in prompt:
        if args.target is None:
            parser.error("this prompt requires --target")
        prompt = prompt.replace("{{TARGET}}", args.target.read_text(encoding="utf-8").strip())

    parts = [
        {"inlineData": {"mimeType": "video/mp4", "data": base64.b64encode(args.video.read_bytes()).decode("ascii")}},
        {"text": prompt},
    ]
    request = Request(
        ENDPOINT,
        data=json.dumps({
            "contents": [{"role": "user", "parts": parts}],
            "generationConfig": {"temperature": 0.2, "maxOutputTokens": 16000},
        }).encode("utf-8"),
        method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urlopen(request, timeout=120) as response:
            result = json.load(response)
    except HTTPError as error:
        parser.exit(1, f"Gemini returned HTTP {error.code}. Check the request and account before retrying.\n")
    except (URLError, TimeoutError) as error:
        parser.exit(1, f"Gemini response could not be retrieved ({type(error).__name__}). Check usage before retrying.\n")

    candidates = result.get("candidates", [])
    response_parts = candidates[0].get("content", {}).get("parts", []) if candidates else []
    report = "\n".join(
        part["text"] for part in response_parts if part.get("text") and not part.get("thought")
    ).strip()
    if not report:
        parser.exit(1, "Gemini returned no report. Check the clip and response status.\n")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report + "\n", encoding="utf-8")
    args.output.with_suffix(args.output.suffix + ".usage.json").write_text(
        json.dumps(result.get("usageMetadata", {}), indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
