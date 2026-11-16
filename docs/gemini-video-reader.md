# Optional Gemini video reader

Use this route if you want a timestamped draft of the reference's actions, speech, or sound cues, or a second check against a clip target. The production workflow can begin with FFmpeg frames and your own transcript. Historical case notes that mention the reader refer to the EvoLink Gemini-native API.

This option sends the supplied MP4 to EvoLink and uses a separate `EVOLINK_API_KEY`. Check the account-facing model price and use a clip you can share with the provider. Use a small MP4 or segment the footage if needed. The model ID is `gemini-3.8-flash`. [EvoLink Gemini-native route](https://evolink.ai/blog/how-to-use-gemini-3-8-flash-api).

Supply the key through your shell's environment or a secret manager. From the repository root, run:

```sh
mkdir -p work
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
python3 tools/video_read.py work/clip.mp4 work/clip-check.md \
  --prompt tools/prompt_compare.txt --target work/clip-target.md
```

Each invocation makes one API request and writes the response text and a separate usage file. Cross-check timestamps with frames and listen to the actual audio for ambiguous words or cues. Treat uncertain observations as uncertain in the plan.
