<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="Haz clic para recrear anuncios ganadores" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="Ver la demo de recreación de anuncios con Claude" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ Reproducir la demo completa de Claude con sonido</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">Reproducir el tráiler de Awesome Ads Clone</a></p>
</div>

## 🍌 Introducción

Recrea un anuncio de referencia para tu producto con EvoLink MCP. Conserva el gancho, la demostración del producto y el ritmo de montaje. Sustituye a la persona que aparece, el producto, el entorno y el guion por los tuyos.

## 📊 Resumen

Las doce recreaciones abarcan demostraciones de producto, pruebas de ropa, un sketch, un videoblog y un anuncio a cámara. Los seis casos documentados muestran el original, la recreación y una comparación lado a lado. Las seis pruebas adicionales incluyen su recreación y su comparación.

## ⚡ Inicio rápido

Conecta [EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) a tu agente. Proporciónale un anuncio de referencia, una imagen y una descripción del producto, y una imagen de la persona que saldrá en pantalla o una descripción del perfil que buscas. Después, pega este prompt.

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
<summary>Conectar desde Codex o Claude Code</summary>

Para Codex:

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

Para Claude Code:

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

Inicia sesión en EvoLink en el navegador cuando se te solicite. En Claude Code, usa `/mcp` → `evolink` → **Authenticate**. Si Codex solicita un inicio de sesión manual, ejecuta `codex mcp login evolink`.

Antes de la primera generación, pide a tu agente que compruebe el saldo de EvoLink y busque un modelo que genere vídeo a partir de una imagen inicial. El agente necesita acceder a archivos locales y disponer de FFmpeg/FFprobe para dividir y editar los clips. Puede hacerlo todo desde la misma conversación.

</details>

## 🛠️ Método en siete pasos

1. **Analiza la referencia.** Extrae fotogramas a 4 fps y revisa con más detalle los movimientos rápidos y los cortes dudosos. Anota el gancho inicial, la demostración del producto, los planos y cuándo se corta cada uno. Para el sonido, usa una transcripción que hayas aportado o las funciones de audio del agente.
2. **Define el resultado.** Especifica qué se sustituye en cada plano. Escribe comprobaciones que el agente pueda aplicar al vídeo, como «la tapa se mantiene puesta hasta que la mano la levanta a los 1,5 segundos». Verifica las afirmaciones sobre el producto antes de usarlas.
3. **Planifica los clips según los cortes.** Da a cada plano su propio fotograma inicial. Si un movimiento continuo resulta difícil, divídelo en una postura estable y comienza el siguiente clip en el último fotograma aprovechable. Deja margen para recortar cuando el modelo lo permita.
4. **Confirma los fotogramas iniciales.** Comprueba en una imagen fija quién aparece, su vestuario, el envase, el estado del producto, cómo se sujeta y el encuadre antes de gastar en vídeo. Muestra el estado exacto que necesitas, como una botella sin tapa.
5. **Revisa todos los elementos de entrada en conjunto.** Asigna una función a cada imagen o clip. Retira la foto del producto si contradice que este deba permanecer oculto y comprueba que el movimiento previsto pueda enlazar los fotogramas inicial y final. Pide a EvoLink MCP un presupuesto para la solicitud exacta antes de aprobarla.
6. **Genera un solo clip y revísalo.** Compara el primer fotograma, la acción principal y el estado final con el resultado previsto. Cambia el elemento de entrada que causó el fallo o divide el plano. Guarda el ID de la tarea y recupera el resultado existente antes de enviar otro trabajo de pago.
7. **Monta y revisa el anuncio.** Recorta los clips aprobados, añade los subtítulos y el audio autorizados y exporta el anuncio. Revisa el ritmo y la continuidad del vídeo completo. Si puedes usar la referencia para una comparación, entrega también esa comparación junto con la recreación.

<details>
<summary>Análisis opcional con Gemini para diálogo, sonido y acción</summary>

La API nativa de Gemini en EvoLink puede preparar un registro de los clips o una transcripción. Este paso opcional usa una `EVOLINK_API_KEY` independiente y envía el MP4 a EvoLink. Consulta el coste antes de ejecutarlo. Contrasta las marcas de tiempo visuales con los fotogramas extraídos.

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 Menú


| Caso | En qué fijarse |
| --- | --- |
| [Pastillas dentífricas Evopaste](#case-1) | Gancho, demostración del producto y presentación del envase en tres planos |
| [Prueba del sujetador E-bra con cierre delantero](#case-2) | Un solo fotograma inicial para mantener la prenda debajo de la camiseta |
| [Sketch de los aperitivos Taqueritos](#case-4) (borrador) | Un fundido por diferencias entre el fotograma inicial y el final |
| [Demostración del perfume Gloss Moderne](#case-5) (borrador) | Cuatro estados del producto en una demostración en la que solo se ven las manos |
| [Videoblog de un día de gimnasio](#case-6) | Continuar una acción larga desde el último fotograma aprovechable |
| [Presentación de un mono corto a cámara](#case-7) | Aprovechar una pausa en el diálogo para recortar un cambio en el vestuario |
| [Cargador solar plegable](#n1) | Panel solar plegable |
| [Lata roja de bálsamo](#n2) | Lata redonda roja de bálsamo |
| [Batido DAILYFORM](#n3) | Proteína en polvo y vaso mezclador |
| [Sérum VELORA](#n4) | Demostración del sérum |
| [Desempaquetado de zapatillas PACELO](#n5) | Desempaquetado de zapatillas |
| [Fragancia VELORA Rose 01](#n6) | Demostración de la fragancia |

## 🎬 Casos documentados

<a id="case-1"></a>

### Caso 1: Pastillas dentífricas Evopaste

| [Ver el original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="Ver el original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="Ver la recreación" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="Ver la comparación" width="210"></a> |

**Presenta el problema con un gancho visual y dedica sendos planos a la demostración y al envase.**

La referencia empieza con una imagen exagerada de dientes amarillos y pasa al uso del producto y a su presentación en primer plano. La recreación mantuvo esos tres momentos, sustituyó a la persona y mostró un envase de pastillas dentífricas masticables Evopaste.

Tres clips separaron el gancho, la demostración con espuma y el plano del envase. Las etiquetas procedían de la imagen del envase. En la toma final tipo selfi hubo que voltear esa zona horizontalmente para corregir el texto reflejado.

El vídeo exportado duró 21,18 segundos. La demostración omitió el momento previsto de escupir en un vaso y dejó espuma morada en los labios durante la sonrisa final. El gasto registrado en vídeo fue de 2,52 USD por los tres clips.

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### Caso 2: Prueba del sujetador E-bra con cierre delantero

| [Ver el original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="Ver el original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="Ver la recreación" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="Ver la comparación" width="210"></a> |

**Cuando el producto deba quedar oculto, fija la capa de ropa en el fotograma inicial y retira la imagen de producto que entra en conflicto.**

La recreación conservó la demostración del cierre delantero, la prueba de la prenda y los planos con gestos de las manos. La imagen de producto de reemplazo mostraba un sujetador estampado de color lavanda con una marca en forma de E.

El plano del cierre delantero necesitó una referencia de movimiento porque las tomas anteriores no respetaban la secuencia de manos y cierre. Para el gesto final, una imagen independiente del producto hizo que el sujetador apareciera por encima de la camiseta. La toma aceptada generó vídeo a partir de un fotograma inicial que ya mostraba la camiseta y una instrucción de texto para el gesto.

La versión final de 17,50 segundos conservó el cierre delantero, la marca de la espalda y el tirante estampado. Los puntos de corte registrados quedaron a un máximo de dos fotogramas de la referencia. El sonido ambiente fue bajando de un plano a otro. El proyecto costó unos 7,50 USD, incluidos los reintentos.

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### Caso 4: Sketch de los aperitivos Taqueritos

| [Ver el original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="Ver el original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="Ver la recreación" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="Ver la comparación" width="210"></a> |

**Antes de enviar la solicitud, comprueba que el movimiento de cámara pueda enlazar los fotogramas inicial y final.**

En el sketch, la cámara recorría de los pies a la cara un sofá cubierto de bolsas de aperitivos. Después cortaba a una reacción y a la presentación del envase. En la recreación se sustituyeron la persona y el envase de los aperitivos.

En los fotogramas inicial y final del recorrido por el sofá, las piernas y las bolsas transparentes estaban en posiciones distintas. El modelo unió ambas imágenes con un fundido. La solución propuesta era sacar los dos fotogramas de una sola imagen más amplia, variando únicamente el encuadre.

Este es el prompt que se usó para el primer clip de la toma fallida descrita arriba.

La exportación de 8,20 segundos es un borrador. El primer plano todavía presenta un fundido entre aproximadamente los 2,15 y 2,60 segundos. La corrección figura en el plan como propuesta. Hasta el borrador se registró un gasto de unos 1,90 USD.

<details>
<summary>Prompt original del clip</summary>

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

Estado: borrador

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### Caso 5: Demostración del perfume Gloss Moderne

| [Ver el original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="Ver el original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="Ver la recreación" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="Ver la comparación" width="210"></a> |

**Prepara un fotograma inicial para cada estado físico del producto y describe la acción mediante momentos que puedan verse.**

La demostración en un coche aparcado muestra únicamente las manos y sigue cuatro momentos: pulverización, frasco tapado, caja abierta y primer plano del envase. La recreación usó el envase del perfume de reemplazo y fotogramas de entrada distintos para cada estado.

El clip de pulverización requería dos rociadas breves, con una pausa clara para que el pulsador volviera a su posición. Al revisar los fotogramas del clip del frasco se encontró una rotación visible que el analizador de vídeo había pasado por alto. El desplazamiento previsto no se produjo.

Este es el prompt que se usó en el clip de pulverización.

El borrador entregado, de 7,17 segundos, mantuvo los tiempos de corte y las dos rociadas. La niebla se disipó rápido y parte del texto pequeño perdió nitidez en el vídeo entregado. El gasto registrado, incluido el análisis de vídeo, fue de unos 2,43 USD.

<details>
<summary>Prompt original del clip</summary>

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

Estado: borrador

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### Caso 6: Videoblog de un día de gimnasio

| [Ver el original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="Ver el original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="Ver la recreación" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="Ver la comparación" width="210"></a> |

**Si una toma larga se desvía en una acción física exigente, continúa desde el último fotograma aprovechable.**

El cambio de la persona en pantalla conservó la secuencia del videoblog: selfi ante un espejo, cocina, puerta y ejercicio. Los recipientes de la cocina siguieron siendo elementos de atrezo genéricos.

La primera generación de la elevación de cadera hizo una repetición y después la persona terminó sentada. El equipo usó el fotograma de los 3,0 segundos como punto de partida para generar la continuación y empalmó los clips durante la pausa en la posición baja.

Este es el prompt que se usó para continuar la elevación de cadera.

La versión final duró 20,08 segundos, frente a 20,03 de la referencia. Los cortes registrados quedaron a un máximo de 0,2 segundos de los originales. La recreación conservó el sonido ambiente normalizado. El gasto registrado, incluidas la continuación y la lectura de vídeo, fue de unos 5,16 USD.

<details>
<summary>Prompt original del clip</summary>

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

### Caso 7: Presentación de un mono corto a cámara

| [Ver el original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="Ver el original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="Ver la recreación" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="Ver la comparación" width="210"></a> |

**Fija las vistas de la prenda antes de generar y revisa el diálogo antes de recortar para ocultar un cambio no deseado.**

La referencia combinaba un gancho de perfil para mostrar cómo quedaba la prenda, una intervención a cámara, gestos sobre la ropa y un giro. La recreación usó a la persona proporcionada y un mono corto liso de color moca, creado a partir de la descripción del resultado.

La segunda generación dejó la espalda más escotada de lo previsto y añadió un tatuaje pequeño. En el montaje elegido se interrumpió el giro durante una pausa del diálogo, justo antes de que apareciera la espalda, y se retomó en el primer fotograma frontal aprovechable.

Este es el prompt que se usó para la apertura de perfil.

La segunda versión, de 16,62 segundos, conserva el tatuaje que se decidió aceptar. El montaje eliminó parte de una frase hablada y adelantó el tercer corte unos 1,42 segundos respecto de la referencia. El gasto de producción registrado fue de unos 3,02 USD. El montaje final usó material ya generado.

<details>
<summary>Prompt original del clip</summary>

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

## 🧪 Pruebas adicionales de recreación

Cada prueba incluye una recreación y una comparación lado a lado.

<a id="n1"></a>

### Cargador solar plegable

| [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="Ver la recreación" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="Ver la comparación" width="240"></a> |

<a id="n2"></a>

### Lata roja de bálsamo

| [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="Ver la recreación" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="Ver la comparación" width="240"></a> |

<a id="n3"></a>

### Batido DAILYFORM

| [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="Ver la recreación" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="Ver la comparación" width="240"></a> |

<a id="n4"></a>

### Sérum VELORA

| [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="Ver la recreación" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="Ver la comparación" width="240"></a> |

<a id="n5"></a>

### Desempaquetado de zapatillas PACELO

| [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="Ver la recreación" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="Ver la comparación" width="240"></a> |

<a id="n6"></a>

### Fragancia VELORA Rose 01

| [Ver la recreación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [Ver la comparación](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="Ver la recreación" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="Ver la comparación" width="240"></a> |

## 🔗 Repositorios relacionados

Consulta [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin) para configurar el cliente y ver la documentación de las herramientas.

## 🙏 Créditos

Los anuncios de referencia pertenecen a sus respectivos creadores. Si un clip necesita una atribución, corrección o retirada, abre una incidencia e indica el nombre del caso.
