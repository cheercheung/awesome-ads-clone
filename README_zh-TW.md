<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="點此重製成效好的廣告" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="觀看 Claude 廣告重製示範" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ 播放有聲的 Claude 完整示範</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">播放 Awesome Ads Clone 宣傳片</a></p>
</div>

## 🍌 簡介

用 EvoLink MCP 把參考廣告改成適合自家產品的廣告。保留吸引注意力的開頭、產品示範和剪輯節奏，換上自己的創作者、產品、場景與腳本。

## 📊 總覽

12 則廣告重製作品涵蓋產品示範、試穿、短劇、生活影片和對鏡口播。6 個有完整紀錄的案例均提供原片、重製影片和並排比較。另有 6 個測試，各自附上交付的重製片和比較影片。

## ⚡ 快速開始

將 [EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) 接到你的 AI 代理。提供一支參考廣告、一張產品照片和產品說明，再附上創作者照片或選角簡報。接著貼上下面的提示詞。

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
<summary>從 Codex 或 Claude Code 連線</summary>

在 Codex 中執行

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

在 Claude Code 中執行

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

看到提示時，在瀏覽器登入 EvoLink。在 Claude Code 裡，依序選擇 `/mcp` → `evolink` → **Authenticate**。如果 Codex 要求手動登入，請執行 `codex mcp login evolink`。

第一次生成前，請 AI 代理查詢 EvoLink 餘額，並找出支援指定首格的圖生影片模型。分割和剪輯片段需要本機檔案存取權及 FFmpeg/FFprobe。這些步驟可以在同一段對話中完成。

</details>

## 🛠️ 重製廣告的七個步驟

1. **拆解參考廣告。** 以每秒 4 格擷取畫面，針對快速動作和難以判斷的剪接點仔細檢查。記下開頭如何吸引觀眾、產品如何示範、各個鏡頭以及剪接時間。音訊可從現有逐字稿分析，也可使用 AI 代理的音訊功能。
2. **寫出每個鏡頭的目標。** 說明每個鏡頭要換掉哪些內容，並寫出 AI 代理能在輸出中檢查的條件，例如「瓶蓋保持蓋著，直到第 1.5 秒才用手拿起來」。確認產品宣稱後再使用。
3. **按剪接點規劃片段。** 為每個鏡頭準備自己的起始畫格。難以一次完成的連續動作，可在姿勢穩定時切成兩段，以下一段接續前一段最後一個能用的畫格。模型允許時，預留一點時間供剪輯。
4. **確認起始畫格。** 先在靜止畫面核對人物、服裝、包裝、產品狀態、拿法和構圖，再花費預算生成影片。畫面要直接顯示所需狀態，例如瓶身已經拿掉瓶蓋。
5. **把輸入放在一起檢查。** 指定每張圖或每段影片的用途。產品應被遮住時，移除可能讓它露出的產品照，還要確認開頭和結尾能靠預定的運鏡接起來。核准前請 EvoLink MCP 針對實際請求報價。
6. **先生成一段，再檢查。** 對照目標查看起始畫格、主要動作和結尾狀態。修改造成偏差的輸入，或把鏡頭拆開。保留任務 ID 並取回已有結果，再決定是否送出下一個付費任務。
7. **剪輯並檢查。** 修整通過檢查的片段，加入核准的字幕和音訊，再匯出廣告。確認整部影片的節奏和畫面連貫性。若參考素材可以用於比較，就把比較影片和重製片一起交付。

<details>
<summary>選用 Gemini 分析對白、聲音和動作</summary>

EvoLink 的 Gemini 原生 API 可以草擬片段紀錄或逐字稿。這項選用步驟會使用獨立的 `EVOLINK_API_KEY`，並把 MP4 傳給 EvoLink。執行前先確認費用，再用擷取的畫格核對畫面的時間戳記。

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 目錄


| 案例 | 觀看重點 |
| --- | --- |
| [Evopaste 牙膏錠](#case-1) | 三個鏡頭呈現開場鉤子、產品示範和包裝亮相 |
| [E-bra 前扣式內衣試穿](#case-2) | 用一個起始畫格讓內衣維持在 T 恤下面 |
| [Taqueritos 洋芋片短劇](#case-4) （草稿） | 起始和結尾畫格不符，導致意外的交叉淡化 |
| [Gloss Moderne 香水示範](#case-5) （草稿） | 只拍雙手，示範四種不同的產品狀態 |
| [Gym Day 健身生活影片](#case-6) | 從上一段最後一個能用的畫格延續長動作 |
| [連身短褲口播影片](#case-7) | 在對白停頓處剪掉服裝走樣的畫面 |
| [摺疊式太陽能充電器](#n1) | 可摺疊的太陽能板 |
| [紅色鐵盒護膚膏](#n2) | 圓形紅盒護膚膏 |
| [DAILYFORM 蛋白飲](#n3) | 蛋白粉與搖搖杯 |
| [VELORA 精華液](#n4) | 精華液示範 |
| [PACELO 運動鞋開箱](#n5) | 運動鞋開箱 |
| [VELORA Rose 01 香氛](#n6) | 香氛示範 |

## 🎬 案例詳解

<a id="case-1"></a>

### 案例 1: Evopaste 牙膏錠

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="播放重製片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="播放比較影片" width="210"></a> |

**先用畫面點出問題，再用獨立鏡頭示範產品並展示包裝。**

原片用誇張的黃牙畫面做開場，接著切到使用示範和產品特寫。重製片保留三個節拍，換成新的創作者和 Evopaste 咀嚼式牙膏錠的包裝。

三段影片分別呈現開場、起泡示範和包裝。標籤以包裝圖為準。結尾的自拍有文字變成鏡像，需要局部水平翻轉。

匯出的成片長 21.18 秒。原先規劃吐進杯子的動作沒有出現，結尾微笑時嘴唇上還留有紫色泡沫。三段影片當時共花費 2.52 美元。

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### 案例 2: E-bra 前扣式內衣試穿

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="播放重製片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="播放比較影片" width="210"></a> |

**需要把產品藏起來時，用起始畫格明確呈現穿搭層次，再移除相衝的產品照。**

重製片保留了前扣示範、試穿和手勢鏡頭。替換的產品照是一件有 E 標誌的淡紫色花紋內衣。

前幾次沒生成正確的手部和扣合順序，所以前扣鏡頭加入了動作參考。結尾手勢鏡頭使用另一張產品照時，內衣跑到了 T 恤外面。採用的版本改用首格圖生影片，先在起始畫格裡放入 T 恤，再用文字指定手勢。

17.50 秒的成片保留前扣、背面標誌和花紋肩帶。紀錄顯示，最後的剪接點和原片相差不超過兩格。環境底噪隨鏡頭逐漸變小。包含重試，專案當時花費約 7.50 美元。

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### 案例 4: Taqueritos 洋芋片短劇

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="播放重製片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="播放比較影片" width="210"></a> |

**送出請求前，先檢查同一個運鏡能否順利接起首格和末格。**

這支短劇先沿著鋪滿洋芋片袋的沙發從腳拍到臉，再切到演員反應和包裝亮相。重製時更換了演員與零食包裝。

沙發段落的首格和末格中，雙腿及透明袋的位置不同。模型用交叉淡化接起衝突的畫面。提出的修法是從同一張較寬的圖取兩個畫格，只改變取景。

這是前述失敗片段當時用的原始提示詞。

8.20 秒的輸出是草稿。第一個鏡頭在約 2.15–2.60 秒仍有交叉淡化。修法仍停留在提案。到草稿為止，紀錄費用約為 1.90 美元。

<details>
<summary>原始片段提示詞</summary>

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

狀態：草稿

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### 案例 5: Gloss Moderne 香水示範

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="播放重製片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="播放比較影片" width="210"></a> |

**為產品的每種狀態準備起始畫格，並用看得見的動作節拍描述變化。**

影片在停著的車內拍攝，只拍下雙手。四個節拍是噴霧、蓋著瓶蓋的瓶身、打開的盒子和包裝特寫。重製片用了新的香水包裝，並為不同狀態分別準備輸入畫格。

噴霧鏡頭需要兩次短噴，中間要清楚停頓並讓噴嘴回彈。逐格檢查時發現瓶身有旋轉，但影片分析工具沒辨識出來。同時，原本規劃的平移也沒有發生。

這是當時噴霧鏡頭的提示詞。

交付的 7.17 秒草稿保留了原定的剪接時間和兩次噴霧。霧氣很快散開，有些小字在交付畫質下較模糊。加上影片分析，當時費用約為 2.43 美元。

<details>
<summary>原始片段提示詞</summary>

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

狀態：草稿

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### 案例 6: Gym Day 健身生活影片

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="播放重製片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="播放比較影片" width="210"></a> |

**高難度動作在長鏡頭裡走樣時，從最後一個能用的畫格接著生成。**

這部影片只換了創作者，保留鏡前自拍、廚房、門口和運動的順序。廚房裡的容器繼續當作一般道具。

原先生成的臀推只做了一下，人物接著坐了起來。團隊用第 3.0 秒的畫格接續下一段，再趁人物停在低點時接起兩段影片。

這是當時接著生成臀推動作用的提示詞。

成片長 20.08 秒，原片長 20.03 秒。紀錄中的剪接點差異不超過 0.2 秒。重製片保留了音量經標準化的環境底噪。包含續段生成與影片分析，當時費用約為 5.16 美元。

<details>
<summary>原始片段提示詞</summary>

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

### 案例 7: 連身短褲口播影片

| [播放原片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="播放原片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="播放重製片" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="播放比較影片" width="210"></a> |

**生成前先確定各角度的服裝外觀。要剪掉走樣畫面時，先核對對白再決定剪接點。**

原片從側面展示穿著效果，接著口播、用手示範服裝細節，再轉身。重製片使用提供的創作者，並依目標描述生成一件素色摩卡連身短褲。

第二次生成做出比目標更低的後背開口，還增加了一個小刺青。剪輯利用對白的停頓，在後背露出前切掉剩餘的轉身動作，再接到第一個可用的正面畫格。

這是當時側面開場鏡頭的提示詞。

16.62 秒的第二版仍保留了已接受的小刺青。剪輯拿掉了部分對白，讓第三個剪接點比參考影片早了約 1.42 秒。紀錄的製作費用約為 3.02 美元。最終剪輯使用既有素材。

<details>
<summary>原始片段提示詞</summary>

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

## 🧪 其他重製測試

每個測試均提供重製片及並排比較影片。

<a id="n1"></a>

### 摺疊式太陽能充電器

| [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="播放重製片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="播放比較影片" width="240"></a> |

<a id="n2"></a>

### 紅色鐵盒護膚膏

| [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="播放重製片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="播放比較影片" width="240"></a> |

<a id="n3"></a>

### DAILYFORM 蛋白飲

| [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="播放重製片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="播放比較影片" width="240"></a> |

<a id="n4"></a>

### VELORA 精華液

| [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="播放重製片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="播放比較影片" width="240"></a> |

<a id="n5"></a>

### PACELO 運動鞋開箱

| [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="播放重製片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="播放比較影片" width="240"></a> |

<a id="n6"></a>

### VELORA Rose 01 香氛

| [播放重製片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [播放比較影片](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="播放重製片" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="播放比較影片" width="240"></a> |

## 🔗 相關儲存庫

請到 [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin) 查看用戶端設定與工具文件。

## 🙏 致謝

參考廣告歸原創作者所有。如需補充署名、更正或移除某段影片，請開啟 issue 並註明案例名稱。
