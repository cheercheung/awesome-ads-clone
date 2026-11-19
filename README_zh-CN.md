<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="点击复刻高表现广告" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="观看 Claude 广告复刻演示" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ 播放带声音的 Claude 完整演示</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">播放 Awesome Ads Clone 宣传片</a></p>
</div>

## 🍌 简介

用 EvoLink MCP 把一支参考广告复刻成适合自家产品的广告。保留开场钩子、产品演示和剪辑节奏，换成自己的创作者、产品、场景和脚本。

## 📊 概览

12 个复刻实例涵盖产品演示、试穿、短剧、视频日志和口播广告。6 个有完整记录的案例均提供原片、复刻成片和并排对比。另有 6 个测试，均可观看测试交付的复刻片和对比片。

## ⚡ 快速开始

将 [EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) 接入你的智能体。提供一支参考广告、一张产品图和产品描述，再附上创作者照片或选角要求。然后粘贴下面的提示词。

```text
Use EvoLink MCP to rebuild this reference ad for my product. Keep the hook,
the order of the shots, and the way the ad shows what the product does.
Replace the creator, product, setting, and script with my own. Use only the
claims I approve.

Reference ad: [attach the video]
Product: [attach a photo and describe what it does]
Creator: [attach a photo or describe who you want on screen]
Output: [for example, a 15-second vertical ad]

First check the inputs, length, and visual requirements. Show me the shot
plan, recommended models and estimated cost. Wait for my approval before
generating. Make and check the first shot, then check the remaining shots
against the plan. Track the original task IDs and return an edited MP4 and
a private side-by-side comparison.
```

<details>
<summary>在 Codex 或 Claude Code 中接入</summary>

在 Codex 中运行

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

在 Claude Code 中运行

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

出现提示时，在浏览器登录 EvoLink。在 Claude Code 中依次选择 `/mcp` → `evolink` → **Authenticate**。如果 Codex 要求手动登录，运行 `codex mcp login evolink`。

首次生成前，让智能体查看 EvoLink 余额，并查找支持首帧的图生视频模型。拆分和剪辑片段需要本地文件访问权限以及 FFmpeg/FFprobe。这些步骤可以在同一对话里完成。

</details>

## 🛠️ 七步复刻法

1. **拆解参考广告。** 按每秒 4 帧抽样，仔细查看快速动作和不易辨认的切点。记录开场钩子、产品如何演示、镜头内容和切点。音频可以用现有转录稿分析，也可以交给支持音频的智能体。
2. **写清目标。** 逐镜头说明要替换的内容，并写出可以直接检查的条件，例如「到第 1.5 秒才由手把瓶盖提起」。涉及产品的宣传说法先确认，再写进广告。
3. **按切点规划片段。** 为每个镜头准备独立首帧。难以一次生成的连续动作，可以在姿势稳定时拆分，让下一段从上一段的最后一个可用画面接起。模型允许时，多留一点用于剪辑的时长。
4. **确认首帧。** 先在静帧上核对人物、服装、包装、产品状态、握持方式和构图，再花钱生成视频。画面要呈现实际需要的状态，例如瓶盖已经取下。
5. **一起检查输入。** 给每张图或每段视频指定一个用途。产品本应被遮住时，移除可能导致它露出的产品图。检查预期运镜能否连续衔接首帧和尾帧。确认前请 EvoLink MCP 为这次具体请求报价。
6. **先生成一段并检查。** 对照目标检查首帧、主要动作和结尾状态。调整造成偏差的输入，或拆分镜头。保存任务 ID 并取回已有结果，再决定是否提交新的付费任务。
7. **剪辑并复查。** 修剪已确认的片段，加上已获批准的字幕和音频，再导出广告。检查整片的节奏和连贯性。如果参考素材可用于对比，就和复刻片一起交付对比片。

<details>
<summary>可选：用 Gemini 分析对白、声音和动作</summary>

EvoLink 的 Gemini 原生 API 可以起草片段记录或转录稿。这一步需要单独的 `EVOLINK_API_KEY`，并会把 MP4 发给 EvoLink。运行前先确认费用，再用抽取的帧核对画面时间戳。

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 目录


| 案例 | 观看要点 |
| --- | --- |
| [Evopaste 牙膏片](#case-1) | 用三个镜头完成钩子、产品演示和包装亮相 |
| [E-bra 前扣内衣试穿](#case-2) | 用一个首帧让内衣始终藏在 T 恤下面 |
| [Taqueritos 薯片短剧](#case-4) （草稿） | 首尾帧冲突导致意外叠化 |
| [Gloss Moderne 香水演示](#case-5) （草稿） | 只拍双手，呈现四种不同产品状态 |
| [Gym Day 健身视频日志](#case-6) | 从最后一个可用画面接续长动作 |
| [连体短裤口播广告](#case-7) | 借对白停顿剪掉服装走样的画面 |
| [折叠式太阳能充电器](#n1) | 可折叠太阳能板 |
| [红色铁盒润肤膏](#n2) | 圆形红盒润肤膏 |
| [DAILYFORM 蛋白饮品](#n3) | 蛋白粉和摇摇杯 |
| [VELORA 精华液](#n4) | 精华液演示 |
| [PACELO 运动鞋开箱](#n5) | 运动鞋开箱 |
| [VELORA Rose 01 香氛](#n6) | 香氛演示 |

## 🎬 案例详解

<a id="case-1"></a>

### 案例 1: Evopaste 牙膏片

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="播放复刻片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="播放对比片" width="210"></a> |

**用视觉钩子呈现问题，产品演示和包装亮相各用一个镜头。**

原片先用夸张的黄牙画面抓住注意力，接着演示使用，最后给出产品特写。复刻片保留这三个节拍，换用新创作者和 Evopaste 咀嚼牙膏片包装。

三个片段分别拍钩子、起泡演示和包装。图中文字以包装图为准。结尾自拍中有文字被镜像，需要在局部做水平翻转。

导出的成片长 21.18 秒。演示少了原计划把泡沫吐进杯子的动作，结尾微笑时嘴唇还留有紫色泡沫。三个片段当时共花费 2.52 美元。

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### 案例 2: E-bra 前扣内衣试穿

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="播放复刻片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="播放对比片" width="210"></a> |

**需要藏住产品时，用首帧明确衣物层次，并去掉与之冲突的产品图。**

复刻片保留了前扣演示、试穿和手势镜头。替换用的产品图显示一件淡紫色花纹内衣，上面有 E 标志。

早期结果没做对手部操作和扣合的次序，所以前扣镜头加入了动作参考。最后一个手势镜头里，单独的产品图让内衣跑到了 T 恤外面。最终采用首帧图生视频，让首帧先显示 T 恤，再用文字指定手势。

17.50 秒的成片保留了前扣、背面标记和花纹肩带。记录的最终切点与参考片相差不超过两帧。各镜头环境底噪逐渐变小。项目当时约花费 7.50 美元，含重试。

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### 案例 4: Taqueritos 薯片短剧

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="播放复刻片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="播放对比片" width="210"></a> |

**提交前先确认，同一个运镜能不能自然接起首帧和尾帧。**

短剧先沿铺满薯片袋的沙发从脚拍到脸，再切到人物反应和包装亮相。复刻片替换了表演者和零食包装。

沙发运镜的首尾帧中，双腿和透明袋的位置不同。模型用叠化来衔接这种冲突。提出的修法是从同一张更宽的图取首尾帧，只改变取景。

这是上面那次失败镜头所用的首段提示词。

8.20 秒的导出仍是草稿，第一镜头在约 2.15–2.60 秒处仍有叠化。修法仅记录在计划里。做到这版草稿为止，记录费用约为 1.90 美元。

<details>
<summary>原始片段提示词</summary>

```text
The same person, outfit, sofa and room as the first and last frames. Raw unedited home video, one continuous take, no cuts.
CAMERA: handheld, high angle looking down at the sofa. 0-1.5 s the camera travels smoothly from her feet along her body toward her head, moving left and lowering slightly; her face comes into frame at about 1.5 s. 1.5-4 s the camera keeps drifting slowly and settles on her upper body. From 4 s to the end the camera holds almost still, ending exactly on the last frame.
ACTION: she lies on her back on the sofa, buried in a deep pile of sealed snack bags, eyes closed, relaxed and content. From the moment her face is visible, her raised hand stays at her mouth, elbow resting on the sofa back, holding a few red rolled chips and pushing them into her mouth one after another: one at about 2 s, one at about 3.5 s, one at about 5 s. Between bites she chews slowly, lips coated with red seasoning powder. Her legs and feet stay still. The bags lie still on and around her.
PHYSICS: the bags are light sealed foil bags; their printed fronts stay flat and unchanged as the camera moves. The chips are rigid and crunchy. The two large clear plastic bags of red rolled chips stay where they are.
LIGHTING: as in the frames, soft daylight; no flash, no ring light.
NEGATIVES: no CGI sheen, no plastic skin, no warped hands, no extra fingers, no stiff movement, no robotic face, no jitter, no flicker, no unintended slow motion, no identity drift, no warped labels, no distorted packaging, no fake branding, no on-screen text, no captions, no second person, no cut. No purple or blue snack bags, no teal or green chips, no hat, the hoodie is never taken off, she never sits up, she never opens a bag.
SOUND: quiet room tone, soft foil crinkle, crunchy chewing; no music, no speech.
```

</details>

状态：草稿

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### 案例 5: Gloss Moderne 香水演示

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="播放复刻片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="播放对比片" width="210"></a> |

**为产品的每种实际状态准备首帧，把动作写成画面里可观察的节拍。**

这支演示在停着的车内拍摄，只拍双手。四个环节是喷雾、盖好瓶盖的瓶身、打开的盒子和包装特写。复刻片换用新的香水包装，每种状态都用独立输入帧。

喷雾片段需要两次短喷，中间明确停顿并让喷头复位。人工逐帧检查发现瓶身转了角度，视频分析工具漏掉了这个动作，而计划中的平移并未发生。

这是当时喷雾片段使用的提示词。

交付的 7.17 秒草稿保留了切点和两次喷雾。雾气散得较快，成片画质下有些小字偏模糊。包含视频分析在内，当时约花费 2.43 美元。

<details>
<summary>原始片段提示词</summary>

```text
The same hand, sleeve, trousers, bottle and car as the first frame. Raw unedited phone video, one continuous take, no cuts.
ACTION: 0-0.8 s the hand holds the bottle still, index finger resting on top of the silver spray nozzle. 0.8-1.0 s the index finger presses the nozzle down once: a short fine puff of mist shoots out of the nozzle opening and drifts up and to the right, thinning out. 1.0-1.9 s the finger lifts, the nozzle springs back up, the hand holds still while the mist fades. 1.9-2.1 s the index finger presses the nozzle down a second time: a second short puff of mist, same direction. 2.1 s to the end the finger lifts, the hand holds the bottle still and the mist fades away.
PHYSICS: the mist is a fine pale translucent spray in a small cone that dissipates within a second; it is not smoke, not steam, not a liquid jet, and leaves no droplets on the glass. The bottle is rigid glass with a weighted grip, fingers keep contact; the white label stays flat and its text unchanged; the clear liquid barely moves.
CAMERA: handheld phone looking down at the lap, slight natural sway, no zoom, no pan.
LIGHTING: as in the first frame, soft overcast daylight; no flash.
NEGATIVES: no CGI sheen, no plastic skin, no warped hands, no extra fingers, no stiff movement, no jitter, no flicker, no unintended slow motion, no warped labels, no distorted packaging, no fake branding, no on-screen text, no captions, no second person, no cut. No cap appearing on the bottle, no ring, no bracelet, no second bottle, no face, no thick smoke, the bottle is never put down.
SOUND: quiet parked-car interior room tone, two short soft spray hisses; no music, no speech.
```

</details>

状态：草稿

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### 案例 6: Gym Day 健身视频日志

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="播放复刻片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="播放对比片" width="210"></a> |

**高难度动作在长镜头里跑偏时，从上一段最后一个可用的画面继续。**

这一版只换了创作者，保留镜前自拍、厨房、门口和运动的顺序。厨房里的容器仍作普通道具使用。

初版臀推做完一次后，人物变成坐起。团队拿第 3.0 秒的画面续生成下一段，在人物保持低位时把两个片段接上。

这是当时续生成臀推片段使用的提示词。

成片长 20.08 秒，参考片长 20.03 秒。记录的切点相差不超 0.2 秒。复刻片保留了音量标准化后的环境底噪。含续生成和视频分析在内，当时约花费 5.16 美元。

<details>
<summary>原始片段提示词</summary>

```text
The same person, outfit, machine and gym as the first frame. Raw unedited phone video, vertical 9:16, one continuous take, no cuts; the phone stands still at knee height.
ACTION: 0-1.3 s she rests in the low position on the hip thrust machine, upper back on the back pad, breathing, eyes half closed. 1.3-2.6 s she drives her hips up against the hip pad until her thighs are about horizontal and her torso is in line with her thighs. 2.6-4 s she holds at the top, then starts to lower. Her upper back stays on the back pad the whole time, both hands stay on the handles, both feet stay flat on the platform, her head stays resting back on the pad; the glasses stay on.
PHYSICS: the machine's lever arm and the weight plates rise and fall with her hips as one rigid unit; the pad presses into the shorts; the weight looks heavy, the movement is controlled.
CAMERA: fixed phone at knee height beside her, no movement, no zoom.
LIGHTING: as in the first frame, cool white overhead light; no flash.
NEGATIVES: no CGI sheen, no plastic skin, no warped hands, no extra fingers, no stiff movement, no robotic face, no jitter, no flicker, no unintended slow motion, no identity drift, no fake branding, no on-screen text, no captions, no second person, no cut. No lettering on the plates or the machine; she does not sit up, does not lean forward, does not stand up.
SOUND: gym room tone, the soft clank of the plates; no music, no speech.
```

</details>

Type: Demo | Date: 2026-11-12

<a id="case-7"></a>

### 案例 7: 连体短裤口播广告

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="播放复刻片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="播放对比片" width="210"></a> |

**生成前明确各角度的服装样式，选剪辑点避开走样时先检查对白。**

原片用侧面展示上身效果作为钩子，接着口播、用手展示衣服细节，再转身。复刻片使用提供的创作者和按目标描述生成的纯色摩卡连体短裤。

第二次生成把后背开口做得比目标更低，还多了一个小纹身。剪辑在背部露出前的对白停顿处切掉剩余转身动作，再从第一个可用的正面画面接回去。

这是当时用于侧面开场的提示词。

16.62 秒的第二版仍保留了接受的小纹身。剪辑去掉了部分对白，让第三个切点比参考片早约 1.42 秒。记录的制作费用约为 3.02 美元，最终剪辑用了已有片段。

<details>
<summary>原始片段提示词</summary>

```text
The same person, outfit and room as the first frame. Raw unedited phone video, vertical 9:16, one continuous take, no cuts. A close side view of a young woman showing the fit of her romper; her face stays above the top edge of the frame for the whole clip.
ACTION: 0-5 s she holds the side pose: chest facing the right side of the frame, hips toward the left side; a small, slow side-to-side sway of the hips and a gentle shift of weight from one leg to the other; the torso stays in profile; the arm reaching back toward the upper left moves only slightly. She does not turn toward the camera, does not walk, and her head does not come into the frame.
PHYSICS: the matte knit romper stretches and moves naturally with the body; the thin straps stay on the shoulder; the hem of the shorts stays at the upper thigh.
CAMERA: handheld phone at waist height, close, very slight natural sway; no zoom, no pan; the crop stays from the shoulder to just above the knees.
LIGHTING: as in the first frame, soft daylight from the window on the left; no striped shadows, no flash, no ring light.
NEGATIVES: no CGI sheen, no plastic skin, no warped hands, no extra fingers, no stiff movement, no jitter, no flicker, no unintended slow motion, no identity drift, no fake branding, no on-screen text, no captions, no second person, no cut. No face in the frame, no long hair, no blonde hair, no black clothing, no satin sheen, no bracelet, no ring, no blind shadows, no white doors, no grey carpet, no exaggerated curves.
SOUND: quiet bedroom room tone only; no speech, no voice, no music.
```

</details>

Type: Demo | Date: 2026-11-12

## 🧪 更多复刻测试

每个测试均提供复刻片和并排对比片。

<a id="n1"></a>

### 折叠式太阳能充电器

| [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="播放复刻片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="播放对比片" width="240"></a> |

<a id="n2"></a>

### 红色铁盒润肤膏

| [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="播放复刻片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="播放对比片" width="240"></a> |

<a id="n3"></a>

### DAILYFORM 蛋白饮品

| [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="播放复刻片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="播放对比片" width="240"></a> |

<a id="n4"></a>

### VELORA 精华液

| [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="播放复刻片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="播放对比片" width="240"></a> |

<a id="n5"></a>

### PACELO 运动鞋开箱

| [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="播放复刻片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="播放对比片" width="240"></a> |

<a id="n6"></a>

### VELORA Rose 01 香氛

| [播放复刻片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [播放对比片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="播放复刻片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="播放对比片" width="240"></a> |

## 🔗 相关仓库

通过 [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin) 查看客户端配置和工具文档。

## 🙏 致谢

参考广告归各自的创作者所有。如需补充署名、更正或移除某个片段，请发起 issue 并注明案例名称。
