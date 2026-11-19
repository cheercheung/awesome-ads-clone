<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="Clique para recriar anúncios vencedores" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="Assista à demonstração de recriação de anúncios com Claude" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ Reproduzir a demonstração completa do Claude com som</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">Reproduzir o trailer de Awesome Ads Clone</a></p>
</div>

## 🍌 Introdução

Recrie um anúncio de referência para seu próprio produto com o EvoLink MCP. Mantenha o gancho, a demonstração do produto e o ritmo da edição. Troque a pessoa em cena, o produto, o cenário e o roteiro pelos seus.

## 📊 Visão geral

As doze recriações incluem demonstrações de produtos, provas de roupas, um esquete, um vlog e um anúncio com apresentação para a câmera. Os seis casos documentados mostram o original, a recriação e uma comparação lado a lado. Os seis testes adicionais trazem suas respectivas recriações e comparações.

## ⚡ Início rápido

Conecte [EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) ao seu agente. Envie um anúncio de referência, uma imagem e uma descrição do produto, além de uma foto da pessoa que aparecerá em cena ou de um perfil para seleção de elenco. Depois, cole este prompt.

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
<summary>Conectar pelo Codex ou pelo Claude Code</summary>

No Codex:

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

No Claude Code:

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

Entre na sua conta do EvoLink no navegador quando solicitado. No Claude Code, use `/mcp` → `evolink` → **Authenticate**. Se o Codex solicitar login manual, execute `codex mcp login evolink`.

Antes da primeira geração, peça ao agente para verificar o saldo no EvoLink e encontrar um modelo que gere vídeo a partir de um quadro inicial. O agente precisa de acesso aos arquivos locais e de FFmpeg/FFprobe para dividir e editar os clipes. Ele pode fazer tudo na mesma conversa.

</details>

## 🛠️ Método em sete etapas

1. **Analise a referência.** Extraia quadros a 4 fps e examine com mais atenção os movimentos rápidos e os cortes duvidosos. Anote o gancho de abertura, a demonstração do produto, os planos e o momento de cada corte. Para o som, use uma transcrição fornecida ou os recursos de áudio do agente.
2. **Defina o resultado desejado.** Especifique o que trocar em cada plano. Escreva critérios que o agente possa conferir no vídeo, como “a tampa permanece no lugar até a mão levantá-la aos 1,5 segundos”. Confirme as alegações sobre o produto antes de usá-las.
3. **Planeje os clipes a partir dos cortes.** Dê a cada plano seu próprio quadro inicial. Se um movimento contínuo for difícil, divida-o em uma posição estável. Inicie o próximo clipe no último quadro aproveitável. Deixe uma margem para aparar quando o modelo permitir.
4. **Confirme os quadros iniciais.** Confira em uma imagem estática a pessoa em cena, o figurino, a embalagem, o estado do produto, a pegada e o enquadramento antes de gastar com vídeo. Mostre o estado exato que você precisa, como um frasco sem tampa.
5. **Confira os materiais de entrada em conjunto.** Dê uma função a cada imagem ou clipe. Retire a foto do produto se ela contrariar a intenção de mantê-lo escondido e confirme que o movimento planejado consegue ligar os quadros inicial e final. Peça ao EvoLink MCP um orçamento para a solicitação exata antes de aprová-la.
6. **Gere um clipe e revise-o.** Compare o primeiro quadro, a ação principal e o estado final com o resultado desejado. Troque o material de entrada que provocou o erro ou divida o plano. Salve o ID da tarefa e recupere o resultado existente antes de enviar outro trabalho pago.
7. **Monte e revise o anúncio.** Apare os clipes aprovados, adicione as legendas e o áudio autorizados e exporte o anúncio. Revise o ritmo e a continuidade do vídeo inteiro. Se puder usar a referência em uma comparação, entregue as duas versões lado a lado junto com a recriação.

<details>
<summary>Análise opcional com Gemini para diálogo, som e ação</summary>

A API nativa do Gemini no EvoLink pode rascunhar um registro dos clipes ou uma transcrição. Essa etapa opcional usa uma `EVOLINK_API_KEY` separada e envia o MP4 ao EvoLink. Consulte o custo antes de executá-la. Cruze as marcações de tempo da imagem com os quadros extraídos.

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 Menu


| Caso | O que observar |
| --- | --- |
| [Pastilhas de creme dental Evopaste](#case-1) | Gancho, demonstração do produto e apresentação da embalagem em três planos |
| [Prova do sutiã E-bra com fecho frontal](#case-2) | Um único quadro inicial mantém a peça por baixo da camiseta |
| [Esquete dos salgadinhos Taqueritos](#case-4) (rascunho) | Uma fusão entre imagens causada por quadros inicial e final incompatíveis |
| [Demonstração do perfume Gloss Moderne](#case-5) (rascunho) | Quatro estados do produto em uma demonstração que mostra apenas as mãos |
| [Vlog de um dia na academia](#case-6) | Continuação de uma ação longa a partir do último quadro aproveitável |
| [Apresentação de um macaquinho para a câmera](#case-7) | Aproveitar uma pausa na fala para cortar uma mudança de figurino |
| [Carregador solar dobrável](#n1) | Painel solar dobrável |
| [Lata vermelha de bálsamo](#n2) | Lata redonda e vermelha de bálsamo |
| [Shake DAILYFORM](#n3) | Proteína em pó e coqueteleira |
| [Sérum VELORA](#n4) | Demonstração do sérum |
| [Abertura da caixa do tênis PACELO](#n5) | Abertura da caixa do tênis |
| [Fragrância VELORA Rose 01](#n6) | Demonstração da fragrância |

## 🎬 Casos documentados

<a id="case-1"></a>

### Caso 1: Pastilhas de creme dental Evopaste

| [Ver o original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="Ver o original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="Ver a recriação" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="Ver a comparação" width="210"></a> |

**Apresente o problema com um gancho visual e dê um plano próprio à demonstração e à embalagem.**

A referência abre com uma imagem exagerada de dentes amarelos e passa para o uso e a apresentação do produto em close. A recriação manteve esses três momentos, trocou a pessoa em cena e mostrou a embalagem de pastilhas de creme dental mastigáveis Evopaste.

Três clipes separaram o gancho, a demonstração com espuma e o plano da embalagem. Os rótulos foram vinculados à imagem da embalagem. Na selfie final, foi preciso espelhar horizontalmente uma região para corrigir o texto invertido.

A exportação durou 21,18 segundos. A demonstração deixou de fora o momento planejado de cuspir no copo e manteve espuma roxa nos lábios durante o sorriso final. O custo registrado de vídeo foi de US$ 2,52 pelos três clipes.

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### Caso 2: Prova do sutiã E-bra com fecho frontal

| [Ver o original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="Ver o original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="Ver a recriação" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="Ver a comparação" width="210"></a> |

**Quando o produto precisar ficar escondido, mostre as camadas da roupa no quadro inicial e descarte a foto do produto que entra em conflito.**

A recriação manteve a demonstração do fecho frontal, a prova da peça e os planos com gestos das mãos. A imagem de produto de reposição mostrava um sutiã estampado na cor lavanda com uma marca em forma de E.

O plano do fecho frontal precisou de uma referência de movimento porque as tentativas anteriores erraram a sequência das mãos e do fecho. No gesto final, uma imagem separada do produto fez o sutiã aparecer por cima da camiseta. A tomada aprovada gerou vídeo a partir de um quadro inicial que já mostrava a camiseta, com uma instrução em texto para o gesto.

A versão final de 17,50 segundos manteve o fecho frontal, a marca nas costas e a alça estampada. Os cortes registrados ficaram a no máximo dois quadros dos da referência. O som ambiente ficou mais baixo de um plano a outro. O projeto custou cerca de US$ 7,50, incluindo as novas tentativas.

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### Caso 4: Esquete dos salgadinhos Taqueritos

| [Ver o original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="Ver o original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="Ver a recriação" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="Ver a comparação" width="210"></a> |

**Antes de enviar a solicitação, confira se o movimento da câmera consegue ligar os quadros inicial e final.**

No esquete, a câmera percorria dos pés ao rosto uma pessoa em um sofá coberto de sacos de salgadinho. Depois, cortava para uma reação e para a apresentação da embalagem. A recriação trocou a pessoa em cena e a embalagem do salgadinho.

Os quadros inicial e final do movimento sobre o sofá mostravam as pernas e os sacos transparentes em posições diferentes. O modelo juntou as imagens com uma fusão. A correção proposta era extrair os dois quadros de uma única imagem mais aberta, mudando apenas o enquadramento.

Este é o prompt usado para o primeiro clipe da tomada malsucedida descrita acima.

A exportação de 8,20 segundos é um rascunho. O primeiro plano ainda apresenta uma fusão entre aproximadamente 2,15 e 2,60 segundos. O plano registra a correção como proposta. O gasto registrado até o rascunho foi de cerca de US$ 1,90.

<details>
<summary>Prompt original do clipe</summary>

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

Status: rascunho

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### Caso 5: Demonstração do perfume Gloss Moderne

| [Ver o original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="Ver o original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="Ver a recriação" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="Ver a comparação" width="210"></a> |

**Prepare um quadro inicial para cada estado físico do produto e descreva a ação em momentos que possam ser observados.**

A demonstração dentro de um carro estacionado mostra apenas as mãos e passa por quatro momentos: borrifada, frasco tampado, caixa aberta e close da embalagem. A recriação usou a embalagem do perfume de reposição e quadros de entrada separados para cada estado.

O clipe da borrifada exigia dois jatos curtos com uma pausa clara e o retorno do bico à posição inicial. Na revisão dos quadros do frasco, viu-se uma rotação que a análise de vídeo não havia detectado. O deslocamento previsto não aconteceu.

Este é o prompt usado no clipe da borrifada.

O rascunho entregue, de 7,17 segundos, conservou os tempos de corte e as duas borrifadas. A névoa desapareceu rápido e parte das letras pequenas ficou pouco nítida na versão entregue. O gasto registrado, incluindo a análise do vídeo, foi de cerca de US$ 2,43.

<details>
<summary>Prompt original do clipe</summary>

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

Status: rascunho

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### Caso 6: Vlog de um dia na academia

| [Ver o original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="Ver o original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="Ver a recriação" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="Ver a comparação" width="210"></a> |

**Se uma tomada longa se desviar em uma ação física difícil, continue a partir do último quadro aproveitável.**

A troca da pessoa em cena preservou a sequência do vlog: selfie no espelho, cozinha, porta e exercício. Os recipientes da cozinha continuaram sendo objetos genéricos de cena.

A primeira geração da elevação de quadril mostrou uma repetição e depois saiu do movimento, com a pessoa se sentando. A equipe partiu do quadro aos 3,0 segundos para gerar a continuação e uniu os clipes durante a pausa na posição baixa.

Este é o prompt usado para continuar a elevação de quadril.

A versão final durou 20,08 segundos, ante 20,03 da referência. Os cortes registrados ficaram a no máximo 0,2 segundo dos originais. A recriação manteve o som ambiente normalizado. O gasto registrado, incluindo a continuação e a análise de vídeo, foi de cerca de US$ 5,16.

<details>
<summary>Prompt original do clipe</summary>

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

### Caso 7: Apresentação de um macaquinho para a câmera

| [Ver o original](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="Ver o original" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="Ver a recriação" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="Ver a comparação" width="210"></a> |

**Fixe como a roupa deve aparecer de cada ângulo antes de gerar e confira a fala antes de escolher um corte que esconda uma alteração indesejada.**

A referência combinava um gancho de perfil para mostrar o caimento, uma apresentação para a câmera, gestos mostrando a roupa e um giro. A recriação usou a pessoa fornecida e um macaquinho liso cor de moca, criado a partir da descrição do resultado desejado.

A segunda geração fez um decote nas costas mais baixo do que o especificado e acrescentou uma pequena tatuagem. A edição escolhida interrompeu o giro em uma pausa da fala, antes de mostrar as costas, e retomou no primeiro quadro frontal aproveitável.

Este é o prompt usado para a abertura de perfil.

A segunda versão, de 16,62 segundos, ainda tem a tatuagem que foi aceita. A edição retirou parte de uma fala e adiantou o terceiro corte em cerca de 1,42 segundo em relação à referência. O gasto de produção registrado foi de cerca de US$ 3,02. A edição final usou material já gerado.

<details>
<summary>Prompt original do clipe</summary>

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

## 🧪 Testes adicionais de recriação

Cada teste inclui uma recriação e uma comparação lado a lado.

<a id="n1"></a>

### Carregador solar dobrável

| [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="Ver a recriação" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="Ver a comparação" width="240"></a> |

<a id="n2"></a>

### Lata vermelha de bálsamo

| [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="Ver a recriação" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="Ver a comparação" width="240"></a> |

<a id="n3"></a>

### Shake DAILYFORM

| [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="Ver a recriação" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="Ver a comparação" width="240"></a> |

<a id="n4"></a>

### Sérum VELORA

| [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="Ver a recriação" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="Ver a comparação" width="240"></a> |

<a id="n5"></a>

### Abertura da caixa do tênis PACELO

| [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="Ver a recriação" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="Ver a comparação" width="240"></a> |

<a id="n6"></a>

### Fragrância VELORA Rose 01

| [Ver a recriação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [Ver a comparação](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="Ver a recriação" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="Ver a comparação" width="240"></a> |

## 🔗 Repositórios relacionados

Consulte [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin) para configurar o cliente e ver a documentação das ferramentas.

## 🙏 Créditos

Os anúncios de referência pertencem aos seus respectivos criadores. Se um clipe precisar de crédito, correção ou remoção, abra uma issue com o nome do caso.
