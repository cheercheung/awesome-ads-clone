<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="Cliquez pour recréer des pubs qui marchent" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="Voir la démonstration de recréation publicitaire avec Claude" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ Lire la démonstration Claude complète avec le son</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">Lire la bande-annonce d’Awesome Ads Clone</a></p>
</div>

## 🍌 Introduction

Recréez une publicité de référence pour votre propre produit avec EvoLink MCP. Gardez l’accroche, la démonstration du produit et le rythme du montage. Remplacez la personne à l’écran, le produit, le décor et le script par les vôtres.

## 📊 Vue d’ensemble

Les douze recréations couvrent des démonstrations de produits, des essayages, un sketch, un vlog et une publicité face caméra. Les six cas documentés présentent chacun l’original, la recréation et une comparaison côte à côte. Les six essais supplémentaires incluent chacun la recréation et la comparaison correspondante.

## ⚡ Démarrage rapide

Connectez [EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) à votre agent. Donnez-lui une publicité de référence, une image et une description du produit, ainsi qu’une photo de la personne à l’écran ou un profil de casting. Collez ensuite ce prompt.

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
<summary>Connexion depuis Codex ou Claude Code</summary>

Dans Codex :

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

Dans Claude Code :

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

Connectez-vous à EvoLink dans le navigateur lorsque l’outil vous le demande. Dans Claude Code, suivez `/mcp` → `evolink` → **Authenticate**. Si Codex demande une connexion manuelle, lancez `codex mcp login evolink`.

Avant la première génération, demandez à votre agent de vérifier le solde EvoLink et de chercher un modèle qui génère une vidéo à partir d’une image de départ. L’agent doit pouvoir accéder aux fichiers locaux et utiliser FFmpeg/FFprobe pour découper et monter les extraits. Il peut faire tout cela dans la même conversation.

</details>

## 🛠️ Méthode en sept étapes

1. **Analysez la référence.** Prélevez des images à 4 images par seconde et examinez de plus près les mouvements rapides et les coupes difficiles à situer. Notez l’accroche, la démonstration du produit, les plans et le moment de chaque coupe. Pour le son, utilisez une transcription fournie ou les capacités audio de l’agent.
2. **Décrivez le résultat visé.** Précisez ce qu’il faut remplacer dans chaque plan. Rédigez des critères que l’agent peut contrôler dans la vidéo, par exemple « Le bouchon reste en place jusqu’à ce que la main le soulève à 1,5 seconde. » Vérifiez les allégations sur le produit avant de les utiliser.
3. **Prévoyez les clips en suivant les coupes.** Donnez à chaque plan sa propre image de départ. Scindez un mouvement continu difficile au moment où la pose se stabilise. Commencez le clip suivant sur la dernière image exploitable. Prévoyez une marge de montage si le modèle le permet.
4. **Validez les images de départ.** Avant d’engager des frais de génération vidéo, contrôlez sur une image fixe la personne à l’écran, les vêtements, l’emballage, l’état du produit, la prise en main et le cadrage. Montrez l’état exact dont vous avez besoin, par exemple un flacon sans son bouchon.
5. **Vérifiez ensemble les éléments fournis au modèle.** Attribuez un rôle à chaque image ou clip. Retirez la photo du produit si elle contredit le fait que celui-ci doit rester caché. Vérifiez que le mouvement prévu peut relier les images de début et de fin. Demandez à EvoLink MCP un devis pour la requête exacte avant de l’approuver.
6. **Générez un clip et vérifiez-le.** Comparez la première image, l’action principale et l’état final au résultat visé. Modifiez l’élément d’entrée qui a causé l’écart, ou scindez le plan. Enregistrez l’identifiant de la tâche et récupérez son résultat avant de lancer un autre travail payant.
7. **Montez et vérifiez la vidéo.** Raccourcissez les clips validés, ajoutez les sous-titres et le son approuvés, puis exportez la publicité. Vérifiez le rythme et la continuité de l’ensemble. Si vous pouvez utiliser la référence pour une comparaison, livrez aussi cette comparaison avec la recréation.

<details>
<summary>Analyse Gemini facultative des dialogues, du son et des actions</summary>

L’API native Gemini d’EvoLink peut préparer une description des clips ou une transcription. Cette étape facultative utilise une clé `EVOLINK_API_KEY` distincte et transmet le MP4 à EvoLink. Vérifiez le coût avant de la lancer. Comparez les repères temporels des éléments visuels aux images prélevées.

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 Sommaire


| Cas | Points à observer |
| --- | --- |
| [Pastilles de dentifrice Evopaste](#case-1) | Accroche, démonstration du produit et révélation de l’emballage en trois plans |
| [Essayage du soutien-gorge E-bra à fermeture frontale](#case-2) | Une seule image de départ pour garder le vêtement sous le tee-shirt |
| [Sketch des chips Taqueritos](#case-4) (brouillon) | Un fondu causé par des images de début et de fin incompatibles |
| [Démonstration du parfum Gloss Moderne](#case-5) (brouillon) | Quatre états du produit dans une démonstration où seules les mains apparaissent |
| [Vlog d’une journée à la salle de sport](#case-6) | Prolonger une action longue à partir de la dernière image exploitable |
| [Présentation face caméra d’un combishort](#case-7) | Profiter d’une pause dans le dialogue pour couper un changement de tenue |
| [Chargeur solaire pliable](#n1) | Panneau solaire pliable |
| [Boîte rouge de baume](#n2) | Boîte ronde et rouge de baume |
| [Shake DAILYFORM](#n3) | Protéines en poudre et shaker |
| [Sérum VELORA](#n4) | Démonstration du sérum |
| [Déballage de baskets PACELO](#n5) | Déballage de baskets |
| [Parfum VELORA Rose 01](#n6) | Démonstration du parfum |

## 🎬 Cas documentés

<a id="case-1"></a>

### Cas 1: Pastilles de dentifrice Evopaste

| [Voir l’original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="Voir l’original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="Voir la recréation" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="Voir la comparaison" width="210"></a> |

**Introduisez le problème avec une accroche visuelle, puis consacrez un plan à la démonstration et un autre à l’emballage.**

La référence commence par une image exagérée de dents jaunes, montre l’utilisation du produit, puis le révèle en gros plan. La recréation a gardé ces trois temps forts, changé la personne à l’écran et montré un emballage de pastilles de dentifrice à mâcher Evopaste.

Trois clips distincts présentent l’accroche, la démonstration avec la mousse et l’emballage. Les étiquettes reprenaient celles de l’image du produit. Dans le selfie final, une partie de l’image a dû être retournée horizontalement pour corriger le texte en miroir.

L’export dure 21,18 secondes. La démonstration a omis le moment prévu où la personne devait cracher dans un verre, et de la mousse violette reste sur ses lèvres lorsqu’elle sourit à la fin. La génération des trois clips a coûté 2,52 USD lors de ce projet.

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### Cas 2: Essayage du soutien-gorge E-bra à fermeture frontale

| [Voir l’original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="Voir l’original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="Voir la recréation" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="Voir la comparaison" width="210"></a> |

**Lorsque le produit doit rester caché, montrez les couches de vêtements dès la première image et écartez la photo du produit qui contredit cette disposition.**

La recréation a conservé la démonstration de la fermeture frontale, l’essayage et les plans avec des gestes des mains. La photo du produit de remplacement montrait un soutien-gorge lavande à motifs avec une marque en forme de E.

Le plan de la fermeture frontale a nécessité une référence de mouvement après plusieurs prises qui ne respectaient pas l’enchaînement des mains et de la fermeture. Pour le geste final, la photo séparée du produit faisait apparaître le soutien-gorge par-dessus le tee-shirt. La prise retenue a été générée à partir d’une image montrant déjà le tee-shirt et d’une consigne écrite pour le geste.

La version finale de 17,50 secondes a conservé la fermeture frontale, la marque au dos et la bretelle à motifs. Les coupes relevées se trouvent à deux images au plus de celles de la référence. Le niveau sonore ambiant baissait d’un plan à l’autre. Le projet a coûté environ 7,50 USD, nouvelles tentatives comprises.

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### Cas 4: Sketch des chips Taqueritos

| [Voir l’original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="Voir l’original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="Voir la recréation" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="Voir la comparaison" width="210"></a> |

**Avant de lancer la génération, vérifiez que le mouvement de caméra peut relier les images de début et de fin.**

Dans le sketch, la caméra remonte des pieds au visage d’une personne allongée sur un canapé couvert de sachets de chips. Une coupe montre ensuite sa réaction puis l’emballage. La recréation a changé la personne à l’écran et l’emballage du produit.

Entre la première et la dernière image du mouvement sur le canapé, les jambes et les sachets transparents ne se trouvent pas au même endroit. Le modèle a relié les images par un fondu enchaîné. La correction proposée consistait à partir d’une seule image plus large et à ne changer que le cadrage pour obtenir les deux images.

Voici le prompt utilisé pour le premier clip de la prise ratée décrite ci-dessus.

L’export de 8,20 secondes est un brouillon. Le premier plan présente toujours un fondu vers 2,15 à 2,60 secondes. La correction figure dans le plan à titre de proposition. Les dépenses enregistrées jusqu’au brouillon s’élèvent à environ 1,90 USD.

<details>
<summary>Prompt original du clip</summary>

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

Statut : brouillon

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### Cas 5: Démonstration du parfum Gloss Moderne

| [Voir l’original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="Voir l’original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="Voir la recréation" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="Voir la comparaison" width="210"></a> |

**Préparez une image de départ pour chaque état physique du produit et découpez l’action en temps que l’on peut observer.**

La démonstration se déroule dans une voiture à l’arrêt, ne montre que les mains et s’articule en quatre temps : vaporisation, flacon fermé, boîte ouverte et gros plan de l’emballage. La recréation a utilisé l’emballage du parfum de remplacement et des images distinctes pour chaque état.

Le clip de vaporisation demandait deux jets courts séparés par une pause nette, avec retour du pulvérisateur en position initiale. Dans le clip du flacon, l’examen image par image a révélé une rotation que l’analyse vidéo n’avait pas détectée. Le déplacement prévu n’a pas eu lieu.

Voici le prompt utilisé pour le clip de vaporisation.

Le brouillon livré dure 7,17 secondes et conserve le moment des coupes ainsi que les deux vaporisations. La brume se dissipe vite et certains petits caractères manquent de netteté dans la vidéo livrée. Les dépenses enregistrées, analyse vidéo comprise, s’élèvent à environ 2,43 USD.

<details>
<summary>Prompt original du clip</summary>

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

Statut : brouillon

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### Cas 6: Vlog d’une journée à la salle de sport

| [Voir l’original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="Voir l’original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="Voir la recréation" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="Voir la comparaison" width="210"></a> |

**Si une prise longue s’écarte du mouvement attendu, reprenez cette action physique à partir de la dernière image exploitable.**

Seule la personne à l’écran a changé. Le vlog conserve son enchaînement : selfie dans un miroir, cuisine, porte et exercice. Les récipients dans la cuisine sont restés de simples accessoires.

Dans la première génération de la poussée de hanches, la personne a effectué une répétition avant de s’asseoir. L’équipe est repartie de l’image à 3,0 secondes pour générer la suite et a raccordé les clips lors de l’arrêt en position basse.

Voici le prompt utilisé pour prolonger la poussée de hanches.

La version finale dure 20,08 secondes contre 20,03 pour la référence. Les coupes relevées sont à 0,2 seconde au plus des originales. La recréation a conservé le son ambiant normalisé. Les dépenses enregistrées, prolongement et analyse vidéo compris, s’élèvent à environ 5,16 USD.

<details>
<summary>Prompt original du clip</summary>

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

### Cas 7: Présentation face caméra d’un combishort

| [Voir l’original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="Voir l’original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="Voir la recréation" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="Voir la comparaison" width="210"></a> |

**Fixez l’apparence du vêtement sous chaque angle avant de lancer la génération et vérifiez le dialogue avant de choisir une coupe pour masquer un écart.**

La référence combinait une accroche de profil pour montrer la coupe du vêtement, une prise de parole face caméra, des gestes montrant le vêtement et un tour sur soi. La recréation a utilisé la personne fournie et un combishort uni couleur moka, réalisé d’après la description du résultat attendu.

La deuxième génération a donné au vêtement un décolleté dans le dos plus bas que prévu et a ajouté un petit tatouage. Le montage retenu interrompt le tour pendant une pause du dialogue, avant de montrer le dos, puis reprend à la première image de face exploitable.

Voici le prompt utilisé pour l’ouverture de profil.

La deuxième version, de 16,62 secondes, contient toujours le tatouage que l’équipe a accepté. Le montage a supprimé une partie d’une réplique et avancé la troisième coupe d’environ 1,42 seconde par rapport à la référence. Les dépenses de production enregistrées s’élèvent à environ 3,02 USD. Le montage final a réutilisé les images déjà générées.

<details>
<summary>Prompt original du clip</summary>

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

## 🧪 Essais supplémentaires de recréation

Chaque essai comprend une recréation et une comparaison côte à côte.

<a id="n1"></a>

### Chargeur solaire pliable

| [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="Voir la recréation" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="Voir la comparaison" width="240"></a> |

<a id="n2"></a>

### Boîte rouge de baume

| [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="Voir la recréation" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="Voir la comparaison" width="240"></a> |

<a id="n3"></a>

### Shake DAILYFORM

| [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="Voir la recréation" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="Voir la comparaison" width="240"></a> |

<a id="n4"></a>

### Sérum VELORA

| [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="Voir la recréation" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="Voir la comparaison" width="240"></a> |

<a id="n5"></a>

### Déballage de baskets PACELO

| [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="Voir la recréation" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="Voir la comparaison" width="240"></a> |

<a id="n6"></a>

### Parfum VELORA Rose 01

| [Voir la recréation](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [Voir la comparaison](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="Voir la recréation" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="Voir la comparaison" width="240"></a> |

## 🔗 Dépôts associés

Consultez [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin) pour configurer votre client et accéder à la documentation des outils.

## 🙏 Crédits

Les publicités de référence appartiennent à leurs créateurs respectifs. Si un clip nécessite une attribution, une correction ou un retrait, ouvrez un ticket en indiquant le nom du cas.
