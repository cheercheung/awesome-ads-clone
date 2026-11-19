<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="クリックして成果の出る広告を再現" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="Claude で広告を再現するデモを見る" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ Claude デモの全編を音声付きで再生</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">Awesome Ads Clone の予告編を再生</a></p>
</div>

## 🍌 はじめに

EvoLink MCP を使って、お手本の広告を自社製品向けに再現します。冒頭の引き、製品の見せ方、編集のテンポを活かしながら、出演者、製品、舞台設定、台本を自分のものに差し替えます。

## 📊 概要

12 件の広告再現例には、製品デモ、試着、寸劇、Vlog、カメラに向かって話す広告があります。記録のある 6 件では、元動画、再現動画、比較動画を見られます。追加テスト 6 件には、各テストで提供された再現動画と比較動画を掲載しています。

## ⚡ クイックスタート

[EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) をエージェントに接続します。参考広告、製品の画像と説明、出演者の画像またはキャスティングの要件を渡してから、以下のプロンプトを貼り付けます。

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
<summary>Codex または Claude Code から接続</summary>

Codex の場合

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

Claude Code の場合

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

案内が表示されたら、ブラウザーで EvoLink にログインします。Claude Code では `/mcp` → `evolink` → **Authenticate** の順に選びます。Codex が手動でのログインを求めたら、`codex mcp login evolink` を実行します。

初回の生成前に、EvoLink の残高を確認し、開始フレームを指定できる画像から動画への生成モデルを探すようエージェントに依頼します。クリップの分割と編集にはローカルファイルへのアクセスと FFmpeg/FFprobe が必要です。これらの作業は同じ会話で進められます。

</details>

## 🛠️ 7 ステップの手順

1. **参考動画を分析する。** 毎秒 4 フレームを取り出し、速い動きや切り替わりが不明瞭な箇所を詳しく確認します。冒頭の引き、製品の見せ方、各ショットと切り替わる時刻を記録します。音声は既存の書き起こし、またはエージェントの音声解析機能で確認します。
2. **目標を明文化する。** 各ショットで差し替える要素を指定します。「開始から 1.5 秒で手が持ち上げるまで、ふたは閉じたまま」のように、生成結果から判断できるチェック項目を書きます。製品に関する表現は使用前に確認します。
3. **カットに合わせてクリップを計画する。** 各ショットに開始フレームを用意します。難しい連続動作は姿勢が安定したところで分割し、直前の使える最後のフレームから次のクリップを始めます。モデルが許す範囲で編集用の余尺も確保します。
4. **開始フレームを確認する。** 動画生成に費用をかける前に、静止画で出演者、衣装、パッケージ、製品の状態、持ち方、構図を確認します。ふたのないボトルなど、必要とする実際の状態を開始フレームに写します。
5. **素材同士の整合性を確認する。** 画像やクリップごとに役割を一つ決めます。製品が隠れる場面と矛盾する製品写真は外し、開始と終了のフレームが想定した動きでつながるか確認します。承認前に、実際に送る条件で EvoLink MCP に見積もりを依頼します。
6. **1 本のクリップを生成して確認する。** 開始フレーム、主な動作、終了時の状態を目標と照らし合わせます。ずれの原因となった素材を変更するか、ショットを分割します。別の有料ジョブを送る前にタスク ID を保存し、すでに生成された結果を取得します。
7. **つないで見直す。** 採用したクリップをトリミングし、承認済みの字幕と音声を加えて広告を書き出します。全編のテンポとつながりを確認します。参考動画を比較に使える場合は、再現動画と一緒に比較版も提出します。

<details>
<summary>Gemini でセリフ・音・動作を分析する（任意）</summary>

EvoLink の Gemini ネイティブ API では、クリップの記録や書き起こしの下書きを作れます。この任意の手順では別途 `EVOLINK_API_KEY` が必要で、MP4 を EvoLink に送信します。実行前に費用を確認し、映像のタイムスタンプを抽出したフレームと照合します。

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 目次


| ケース | 注目点 |
| --- | --- |
| [Evopaste の歯磨きタブレット](#case-1) | 冒頭の引き、製品の実演、パッケージのお披露目を 3 ショットで構成 |
| [E-bra のフロントホックブラ試着](#case-2) | 開始フレーム 1 枚でブラを T シャツの下に収める |
| [Taqueritos のチップス寸劇](#case-4) （下書き） | 開始・終了フレームの不一致で生じたディゾルブ |
| [Gloss Moderne の香水デモ](#case-5) （下書き） | 手元だけのデモで 4 つの異なる製品状態を見せる |
| [ジムでの一日を追う Vlog](#case-6) | 使える最後のフレームから長い動作を続ける |
| [ロンパースの着用感を語る広告](#case-7) | セリフの間を利用して衣装のずれをカットで隠す |
| [折りたたみ式ソーラー充電器](#n1) | 折りたたみ式ソーラーパネル |
| [赤いバーム缶](#n2) | 赤く丸いバーム缶 |
| [DAILYFORM のプロテインシェイク](#n3) | プロテインパウダーとシェーカー |
| [VELORA の美容液](#n4) | 美容液のデモ |
| [PACELO のスニーカー開封](#n5) | スニーカーの開封 |
| [香水 VELORA Rose 01](#n6) | フレグランスのデモ |

## 🎬 制作記録のあるケース

<a id="case-1"></a>

### ケース 1: Evopaste の歯磨きタブレット

| [元動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="元動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="再現動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="比較動画を再生" width="210"></a> |

**視覚的な引きで問題を提示し、実演とパッケージは別々のショットで見せます。**

参考動画は誇張した黄ばんだ歯の映像で始まり、使用場面、製品のアップへと切り替わります。再現動画はこの 3 つの展開を保ち、出演者を差し替え、製品には Evopaste の噛んで使う歯磨きタブレットを採用しました。

冒頭の引き、泡立ちの実演、パッケージの映像を 3 本のクリップに分けました。ラベルはパッケージ画像を参照しました。最後の自撮りでは、一部を水平反転して文字の左右反転を修正しました。

書き出しは 21.18 秒でした。予定していたカップに吐き出す場面は省かれ、最後に笑うときは唇に紫色の泡が残りました。当時の 3 クリップの動画生成費は合計 2.52 米ドルでした。

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### ケース 2: E-bra のフロントホックブラ試着

| [元動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="元動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="再現動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="比較動画を再生" width="210"></a> |

**製品を隠す必要がある場合は、開始フレームで衣装の重なりを決め、矛盾する製品写真を外します。**

再現動画はフロントホックの実演、試着、手振りのショットを引き継ぎました。差し替える製品写真には、E のマークが付いたラベンダー色の柄入りブラが写っていました。

初期のテイクでは手の動きとホックを留める順序が合わず、フロントホックのショットに動作の参考動画が必要でした。最後の手振りのショットでは、別添の製品画像を使うとブラが T シャツの外に現れました。採用したテイクでは、T シャツがすでに写った画像を開始フレームに使って動画化し、手振りは文章で指定しました。

17.50 秒の完成版には、フロントホック、背面のマーク、柄入りのストラップが残りました。記録上、完成版のカット位置は参考動画から 2 フレーム以内で、環境音はショットが進むにつれて小さくなりました。再試行を含めた当時の制作費は約 7.50 米ドルでした。

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### ケース 4: Taqueritos のチップス寸劇

| [元動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="元動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="再現動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="比較動画を再生" width="210"></a> |

**送信前に、開始フレームと終了フレームが想定したカメラの動きでつながるか確認します。**

寸劇は、チップスの袋で覆われたソファの上を足元から顔へ移動し、リアクションとパッケージのお披露目へ切り替わる構成です。今回の生成では出演者と対象のお菓子のパッケージを差し替えました。

ソファ上を移動するショットでは、開始と終了で脚と透明な袋の位置が異なりました。モデルはその食い違いをディゾルブでつなぎました。修正案は、同じ広い画像から構図だけを変えて両端のフレームを作ることでした。

以下は、上記の失敗したテイクで使用した最初のクリップのプロンプトです。

8.20 秒の書き出しは下書きです。最初のショットでは約 2.15〜2.60 秒にディゾルブが残っています。上記の修正は計画上の提案です。下書きまでに記録された費用は約 1.90 米ドルでした。

<details>
<summary>実際に使ったクリップのプロンプト</summary>

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

ステータス：下書き

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### ケース 5: Gloss Moderne の香水デモ

| [元動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="元動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="再現動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="比較動画を再生" width="210"></a> |

**製品の状態ごとに開始フレームを用意し、動作を確認できる単位で指定します。**

駐車した車内で手元だけを映すデモは、噴霧、ふた付きボトル、開いた箱、パッケージのアップという 4 つの場面で構成されます。再現版では差し替え用の香水パッケージと、各状態に対応する別々の入力フレームを使いました。

噴霧クリップでは、2 回軽く噴霧し、その間に間を空けてノズルを元の位置に戻す必要がありました。ボトルのショットをフレームで確認すると、動画解析では検出されなかった回転があり、予定した平行移動はありませんでした。

以下は、噴霧クリップで使用したプロンプトです。

納品した 7.17 秒の下書きは、カットのタイミングと 2 回の噴霧を保ちました。霧はすぐに消え、納品時の画質では一部の小さな文字がぼやけました。動画解析を含む当時の費用は約 2.43 米ドルでした。

<details>
<summary>実際に使ったクリップのプロンプト</summary>

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

ステータス：下書き

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### ケース 6: ジムでの一日を追う Vlog

| [元動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="元動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="再現動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="比較動画を再生" width="210"></a> |

**長回しで難しい動作が崩れたら、使える最後のフレームから続きを生成します。**

出演者だけを差し替え、鏡越しの自撮り、キッチン、ドア、トレーニングという Vlog の流れを保ちました。厨房の容器は一般的な小道具のままとしました。

最初のヒップスラストの生成では、1 回動作した後に出演者が起き上がってしまいました。3.0 秒のフレームを入力にして続きを生成し、腰を下げたまま止まっている部分で前後をつなぎました。

以下は、ヒップスラストの続きを生成したときのプロンプトです。

完成版は 20.08 秒で、参考動画は 20.03 秒でした。記録されたカットの時刻は 0.2 秒以内に収まっています。再現版は音量を正規化した環境音を維持しました。続きの生成と動画解析を含む当時の費用は約 5.16 米ドルでした。

<details>
<summary>実際に使ったクリップのプロンプト</summary>

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

### ケース 7: ロンパースの着用感を語る広告

| [元動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="元動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="再現動画を再生" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="比較動画を再生" width="210"></a> |

**生成前に衣装の見え方を決め、ずれを隠す編集点を選ぶ前にセリフを確認します。**

参考動画は、横向きで着用感を見せる冒頭、カメラに向かって話す場面、衣装を手で示す動作、振り返りを組み合わせていました。再現版には、提供された出演者と、要件に沿った無地のモカ色のロンパースを使いました。

2 回目の生成では背中が指定より深く開き、小さなタトゥーが追加されました。採用した編集では、背中が見える前のセリフの間で振り返りを切り、再び正面を向いている最初の使えるフレームから続けました。

以下は、横向きの冒頭ショットに使ったプロンプトです。

16.62 秒の第 2 版には、許容したタトゥーが残っています。編集でセリフの一部が省かれ、3 番目のカットは参考動画より約 1.42 秒早くなりました。記録された制作費は約 3.02 米ドルです。最終編集にはすでに生成済みの映像を使いました。

<details>
<summary>実際に使ったクリップのプロンプト</summary>

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

## 🧪 追加の再現テスト

各テストに再現動画と比較動画があります。

<a id="n1"></a>

### 折りたたみ式ソーラー充電器

| [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="再現動画を再生" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="比較動画を再生" width="240"></a> |

<a id="n2"></a>

### 赤いバーム缶

| [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="再現動画を再生" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="比較動画を再生" width="240"></a> |

<a id="n3"></a>

### DAILYFORM のプロテインシェイク

| [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="再現動画を再生" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="比較動画を再生" width="240"></a> |

<a id="n4"></a>

### VELORA の美容液

| [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="再現動画を再生" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="比較動画を再生" width="240"></a> |

<a id="n5"></a>

### PACELO のスニーカー開封

| [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="再現動画を再生" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="比較動画を再生" width="240"></a> |

<a id="n6"></a>

### 香水 VELORA Rose 01

| [再現動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [比較動画を再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="再現動画を再生" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="比較動画を再生" width="240"></a> |

## 🔗 関連リポジトリ

クライアントの設定方法やツールの使い方は [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin) を参照してください。

## 🙏 クレジット

元の参考広告は、それぞれの制作者に帰属します。クレジットの追加、訂正、削除が必要な場合は、ケース名を添えて Issue を作成してください。
