<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="Per Klick erfolgreiche Werbeanzeigen nachbauen" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="Claude-Demo zum Nachbau einer Werbeanzeige ansehen" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ Vollständige Claude-Demo mit Ton abspielen</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">Trailer zu Awesome Ads Clone abspielen</a></p>
</div>

## 🍌 Einführung

Baue mit EvoLink MCP eine Referenzanzeige für dein eigenes Produkt nach. Behalte den Einstieg, die Produktvorführung und den Schnittrhythmus bei. Setze deine eigene Person vor der Kamera, dein Produkt, deinen Schauplatz und dein Skript ein.

## 📊 Überblick

Die zwölf nachgebauten Anzeigen umfassen Produktdemos, Anproben, einen Sketch, einen Vlog und eine Anzeige mit direkter Kameraansprache. In den sechs dokumentierten Fällen siehst du jeweils das Original, den Nachbau und einen direkten Vergleich. Zu den sechs weiteren Tests findest du jeweils den gelieferten Nachbau und Vergleich.

## ⚡ Schnellstart

Verbinde [EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) mit deinem Agenten. Gib ihm eine Referenzanzeige, ein Produktfoto samt Beschreibung sowie ein Foto der Person vor der Kamera oder ein Casting-Briefing. Füge dann diesen Prompt ein.

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
<summary>Verbindung in Codex oder Claude Code einrichten</summary>

In Codex

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

In Claude Code

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

Melde dich bei Aufforderung im Browser bei EvoLink an. Wähle in Claude Code `/mcp` → `evolink` → **Authenticate**. Wenn Codex eine manuelle Anmeldung verlangt, führe `codex mcp login evolink` aus.

Lass deinen Agenten vor der ersten Generierung das EvoLink-Guthaben prüfen und ein Bild-zu-Video-Modell suchen, das aus einem Startbild arbeitet. Zum Aufteilen und Schneiden der Clips braucht er lokalen Dateizugriff und FFmpeg/FFprobe. Das erledigt er im selben Chat.

</details>

## 🛠️ Methode in sieben Schritten

1. **Analysiere die Vorlage.** Ziehe vier Einzelbilder pro Sekunde und sieh dir schnelle Bewegungen und unklare Schnitte genauer an. Notiere den Aufhänger am Anfang, die Produktvorführung, die Einstellungen und deren Schnittpunkte. Nutze für den Ton ein vorhandenes Transkript oder die Audiofunktionen des Agenten.
2. **Beschreibe das gewünschte Ergebnis.** Lege fest, was du in jeder Einstellung austauschen willst. Formuliere Prüfkriterien, die der Agent im Ergebnis kontrollieren kann, etwa „Der Deckel bleibt auf der Flasche, bis die Hand ihn nach 1,5 Sekunden anhebt.“ Prüfe Aussagen über das Produkt, bevor du sie übernimmst.
3. **Plane die Clips entlang der Schnitte.** Gib jeder Einstellung ein eigenes Startbild. Teile schwierige, durchgehende Bewegungen an einer stabilen Pose. Beginne den nächsten Clip mit dem letzten brauchbaren Bild. Plane je nach Modell etwas Reserve zum Kürzen ein.
4. **Gib die Startbilder frei.** Prüfe Person, Kleidung, Verpackung, Produktzustand, Griff und Bildausschnitt im Standbild, bevor du für ein Video bezahlst. Zeige den tatsächlich benötigten Zustand, etwa eine Flasche ohne Deckel.
5. **Prüfe die Eingaben im Zusammenspiel.** Gib jedem Bild oder Clip eine klare Aufgabe. Entferne ein Produktfoto, wenn es dem gewünschten verdeckten Zustand widerspricht. Prüfe, ob die vorgesehene Bewegung das Start- und Endbild verbinden kann. Lass dir von EvoLink MCP vor der Freigabe den Preis für genau diesen Auftrag nennen.
6. **Erzeuge und prüfe einen Clip.** Vergleiche das erste Bild, die Hauptbewegung und den Endzustand mit dem gewünschten Ergebnis. Ersetze die Eingabe, die den Fehler verursacht hat, oder teile die Einstellung auf. Speichere die Auftrags-ID und rufe das vorhandene Ergebnis ab, bevor du einen weiteren kostenpflichtigen Auftrag abschickst.
7. **Schneide und kontrolliere die Anzeige.** Kürze die freigegebenen Clips, ergänze freigegebene Texteinblendungen und Ton und exportiere die Anzeige. Prüfe Rhythmus und Anschlüsse im gesamten Video. Wenn du die Vorlage für einen Vergleich verwenden darfst, liefere ihn zusammen mit dem Nachbau.

<details>
<summary>Optional: Dialoge, Geräusche und Bewegungen mit Gemini auswerten</summary>

Die native Gemini-API von EvoLink kann einen ersten Einstellungsbericht oder ein Transkript erstellen. Dieser optionale Schritt verwendet einen separaten `EVOLINK_API_KEY` und sendet die MP4-Datei an EvoLink. Prüfe vorher die Kosten. Gleiche die Zeitmarken für Bildereignisse mit den entnommenen Einzelbildern ab.

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 Inhalt


| Fall | Worauf du achten kannst |
| --- | --- |
| [Zahnpasta-Tabs von Evopaste](#case-1) | Aufhänger, Produktvorführung und Verpackung in drei Einstellungen |
| [Anprobe des E-bra mit Frontverschluss](#case-2) | Ein einzelnes Startbild hält das Kleidungsstück unter dem T-Shirt |
| [Sketch für Taqueritos-Chips](#case-4) (Entwurf) | Überblendung durch widersprüchliche Start- und Endbilder |
| [Vorführung des Parfums von Gloss Moderne](#case-5) (Entwurf) | Vier Produktzustände in einer Demo, die nur Hände zeigt |
| [Vlog „Gym Day“](#case-6) | Eine längere Bewegung ab dem letzten brauchbaren Bild fortsetzen |
| [Direkte Kameraansprache im Einteiler](#case-7) | Eine Sprechpause nutzen, um eine Abweichung beim Outfit herauszuschneiden |
| [Faltbares Solarladegerät](#n1) | Faltbares Solarmodul |
| [Rote Balsamdose](#n2) | Runde rote Balsamdose |
| [Shake von DAILYFORM](#n3) | Proteinpulver und Shaker |
| [Serum von VELORA](#n4) | Anwendung des Serums |
| [Auspacken der Sneaker von PACELO](#n5) | Sneaker auspacken |
| [Duft VELORA Rose 01](#n6) | Vorführung des Dufts |

## 🎬 Dokumentierte Fälle

<a id="case-1"></a>

### Fall 1: Zahnpasta-Tabs von Evopaste

| [Original abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="Original abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="Nachbau abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="Vergleich abspielen" width="210"></a> |

**Zeige das Problem mit einem visuellen Aufhänger und gib der Vorführung und der Verpackung je eine eigene Einstellung.**

Die Vorlage beginnt mit einer überzeichneten Darstellung gelber Zähne. Danach folgen die Anwendung und eine Nahaufnahme des Produkts. Der Nachbau behielt diese drei Teile bei und setzte eine andere Person sowie die kaubaren Zahnpasta-Tabs von Evopaste ein.

Drei Clips zeigten den Aufhänger, die Schaumbildung und die Verpackung. Als Vorlage für die Beschriftung diente das Verpackungsfoto. Im abschließenden Selfie musste ein Teil des Bildes horizontal gespiegelt werden, um die spiegelverkehrte Schrift zu korrigieren.

Der Export war 21,18 Sekunden lang. Das geplante Ausspucken in einen Becher fehlte. Beim abschließenden Lächeln blieb violetter Schaum auf den Lippen. Die drei Clips kosteten damals insgesamt 2,52 US-Dollar.

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### Fall 2: Anprobe des E-bra mit Frontverschluss

| [Original abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="Original abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="Nachbau abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="Vergleich abspielen" width="210"></a> |

**Wenn das Produkt verdeckt bleiben soll, zeige die Kleidungsschichten im Startbild und lass das widersprüchliche Produktfoto weg.**

Im Nachbau blieben die Vorführung des Frontverschlusses, die Anprobe und die Handgesten erhalten. Das neue Produktbild zeigte einen lavendelfarbenen gemusterten BH mit einem E-Zeichen.

Für die Einstellung mit dem Frontverschluss war eine Bewegungsvorlage nötig, nachdem frühere Versuche den Ablauf von Handbewegungen und Verschluss verfehlt hatten. Bei der letzten Geste ließ ein separates Produktfoto den BH über dem T-Shirt erscheinen. Die freigegebene Version entstand per Bild-zu-Video aus einem Startbild, auf dem das T-Shirt schon zu sehen war. Die Geste wurde per Text vorgegeben.

In der 17,50 Sekunden langen Endfassung blieben der Frontverschluss, das Zeichen am Rücken und der gemusterte Träger erhalten. Die dokumentierten Schnittpunkte lagen höchstens zwei Einzelbilder von denen der Vorlage entfernt. Das Raumgeräusch wurde von Einstellung zu Einstellung leiser. Einschließlich neuer Versuche lagen die damaligen Kosten bei rund 7,50 US-Dollar.

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### Fall 4: Sketch für Taqueritos-Chips

| [Original abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="Original abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="Nachbau abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="Vergleich abspielen" width="210"></a> |

**Prüfe vor dem Abschicken, ob die Kamerabewegung das Start- und Endbild verbinden kann.**

Die Kamera fährt von den Füßen bis zum Gesicht über ein Sofa voller Chipstüten. Es folgen ein Schnitt zur Reaktion und die Präsentation der Verpackung. Im Nachbau wurden die Darstellerin und die Snackverpackung ausgetauscht.

Im Start- und Endbild der Sofafahrt lagen die Beine und die durchsichtigen Tüten an unterschiedlichen Stellen. Das Modell löste den Widerspruch mit einer Überblendung. Als Korrektur wurde vorgeschlagen, beide Bilder aus einer einzigen Aufnahme mit weiterem Bildausschnitt abzuleiten und nur den Ausschnitt zu ändern.

Das ist der damalige Prompt für den ersten Clip des fehlgeschlagenen Versuchs.

Der 8,20 Sekunden lange Export ist ein Entwurf. In der ersten Einstellung ist zwischen etwa 2,15 und 2,60 Sekunden weiterhin eine Überblendung zu sehen. Die Korrektur steht als Vorschlag im Plan. Bis zum Entwurf waren rund 1,90 US-Dollar angefallen.

<details>
<summary>Ursprünglicher Prompt für den Clip</summary>

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

Status: Entwurf

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### Fall 5: Vorführung des Parfums von Gloss Moderne

| [Original abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="Original abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="Nachbau abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="Vergleich abspielen" width="210"></a> |

**Erstelle für jeden sichtbaren Produktzustand ein Startbild und beschreibe die Bewegung in überprüfbaren Abschnitten.**

Die Demo im geparkten Auto zeigt nur Hände und hat vier Abschnitte: einen Sprühstoß, den Flakon mit Kappe, die geöffnete Schachtel und eine Nahaufnahme der Verpackung. Der Nachbau verwendete die neue Parfumverpackung und für jeden Zustand ein eigenes Eingabebild.

Für die Sprühaufnahme waren zwei kurze Stöße mit klarer Pause nötig, in der die Düse in ihre Ausgangsposition zurückkehrt. Bei der Flakonaufnahme zeigte die Einzelbildprüfung eine sichtbare Drehung, die die Videoanalyse übersehen hatte. Die geplante Verschiebung des Flakons fehlte.

Das ist der damals verwendete Prompt für die Sprühaufnahme.

Der gelieferte Entwurf war 7,17 Sekunden lang und hielt die Schnittzeiten und beide Sprühstöße ein. Der Nebel verflog schnell. Einige kleine Schriftzüge wurden in der gelieferten Qualität unscharf. Einschließlich der Videoanalyse lagen die damaligen Kosten bei rund 2,43 US-Dollar.

<details>
<summary>Ursprünglicher Prompt für den Clip</summary>

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

Status: Entwurf

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### Fall 6: Vlog „Gym Day“

| [Original abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="Original abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="Nachbau abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="Vergleich abspielen" width="210"></a> |

**Setze eine anspruchsvolle Bewegung ab dem letzten brauchbaren Einzelbild fort, wenn eine lange Einstellung abweicht.**

Beim Austausch der Person blieb die Vlog-Sequenz aus Spiegel-Selfie, Küche, Tür und Training erhalten. Die Behälter in der Küche dienten als neutrale Requisiten.

Im ersten generierten Hip-Thrust-Clip machte die Person eine Wiederholung und setzte sich anschließend auf. Das Team nahm das Bild bei 3,0 Sekunden als Eingabe für die Fortsetzung, generierte die nächste Bewegungsphase und setzte den Schnitt in die kurze Haltephase in der unteren Position.

Das ist der damals verwendete Prompt für die Fortsetzung des Hip Thrusts.

Die Endfassung dauerte 20,08 Sekunden, die Vorlage 20,03 Sekunden. Die dokumentierten Schnittpunkte lagen höchstens 0,2 Sekunden auseinander. Der Nachbau behielt das in der Lautstärke angeglichene Raumgeräusch bei. Einschließlich Fortsetzung und Videoanalyse lagen die damaligen Kosten bei rund 5,16 US-Dollar.

<details>
<summary>Ursprünglicher Prompt für den Clip</summary>

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

### Fall 7: Direkte Kameraansprache im Einteiler

| [Original abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="Original abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="Nachbau abspielen" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="Vergleich abspielen" width="210"></a> |

**Lege die Ansichten des Kleidungsstücks vor der Generierung fest und prüfe den Dialog, bevor du Abweichungen herausschneidest.**

Die Vorlage beginnt mit einer Seitenansicht, die den Sitz des Kleidungsstücks zeigt. Danach folgen direkte Kameraansprache, Gesten am Kleidungsstück und eine Drehung. Der Nachbau setzte die vorgegebene Person und einen schlichten mokkafarbenen Einteiler nach der Zielbeschreibung ein.

Die zweite Generierung zeigte einen tieferen Rückenausschnitt als vorgesehen und fügte ein kleines Tattoo hinzu. Im gewählten Schnitt endet die Drehung in einer Sprechpause, bevor der Rücken sichtbar wird. Das Video setzt mit dem ersten brauchbaren Bild von vorn wieder ein.

Das ist der damals verwendete Prompt für den Einstieg in der Seitenansicht.

Das akzeptierte Tattoo ist in der 16,62 Sekunden langen zweiten Fassung weiterhin zu sehen. Beim Schnitt entfiel ein Teil einer gesprochenen Zeile. Der dritte Schnitt liegt rund 1,42 Sekunden früher als in der Vorlage. Die dokumentierten Produktionskosten lagen bei rund 3,02 US-Dollar. Für den finalen Schnitt wurde vorhandenes Material verwendet.

<details>
<summary>Ursprünglicher Prompt für den Clip</summary>

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

## 🧪 Weitere Nachbau-Tests

Zu jedem Test gibt es einen Nachbau und einen direkten Vergleich.

<a id="n1"></a>

### Faltbares Solarladegerät

| [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="Nachbau abspielen" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="Vergleich abspielen" width="240"></a> |

<a id="n2"></a>

### Rote Balsamdose

| [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="Nachbau abspielen" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="Vergleich abspielen" width="240"></a> |

<a id="n3"></a>

### Shake von DAILYFORM

| [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="Nachbau abspielen" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="Vergleich abspielen" width="240"></a> |

<a id="n4"></a>

### Serum von VELORA

| [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="Nachbau abspielen" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="Vergleich abspielen" width="240"></a> |

<a id="n5"></a>

### Auspacken der Sneaker von PACELO

| [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="Nachbau abspielen" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="Vergleich abspielen" width="240"></a> |

<a id="n6"></a>

### Duft VELORA Rose 01

| [Nachbau abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [Vergleich abspielen](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="Nachbau abspielen" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="Vergleich abspielen" width="240"></a> |

## 🔗 Verwandte Repositories

[EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin) für die Einrichtung des Clients und die Dokumentation der Werkzeuge.

## 🙏 Danksagung

Die Referenzanzeigen stammen von den jeweiligen Urheberinnen und Urhebern. Wenn bei einem Clip eine Quellenangabe, Korrektur oder Entfernung nötig ist, lege bitte ein Issue an und nenne den entsprechenden Fall.
