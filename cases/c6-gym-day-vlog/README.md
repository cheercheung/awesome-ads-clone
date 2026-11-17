# Gym Day vlog

| [Play original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [Play rebuild](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [Play comparison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="Play original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="Play rebuild" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="Play comparison" width="210"></a> |

**Continue a demanding physical action from the last usable frame when the long take drifts.**

## What was rebuilt

The creator-only swap preserved the vlog sequence of mirror selfie, kitchen, door, and exercise. The kitchen containers remained generic props.

## The production decision

The original hip-thrust generation performed one rep and then drifted into the creator sitting up. The team used the frame at 3.0 seconds as the continuation input, generated the next beat, and joined it during the low hold.

This is the historical hip-thrust continuation prompt. [Clip prompt](clip-prompt.txt).

## Result and limits

The final ran 20.08 seconds versus 20.03 seconds for the reference. The recorded cut timings were within 0.2 seconds. The rebuild kept normalized room tone. Historical spend including the continuation and reader was about $5.16.

Source: `04-Clone-Cases/c6-Gym-day-vlog/rebuild-plan.md` in the AI Ad Clone Pack. See the [asset inventory](../../data/cases.json) for the original file mapping.
