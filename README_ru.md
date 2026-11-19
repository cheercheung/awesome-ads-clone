<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="Нажмите, чтобы воссоздать успешную рекламу" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="Смотреть, как Claude воссоздаёт рекламу" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ Смотреть полную демонстрацию Claude со звуком</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">Смотреть трейлер Awesome Ads Clone</a></p>
</div>

## 🍌 Введение

Используйте EvoLink MCP, чтобы воссоздать рекламный ролик для своего продукта по образцу. Сохраните приём, который привлекает внимание в начале, способ показа продукта и ритм монтажа. Замените участника, продукт, обстановку и сценарий на свои.

## 📊 Обзор

В 12 примерах есть демонстрации продуктов, примерки, скетч, влог и реклама с обращением в камеру. Для каждого из 6 примеров с описанием работы доступны оригинал, воссозданный ролик и видео со сравнением. В 6 дополнительных тестах показаны полученные ролики и сравнения.

## ⚡ Быстрый старт

Подключите [EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) к своему агенту. Передайте ему рекламный ролик для образца, фото и описание продукта, а также фото участника или требования к кастингу. Затем вставьте этот промпт.

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
<summary>Подключение из Codex или Claude Code</summary>

Для Codex

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

Для Claude Code

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

Когда появится запрос, войдите в EvoLink в браузере. В Claude Code выберите `/mcp` → `evolink` → **Authenticate**. Если Codex просит войти вручную, выполните `codex mcp login evolink`.

Перед первой генерацией попросите агента проверить баланс EvoLink и подобрать модель, которая генерирует видео из изображения с заданным начальным кадром. Для нарезки и монтажа агенту нужен доступ к локальным файлам и FFmpeg/FFprobe. Всё это можно сделать в том же диалоге.

</details>

## 🛠️ Метод в семь шагов

1. **Разберите ролик-образец.** Извлеките 4 кадра в секунду и подробнее проанализируйте быстрые движения и неочевидные склейки. Запишите, что привлекает внимание в начале, как показывают продукт, какие есть планы и где они сменяются. Для звука используйте готовую расшифровку или функции анализа аудио у агента.
2. **Опишите нужный результат.** Перечислите, что заменить в каждом плане. Сформулируйте критерии, которые агент сможет проверить в результате, например «крышка остаётся на месте, пока рука не поднимет её на 1,5 секунде». Согласуйте утверждения о продукте перед использованием.
3. **Спланируйте клипы по точкам монтажа.** Задайте начальный кадр для каждого плана. Сложное непрерывное движение разделите в момент, когда поза стабильна. Начните следующий клип с последнего пригодного кадра предыдущего. Если модель позволяет, оставьте запас для обрезки.
4. **Проверьте начальные кадры.** Прежде чем тратить средства на видео, проверьте на статичном изображении участника, одежду, упаковку, состояние продукта, хват и кадрирование. Покажите продукт именно в нужном состоянии, например флакон без крышки.
5. **Проверьте, согласуются ли исходные материалы.** У каждого изображения или клипа должна быть одна задача. Уберите фото продукта, если по сценарию его не должно быть видно, и проверьте, что задуманное движение соединяет начальный и конечный кадры. До подтверждения запросите у EvoLink MCP расчёт стоимости для конкретных параметров.
6. **Сгенерируйте один клип и проверьте его.** Сверьте первый кадр, основное действие и конечное состояние с заданием. Замените источник, из-за которого возникло отклонение, или разделите план. Сохраните ID задачи и получите её результат перед отправкой новой платной задачи.
7. **Соберите ролик и просмотрите его.** Обрежьте принятые клипы, добавьте согласованные титры и звук и экспортируйте рекламу. Проверьте ритм и непрерывность всего ролика. Если ролик-образец можно использовать для сравнения, приложите сравнительную версию к готовой рекламе.

<details>
<summary>Анализ реплик, звуков и действий через Gemini (необязательно)</summary>

Нативный API Gemini в EvoLink может подготовить черновой журнал клипов или расшифровку. На этом необязательном шаге используется отдельный `EVOLINK_API_KEY`, а MP4 отправляется в EvoLink. Перед запуском проверьте стоимость. Сверьте таймкоды видеоряда с извлечёнными кадрами.

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 Содержание


| Пример | На что обратить внимание |
| --- | --- |
| [Таблетки для чистки зубов Evopaste](#case-1) | Завязка, показ продукта в действии и появление упаковки в трёх планах |
| [Примерка бюстгальтера E-bra с передней застёжкой](#case-2) | Как одним начальным кадром оставить бельё под футболкой |
| [Скетч с чипсами Taqueritos](#case-4) (черновик) | Наплыв из-за несовпадения начального и конечного кадров |
| [Демонстрация парфюма Gloss Moderne](#case-5) (черновик) | Четыре состояния продукта в демонстрации, где видны только руки |
| [Влог о дне в спортзале](#case-6) | Как продолжить длинное движение с последнего пригодного кадра |
| [Рассказ на камеру о посадке комбинезона-шорт](#case-7) | Пауза в речи как точка монтажа для скрытия изменений одежды |
| [Складное солнечное зарядное устройство](#n1) | Складная солнечная панель |
| [Красная баночка с бальзамом](#n2) | Круглая красная баночка с бальзамом |
| [Протеиновый коктейль DAILYFORM](#n3) | Протеиновый порошок и шейкер |
| [Сыворотка VELORA](#n4) | Демонстрация сыворотки |
| [Распаковка кроссовок PACELO](#n5) | Распаковка кроссовок |
| [Аромат VELORA Rose 01](#n6) | Демонстрация аромата |

## 🎬 Примеры с описанием работы

<a id="case-1"></a>

### Пример 1: Таблетки для чистки зубов Evopaste

| [Смотреть оригинал](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="Смотреть оригинал" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="Смотреть воссозданный ролик" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="Смотреть сравнение" width="210"></a> |

**Покажите проблему в первом кадре, который привлечёт внимание, а демонстрацию и упаковку вынесите в отдельные планы.**

В оригинале сначала показывают нарочито жёлтые зубы, затем использование продукта и его крупный план. В новом ролике сохранили эти три эпизода, заменив участника и упаковку на жевательные таблетки для чистки зубов Evopaste.

Три клипа разделили завязку, демонстрацию пены и кадр с упаковкой. Надписи брали с изображения упаковки. В финальном селфи пришлось отразить часть кадра по горизонтали, чтобы исправить зеркальный текст.

Экспортированный ролик длился 21,18 секунды. Запланированный момент, когда участник сплёвывает в стакан, выпал. При финальной улыбке на губах осталась фиолетовая пена. Генерация трёх клипов тогда обошлась в 2,52 доллара США.

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### Пример 2: Примерка бюстгальтера E-bra с передней застёжкой

| [Смотреть оригинал](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="Смотреть оригинал" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="Смотреть воссозданный ролик" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="Смотреть сравнение" width="210"></a> |

**Когда продукт должен оставаться скрытым, задайте порядок слоёв одежды в начальном кадре и уберите противоречащее ему фото товара.**

В новом ролике сохранили показ передней застёжки, примерку и планы с жестами рук. На фото заменяющего продукта был сиреневый бюстгальтер с узором и меткой E.

Первые дубли неверно передавали последовательность движений рук и работы застёжки, поэтому для этого плана понадобился образец движения. В финальном плане с жестом отдельное фото продукта вывело бюстгальтер поверх футболки. В принятом клипе видео сгенерировали из начального изображения, на котором уже была футболка, а жест задали текстом.

В итоговом ролике на 17,50 секунды сохранились передняя застёжка, метка на спине и бретель с узором. Зафиксированные точки склейки отличались от оригинала не более чем на 2 кадра. Фоновый звук помещения становился тише от плана к плану. С повторными попытками работа тогда обошлась примерно в 7,50 доллара США.

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### Пример 4: Скетч с чипсами Taqueritos

| [Смотреть оригинал](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="Смотреть оригинал" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="Смотреть воссозданный ролик" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="Смотреть сравнение" width="210"></a> |

**Перед отправкой запроса проверьте, что задуманное движение камеры может связать начальный и конечный кадры.**

В скетче камера движется от ног к лицу по дивану, заваленному пакетами с чипсами. Далее идут реакция и показ упаковки. В новом ролике заменили исполнителя и упаковку снеков.

В первом и последнем кадрах движения по дивану ноги и прозрачные пакеты находились в разных местах. Модель соединила их наплывом. Предложение по исправлению состояло в том, чтобы взять оба крайних кадра из одного более широкого изображения, меняя только кадрирование.

Ниже приведён использованный тогда промпт первого клипа для неудачного дубля, описанного выше.

Экспорт на 8,20 секунды остался черновиком. В первом плане сохранился наплыв примерно с 2,15 по 2,60 секунды. Исправление осталось предложением в плане. На момент черновика было потрачено около 1,90 доллара США.

<details>
<summary>Промпт, использованный для клипа</summary>

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

Статус: черновик

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### Пример 5: Демонстрация парфюма Gloss Moderne

| [Смотреть оригинал](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="Смотреть оригинал" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="Смотреть воссозданный ролик" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="Смотреть сравнение" width="210"></a> |

**Подготовьте начальный кадр для каждого состояния продукта и опишите действие по отдельным наблюдаемым этапам.**

В ролике, снятом в припаркованной машине, видны только руки. Четыре этапа показа продукта — распыление, флакон с закрытой крышкой, открытая коробка и упаковка крупным планом. Для нового ролика использовали упаковку другого парфюма и отдельные входные кадры для каждого состояния.

В клипе с распылителем нужны были два коротких распыления с явной паузой и возвратом распылителя в исходное положение. Покадровый просмотр плана с флаконом выявил вращение, которое пропустил инструмент анализа видео. При этом запланированного перемещения не было.

Ниже приведён промпт, использованный для клипа с распылением.

Переданный черновик на 7,17 секунды сохранил тайминг склеек и оба распыления. Облачко быстро рассеялось, а часть мелкого текста в переданном качестве выглядела размытой. Вместе с анализом видео работа тогда обошлась примерно в 2,43 доллара США.

<details>
<summary>Промпт, использованный для клипа</summary>

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

Статус: черновик

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### Пример 6: Влог о дне в спортзале

| [Смотреть оригинал](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="Смотреть оригинал" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="Смотреть воссозданный ролик" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="Смотреть сравнение" width="210"></a> |

**Если в длинном дубле сбивается сложное движение, продолжите его с последнего пригодного кадра.**

Заменили только участника и сохранили последовательность влога: селфи в зеркале, кухня, дверь и упражнения. Кухонные ёмкости оставили обычным реквизитом.

В первой генерации упражнения с подъёмом таза участница сделала один повтор, а затем села. Для следующей генерации взяли кадр на 3,0 секунде. Продолжение склеили с первым клипом в паузе в нижнем положении.

Ниже приведён промпт, использованный для продолжения упражнения с подъёмом таза.

Итоговый ролик длится 20,08 секунды, ролик-образец — 20,03 секунды. Разница в зафиксированных точках склейки составила не более 0,2 секунды. В новом ролике сохранился нормализованный фоновый звук. Продолжение и анализ видео вошли в расходы примерно на 5,16 доллара США.

<details>
<summary>Промпт, использованный для клипа</summary>

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

### Пример 7: Рассказ на камеру о посадке комбинезона-шорт

| [Смотреть оригинал](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="Смотреть оригинал" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="Смотреть воссозданный ролик" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="Смотреть сравнение" width="210"></a> |

**До генерации определите ракурсы одежды, а перед выбором точки обрезки для скрытия отклонения проверьте реплики.**

Ролик-образец сочетал вступительный план сбоку, в котором видна посадка одежды, обращение в камеру, жесты, показывающие одежду, и поворот. Для нового ролика взяли предоставленный образ участницы и однотонный комбинезон-шорты цвета мокко, созданный по описанию.

Во второй генерации вырез на спине получился глубже, чем требовалось, а у участницы появилась небольшая татуировка. В итоговом монтаже поворот обрезали на паузе в речи, пока спина ещё не была видна, а затем продолжили с первого пригодного кадра анфас.

Ниже приведён промпт вступительного плана сбоку, использованный при генерации.

Во второй версии на 16,62 секунды оставили татуировку. Монтаж убрал часть реплики и перенёс третью склейку примерно на 1,42 секунды раньше по сравнению с оригиналом. Зафиксированные производственные расходы составили около 3,02 доллара США. Итоговый монтаж сделали из уже полученного видео.

<details>
<summary>Промпт, использованный для клипа</summary>

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

## 🧪 Дополнительные тесты воссоздания

Для каждого теста есть воссозданный ролик и видео со сравнением.

<a id="n1"></a>

### Складное солнечное зарядное устройство

| [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="Смотреть воссозданный ролик" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="Смотреть сравнение" width="240"></a> |

<a id="n2"></a>

### Красная баночка с бальзамом

| [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="Смотреть воссозданный ролик" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="Смотреть сравнение" width="240"></a> |

<a id="n3"></a>

### Протеиновый коктейль DAILYFORM

| [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="Смотреть воссозданный ролик" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="Смотреть сравнение" width="240"></a> |

<a id="n4"></a>

### Сыворотка VELORA

| [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="Смотреть воссозданный ролик" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="Смотреть сравнение" width="240"></a> |

<a id="n5"></a>

### Распаковка кроссовок PACELO

| [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="Смотреть воссозданный ролик" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="Смотреть сравнение" width="240"></a> |

<a id="n6"></a>

### Аромат VELORA Rose 01

| [Смотреть воссозданный ролик](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [Смотреть сравнение](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="Смотреть воссозданный ролик" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="Смотреть сравнение" width="240"></a> |

## 🔗 Связанные репозитории

Инструкции по подключению клиента и работе с инструментами доступны в [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin).

## 🙏 Благодарности

Права на оригинальные рекламные ролики принадлежат их создателям. Если нужно указать авторство, внести исправление или удалить ролик, создайте задачу (Issue) с названием примера.
