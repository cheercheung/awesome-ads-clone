<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="클릭해 성과가 좋은 광고를 재현하기" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="Claude 광고 재현 데모 보기" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ 소리와 함께 Claude 데모 전체 재생</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">Awesome Ads Clone 예고편 재생</a></p>
</div>

## 🍌 소개

EvoLink MCP로 참고 광고를 내 제품에 맞게 재현합니다. 도입부의 후킹 요소, 제품을 보여 주는 방식, 편집의 리듬은 살리고 출연자, 제품, 배경, 대본은 원하는 것으로 바꿉니다.

## 📊 개요

광고 재현 12건에는 제품 시연, 착용, 상황극, 브이로그, 카메라를 보며 말하는 광고가 포함됩니다. 제작 과정이 기록된 6건은 각각 원본, 재현 영상, 나란히 비교한 영상을 제공합니다. 추가 테스트 6건에는 각 테스트에서 제공된 재현 영상과 비교 영상이 있습니다.

## ⚡ 빠른 시작

에이전트에 [EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent)을 연결합니다. 참고 광고, 제품 이미지와 설명, 출연자 이미지 또는 캐스팅 조건을 전달한 뒤 아래 프롬프트를 붙여 넣습니다.

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
<summary>Codex 또는 Claude Code에서 연결하기</summary>

Codex 사용 시

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

Claude Code 사용 시

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

로그인 안내가 뜨면 브라우저에서 EvoLink에 로그인합니다. Claude Code에서는 `/mcp` → `evolink` → **Authenticate**를 선택합니다. Codex가 수동 로그인을 요청하면 `codex mcp login evolink`를 실행합니다.

첫 영상을 생성하기 전에 에이전트에게 EvoLink 잔액을 확인하고 시작 프레임을 지정해 이미지에서 영상을 생성할 수 있는 모델을 찾아 달라고 하세요. 클립을 분할하고 편집하려면 로컬 파일 접근 권한과 FFmpeg/FFprobe가 필요합니다. 에이전트는 같은 대화에서 이 작업을 진행할 수 있습니다.

</details>

## 🛠️ 7단계 작업 방법

1. **참고 영상을 분석합니다.** 초당 4프레임을 추출하고 빠른 동작이나 전환 지점이 모호한 부분은 더 자세히 살펴봅니다. 오프닝의 후킹 요소, 제품 시연, 각 쇼트와 편집점을 기록합니다. 음성은 제공된 대본이나 에이전트의 오디오 분석 기능으로 확인합니다.
2. **재현 목표를 작성합니다.** 각 쇼트에서 바꿀 항목을 정합니다. “1.5초에 손이 들어 올릴 때까지 뚜껑이 닫혀 있다”처럼 에이전트가 결과에서 확인할 수 있는 기준을 작성합니다. 제품 관련 주장이나 표현은 사용하기 전에 확인합니다.
3. **편집점을 기준으로 클립을 계획합니다.** 각 쇼트에 시작 프레임을 지정합니다. 이어지는 동작이 어렵다면 자세가 안정된 지점에서 나눕니다. 다음 클립은 직전 클립의 마지막으로 쓸 수 있는 프레임에서 시작합니다. 모델이 허용하면 앞뒤를 잘라낼 여유도 둡니다.
4. **시작 프레임을 확인합니다.** 영상 생성에 비용을 쓰기 전에 정지 이미지에서 출연자, 의상, 포장, 제품 상태, 쥐는 방식, 구도를 점검합니다. 뚜껑을 뺀 병처럼 실제로 필요한 상태를 시작 프레임에 담습니다.
5. **입력 자료를 함께 점검합니다.** 이미지나 클립마다 역할을 하나씩 부여합니다. 제품이 가려져야 하는 장면과 충돌하는 제품 사진은 빼고, 의도한 움직임으로 시작 프레임에서 끝 프레임까지 이어질 수 있는지 확인합니다. 승인 전에 EvoLink MCP에 실제 요청 조건으로 견적을 받습니다.
6. **클립 하나를 생성해 검사합니다.** 첫 프레임, 주요 동작, 마지막 상태를 목표와 비교합니다. 어긋난 원인이 된 입력을 바꾸거나 쇼트를 나눕니다. 새 유료 작업을 제출하기 전에 작업 ID를 저장하고 기존 결과를 먼저 가져옵니다.
7. **클립을 이어 붙이고 검토합니다.** 채택한 클립의 앞뒤를 정리하고 승인된 자막과 오디오를 넣어 광고를 내보냅니다. 전체 영상의 리듬과 연결이 자연스러운지 확인합니다. 참고 영상을 비교에 사용할 수 있으면 재현 영상과 함께 비교 영상도 전달합니다.

<details>
<summary>Gemini로 대사, 소리, 동작 분석하기(선택)</summary>

EvoLink의 Gemini 네이티브 API로 클립 기록이나 대본의 초안을 만들 수 있습니다. 이 선택 단계에서는 별도의 `EVOLINK_API_KEY`를 사용하고 MP4를 EvoLink에 전송합니다. 실행 전에 비용을 확인하고, 영상의 타임스탬프를 추출한 프레임과 대조합니다.

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 목차


| 사례 | 살펴볼 점 |
| --- | --- |
| [Evopaste 고체 치약 정제](#case-1) | 오프닝, 제품 시연, 포장 공개를 세 쇼트로 구성 |
| [E-bra 앞여밈 브라 착용](#case-2) | 시작 프레임 한 장으로 브라가 티셔츠 안에 위치하도록 설정 |
| [Taqueritos 칩 상황극](#case-4) (초안) | 시작 프레임과 끝 프레임의 불일치로 생긴 디졸브 |
| [Gloss Moderne 향수 데모](#case-5) (초안) | 손만 나오는 시연에서 제품의 네 가지 상태를 보여 주는 방법 |
| [헬스장에서의 하루 브이로그](#case-6) | 마지막으로 쓸 수 있는 프레임에서 긴 동작을 이어 가는 방법 |
| [롬퍼의 착용감을 소개하는 광고](#case-7) | 대사 사이의 멈춤을 활용해 의상 불일치를 잘라내는 방법 |
| [접이식 태양광 충전기](#n1) | 접이식 태양광 패널 |
| [빨간 밤 용기](#n2) | 빨갛고 둥근 밤 용기 |
| [DAILYFORM 단백질 셰이크](#n3) | 단백질 파우더와 셰이커 |
| [VELORA 세럼](#n4) | 세럼 시연 |
| [PACELO 스니커즈 개봉](#n5) | 스니커즈 개봉 |
| [VELORA Rose 01 향수](#n6) | 향수 시연 |

## 🎬 제작 과정이 기록된 사례

<a id="case-1"></a>

### 사례 1: Evopaste 고체 치약 정제

| [원본 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="원본 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="재현 영상 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="비교 영상 재생" width="210"></a> |

**시선을 끄는 장면으로 문제를 제시하고 시연과 포장에는 각각 별도의 쇼트를 배정합니다.**

참고 영상은 과장된 누런 치아로 시작해 제품 사용 장면과 제품 클로즈업으로 이어집니다. 재현 영상은 이 세 장면의 흐름을 유지하면서 출연자를 바꾸고 Evopaste 씹는 치약 정제를 사용했습니다.

오프닝, 거품 시연, 포장 장면을 세 클립으로 나눴습니다. 라벨은 포장 이미지를 기준으로 맞췄습니다. 마지막 셀피에서는 글자가 거울처럼 뒤집힌 부분을 가로로 반전해 바로잡았습니다.

내보낸 영상은 21.18초입니다. 예정했던 컵에 뱉는 동작은 빠졌고, 마지막에 미소 지을 때 입술에 보라색 거품이 남았습니다. 당시 세 클립의 영상 생성 비용은 총 2.52달러였습니다.

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### 사례 2: E-bra 앞여밈 브라 착용

| [원본 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="원본 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="재현 영상 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="비교 영상 재생" width="210"></a> |

**제품을 가려야 할 때는 시작 프레임에서 옷의 겹침을 정하고, 그와 충돌하는 제품 사진을 뺍니다.**

재현 영상은 앞여밈 잠금장치 시연, 착용, 손동작 장면을 유지했습니다. 교체 제품 사진에는 E 표시가 달린 연보라색 무늬 브라가 담겼습니다.

앞선 결과에서 손동작과 잠금장치의 순서가 맞지 않아 앞여밈 쇼트에 동작 참고 영상이 필요했습니다. 마지막 손동작에 별도의 제품 이미지를 넣자 브라가 티셔츠 밖에 나타났습니다. 채택한 결과는 티셔츠가 이미 보이는 프레임을 시작점으로 이미지에서 영상을 만들고, 손동작은 글로 지정했습니다.

최종 영상은 17.50초이며 앞여밈 잠금장치, 등쪽 표시, 무늬가 있는 끈을 유지했습니다. 기록된 최종 편집점은 참고 영상과 2프레임 이내로 일치했습니다. 쇼트가 진행될수록 배경의 현장 소리는 작아졌습니다. 재시도를 포함한 당시 제작 비용은 약 7.50달러였습니다.

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### 사례 4: Taqueritos 칩 상황극

| [원본 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="원본 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="재현 영상 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="비교 영상 재생" width="210"></a> |

**요청을 제출하기 전에 의도한 카메라 움직임으로 시작 프레임과 끝 프레임을 연결할 수 있는지 확인합니다.**

상황극은 칩 봉지가 쌓인 소파에서 발부터 얼굴까지 카메라가 이동한 뒤, 반응과 포장이 드러나는 장면으로 넘어갑니다. 이 작업에서는 출연자와 대상 과자의 포장 디자인을 바꿨습니다.

소파를 따라 이동하는 쇼트의 처음과 끝에서 다리와 투명 봉지의 위치가 달랐습니다. 모델은 이를 디졸브로 이어 붙였습니다. 제안한 수정 방법은 한 장의 넓은 이미지에서 구도만 바꿔 양쪽 프레임을 만드는 것이었습니다.

아래는 위에서 설명한 실패한 테이크의 첫 클립에 썼던 프롬프트입니다.

8.20초 영상은 초안입니다. 첫 쇼트의 약 2.15~2.60초 구간에는 디졸브가 남아 있습니다. 수정 방법은 계획에 제안으로 남아 있습니다. 초안까지 기록된 비용은 약 1.90달러였습니다.

<details>
<summary>실제 클립 제작에 사용한 프롬프트</summary>

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

상태: 초안

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### 사례 5: Gloss Moderne 향수 데모

| [원본 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="원본 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="재현 영상 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="비교 영상 재생" width="210"></a> |

**제품의 실제 상태별로 시작 프레임을 준비하고, 확인할 수 있는 동작 단위로 설명합니다.**

주차한 차 안에서 손만 보여 주는 시연은 분사, 뚜껑을 닫은 병, 열린 상자, 포장 클로즈업이라는 네 장면으로 이루어집니다. 재현 작업에서는 교체한 향수 포장과 각 상태에 맞는 별개의 입력 프레임을 사용했습니다.

분사 클립에는 작은 분무 두 번, 그 사이의 명확한 정지, 노즐이 원래 위치로 돌아가는 동작이 필요했습니다. 병 클립의 프레임을 직접 확인하자 영상 분석에서 놓친 회전이 보였고, 계획했던 위치 이동은 없었습니다.

아래는 분사 클립을 만들 때 썼던 프롬프트입니다.

제공된 7.17초 초안은 편집 타이밍과 두 번의 분사를 유지했습니다. 분무는 금방 사라졌고, 납품 화질에서는 작은 글자 일부가 흐릿해졌습니다. 영상 분석을 포함한 당시 비용은 약 2.43달러였습니다.

<details>
<summary>실제 클립 제작에 사용한 프롬프트</summary>

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

상태: 초안

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### 사례 6: 헬스장에서의 하루 브이로그

| [원본 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="원본 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="재현 영상 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="비교 영상 재생" width="210"></a> |

**긴 테이크에서 어려운 동작이 흐트러지면 마지막으로 쓸 수 있는 프레임부터 이어서 생성합니다.**

출연자만 바꿔 거울 셀피, 주방, 문, 운동으로 이어지는 브이로그의 순서를 유지했습니다. 주방의 용기는 특정 브랜드가 없는 소품으로 남겼습니다.

처음 생성한 힙 스러스트 영상은 동작을 한 번 한 뒤 출연자가 상체를 일으켜 버렸습니다. 3.0초 지점의 프레임을 다음 생성의 입력으로 사용해 동작을 이어 만들고, 몸을 낮춘 채 잠시 멈춘 지점에서 두 클립을 연결했습니다.

아래는 힙 스러스트 동작을 이어 생성할 때 썼던 프롬프트입니다.

최종 영상은 20.08초, 참고 영상은 20.03초였습니다. 기록된 편집 타이밍의 차이는 0.2초 이내였습니다. 재현 영상은 음량을 정규화한 현장 소리를 유지했습니다. 이어지는 동작 생성과 영상 분석을 포함한 당시 비용은 약 5.16달러였습니다.

<details>
<summary>실제 클립 제작에 사용한 프롬프트</summary>

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

### 사례 7: 롬퍼의 착용감을 소개하는 광고

| [원본 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="원본 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="재현 영상 재생" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="비교 영상 재생" width="210"></a> |

**생성 전에 의상이 보이는 각도를 확정하고, 의상 불일치를 숨길 편집점을 고르기 전에 대사를 확인합니다.**

참고 영상은 옆모습으로 핏을 보여 주는 도입부, 카메라를 보며 말하는 장면, 옷을 손으로 가리키는 동작과 몸을 돌리는 동작을 결합했습니다. 재현 영상에는 제공한 출연자와 목표 설명에 맞춘 무늬 없는 모카색 롬퍼를 사용했습니다.

두 번째 생성에서는 등쪽 파임이 목표보다 깊어졌고 작은 문신도 생겼습니다. 선택한 편집은 등이 보이기 전 대사가 잠시 끊기는 부분에서 회전을 잘라내고, 다시 정면을 향하는 첫 번째 쓸 만한 프레임부터 이어 붙였습니다.

아래는 오프닝의 옆모습 쇼트에 썼던 프롬프트입니다.

16.62초짜리 두 번째 버전에는 그대로 두기로 한 문신이 남아 있습니다. 편집 과정에서 대사 일부를 덜어 내고 세 번째 편집점을 참고 영상보다 약 1.42초 앞당겼습니다. 기록된 제작 비용은 약 3.02달러입니다. 최종 편집에는 기존에 생성한 영상을 사용했습니다.

<details>
<summary>실제 클립 제작에 사용한 프롬프트</summary>

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

## 🧪 추가 재현 테스트

각 테스트에 재현 영상과 나란히 비교한 영상이 있습니다.

<a id="n1"></a>

### 접이식 태양광 충전기

| [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="재현 영상 재생" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="비교 영상 재생" width="240"></a> |

<a id="n2"></a>

### 빨간 밤 용기

| [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="재현 영상 재생" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="비교 영상 재생" width="240"></a> |

<a id="n3"></a>

### DAILYFORM 단백질 셰이크

| [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="재현 영상 재생" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="비교 영상 재생" width="240"></a> |

<a id="n4"></a>

### VELORA 세럼

| [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="재현 영상 재생" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="비교 영상 재생" width="240"></a> |

<a id="n5"></a>

### PACELO 스니커즈 개봉

| [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="재현 영상 재생" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="비교 영상 재생" width="240"></a> |

<a id="n6"></a>

### VELORA Rose 01 향수

| [재현 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [비교 영상 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="재현 영상 재생" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="비교 영상 재생" width="240"></a> |

## 🔗 관련 저장소

클라이언트 설정과 도구 사용법은 [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin)에서 확인하세요.

## 🙏 제작자 표기

원본 참고 광고는 각각 해당 제작자에게 귀속됩니다. 제작자 표기 추가, 정정 또는 삭제가 필요한 영상이 있다면 사례 이름을 적어 이슈를 열어 주세요.
