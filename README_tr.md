<div align="center">
  <a href="https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/banner-f4c2faacd4ba6d8b.jpg" alt="Başarılı reklamları klonlamak için tıkla" width="760"></a>
</div>

<h1 align="center">Awesome Ads Clone</h1>

<!-- language-picker -->
<div align="center">

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>
<!-- /language-picker -->

<div align="center">
  <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-preview-adadfdc5dff4f2e1.gif" alt="Claude ile reklam klonlama demosunu izle" width="600"></a>
  <p><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/readme/claude-demo-full-b9b79865b740433e.mp4">▶ Claude demosunun tamamını sesli oynat</a> · <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/hero/promo-video-5842b3c0d2ce4300.mp4">Awesome Ads Clone tanıtımını oynat</a></p>
</div>

## 🍌 Giriş

EvoLink MCP ile örnek bir reklamı kendi ürünün için yeniden oluştur. Dikkat çeken açılışı, ürün gösterimini ve kurgu ritmini koru. Reklamda kendi içerik üreticini, ürününü, mekânını ve metnini kullan.

## 📊 Genel bakış

Yeniden oluşturulan on iki reklam arasında ürün demoları, giysi denemeleri, bir skeç, bir vlog ve kameraya konuşulan bir reklam var. Belgelenen altı örneğin her birinde orijinali, yeniden oluşturulan videoyu ve yan yana karşılaştırmayı izleyebilirsin. Diğer altı testte, her testle birlikte sunulan yeniden oluşturulmuş video ve karşılaştırma yer alır.

## ⚡ Hızlı başlangıç

[EvoLink MCP](https://evolink.ai/tools/ad-clone?utm_source=github&utm_medium=readme&utm_campaign=ad-clone&utm_content=quickstart#agent) bağlantısını ajanına ekle. Ajana referans reklamı, bir ürün fotoğrafıyla açıklamasını ve içerik üreticisinin fotoğrafını ya da oyuncu seçimi için kısa bir tarif ver. Ardından bu istemi yapıştır.

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
<summary>Codex veya Claude Code üzerinden bağlan</summary>

Codex için

```sh
codex mcp add evolink --url https://mcp.evolink.ai/mcp
```

Claude Code için

```sh
claude mcp add --transport http --scope user evolink https://mcp.evolink.ai/mcp
```

İstendiğinde tarayıcıda EvoLink hesabına giriş yap. Claude Code’da `/mcp` → `evolink` → **Authenticate** yolunu izle. Codex elle giriş yapmanı isterse `codex mcp login evolink` komutunu çalıştır.

İlk üretimden önce ajanından EvoLink bakiyesini kontrol etmesini ve ilk kareyi girdi olarak kullanan bir görselden video üretme modeli bulmasını iste. Ajanın klipleri bölüp düzenleyebilmesi için yerel dosyalara ve FFmpeg/FFprobe araçlarına erişmesi gerekir. Bu adımları aynı sohbetten yürütebilir.

</details>

## 🛠️ Yedi adımda yöntem

1. **Referansı incele.** Saniyede 4 kare örnekle. Hızlı hareketlere ve kesme noktasının belirsiz olduğu yerlere daha yakından bak. Dikkat çeken açılışı, ürün gösterimini, çekimleri ve kesme noktalarını not et. Ses için varsa konuşma dökümünü ya da ajanın ses özelliklerini kullan.
2. **Hedefi yaz.** Her çekimde nelerin değişeceğini belirt. Ajanın sonuçta denetleyebileceği koşullar yaz. Örneğin, “El kapağı 1,5. saniyede kaldırana kadar kapak yerinde kalır.” Ürünle ilgili iddiaları kullanmadan önce doğrula.
3. **Klipleri kesme noktalarına göre planla.** Her çekim için bir başlangıç karesi belirle. Zor ve kesintisiz bir hareketi sabit bir pozda böl. Sonraki klibi son kullanılabilir kareden başlat. Model izin veriyorsa sonradan kırpmak için klibi biraz uzun tut.
4. **Başlangıç karelerini onayla.** Video üretimine para harcamadan önce içerik üreticisini, kıyafeti, ambalajı, ürünün nasıl göründüğünü, tutuşu ve kadrajı sabit bir görselde kontrol et. Örneğin sahnede kapaksız bir şişe gerekiyorsa başlangıç karesinde onu kapaksız göster.
5. **Girdileri birlikte kontrol et.** Her görsele veya klibe tek bir görev ver. Ürünün gizli olması gereken bir sahneyle çelişen ürün fotoğrafını kaldır. Tasarlanan hareketin başlangıç ve bitiş karelerini birbirine bağlayabildiğini doğrula. Onay vermeden önce EvoLink MCP’den tam olarak bu üretim isteği için fiyat iste.
6. **Bir klip üret ve incele.** İlk kareyi, ana hareketi ve son durumu hedefle karşılaştır. Soruna yol açan girdiyi değiştir veya çekimi böl. Yeni bir ücretli iş göndermeden önce görev kimliğini kaydet ve mevcut sonucu al.
7. **Birleştir ve son kontrolü yap.** Onaylanan klipleri kırp, onaylanmış altyazıyı ve sesi ekle, ardından reklamı dışa aktar. Tüm videonun ritmini ve devamlılığını kontrol et. Referansı karşılaştırmada kullanabiliyorsan, karşılaştırmayı yeniden oluşturulan videoyla birlikte teslim et.

<details>
<summary>İsteğe bağlı olarak Gemini ile diyalog, ses ve hareketi incele</summary>

EvoLink’in yerel Gemini API’si bir çekim dökümü veya konuşma metni taslağı hazırlayabilir. Bu isteğe bağlı adım ayrı bir `EVOLINK_API_KEY` kullanır ve MP4 dosyasını EvoLink’e gönderir. Çalıştırmadan önce ücreti kontrol et. Görsel olayların zaman damgalarını örneklenen karelerle karşılaştır.

```sh
python3 tools/video_read.py reference.mp4 work/reference-scan.md
python3 tools/video_read.py reference.mp4 work/reference-sound.md --prompt tools/prompt_sound.txt
```

</details>

## 📑 İçindekiler


| Örnek | Nelere dikkat etmeli? |
| --- | --- |
| [Evopaste diş macunu tabletleri](#case-1) | Üç ayrı çekimde dikkat çeken açılış, ürün gösterimi ve ambalajın ortaya çıkışı |
| [Önden kopçalı E-bra denemesi](#case-2) | Giysiyi tişörtün altında tutan tek bir başlangıç karesi |
| [Taqueritos cips reklamı skeci](#case-4) (taslak) | Uyuşmayan başlangıç ve bitiş karelerinin yol açtığı erime geçişi |
| [Gloss Moderne parfüm demosu](#case-5) (taslak) | Yalnızca ellerin göründüğü demoda ürünün dört farklı hâli |
| [Gym Day vlogu](#case-6) | Uzun bir hareketi kullanılabilir son kareden sürdürme |
| [Tulumla kameraya konuşma](#case-7) | Kıyafetteki tutarsızlığı konuşma arasındaki bir kesmeyle gizleme |
| [Katlanabilir güneş enerjili şarj cihazı](#n1) | Katlanabilir güneş paneli |
| [Kırmızı balm kutusu](#n2) | Yuvarlak kırmızı balm kutusu |
| [DAILYFORM protein içeceği](#n3) | Protein tozu ve karıştırma şişesi |
| [VELORA serumu](#n4) | Serumun uygulanışı |
| [PACELO spor ayakkabı kutu açılışı](#n5) | Spor ayakkabının kutudan çıkarılması |
| [VELORA Rose 01 parfümü](#n6) | Parfüm gösterimi |

## 🎬 Belgelenen örnekler

<a id="case-1"></a>

### Örnek 1: Evopaste diş macunu tabletleri

| [Orijinali oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4) | [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-video-3c95238f8ccda0bf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/reference-poster-9a45c703f1b766ee.jpg" alt="Orijinali oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-video-53453c69d9d446eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/rebuild-poster-713995491d7e02a4.jpg" alt="Yeniden oluşturulan videoyu oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-video-1583837523ced8e1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c1/comparison-poster-a03f572b1aa7b1b4.jpg" alt="Karşılaştırmayı oynat" width="210"></a> |

**Sorunu dikkat çeken bir görselle anlat. Ürün gösterimi ve ambalaj için ayrı çekimler kullan.**

Referans, sarı dişleri abartılı biçimde göstererek açılıyor. Ardından ürünün nasıl kullanıldığı ve yakından görünümü geliyor. Yeni video bu üç bölümü korudu. İçerik üreticisi değiştirildi ve ürün ile ambalajı yerine Evopaste çiğnenebilir diş macunu tabletleri kullanıldı.

Dikkat çeken açılış, köpürme gösterimi ve ambalaj ayrı kliplerde yer aldı. Etiket metni için ambalaj görseli kullanıldı. Sondaki selfie’de ters görünen yazıyı düzeltmek için görüntünün bir bölümü yatay çevrildi.

Dışa aktarılan video 21,18 saniye sürdü. Bardağa tükürme planı demoda yer almadı. Son gülümsemede dudaklarda mor köpük kaldı. O tarihte üç klip için toplam 2,52 ABD doları harcandı.

Type: Demo | Date: 2026-11-05

<a id="case-2"></a>

### Örnek 2: Önden kopçalı E-bra denemesi

| [Orijinali oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4) | [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-video-e0f411eae8770e7a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/reference-poster-dc7d5f178700c891.jpg" alt="Orijinali oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-video-b573dcc9cdb2629a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/rebuild-poster-60c737c4e310b30e.jpg" alt="Yeniden oluşturulan videoyu oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-video-f132b3396d204c82.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c2/comparison-poster-6fec48010516d597.jpg" alt="Karşılaştırmayı oynat" width="210"></a> |

**Ürün gizli kalacaksa kıyafetlerin nasıl katmanlandığını başlangıç karesinde göster ve buna aykırı ürün fotoğrafını kullanma.**

Yeniden oluşturulan video ön kopçanın gösterimini, giysi denemesini ve el hareketlerini korudu. Yeni ürün görselinde üzerinde E işareti olan lavanta rengi desenli bir sütyen vardı.

İlk denemelerde ellerin ve kopçanın hareket sırası tutmadığı için ön kopça çekiminde bir hareket referansı kullanıldı. Son el hareketinde ayrı ürün görseli, sütyenin tişörtün üstünde görünmesine yol açtı. Onaylanan çekim, tişörtün zaten göründüğü ilk kareden üretildi. El hareketi yazıyla tarif edildi.

17,50 saniyelik son videoda ön kopça, sırttaki işaret ve desenli askı yerini korudu. Kaydedilen son kesme noktaları referanstan en fazla iki kare saptı. Ortam sesi çekimden çekime azaldı. Yeniden denemeler dâhil o tarihte projeye yaklaşık 7,50 ABD doları harcandı.

Type: Demo | Date: 2026-11-10

<a id="case-4"></a>

### Örnek 4: Taqueritos cips reklamı skeci

| [Orijinali oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4) | [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-video-0c912fe25c8e0d11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/reference-poster-cc26a8b2b0404f4a.jpg" alt="Orijinali oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-video-d3c2388ec817f3c2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/rebuild-poster-1ae89b69025c81f0.jpg" alt="Yeniden oluşturulan videoyu oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-video-90a2bdef62fb3a03.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c4/comparison-poster-b6519a7ce3553d10.jpg" alt="Karşılaştırmayı oynat" width="210"></a> |

**Üretime göndermeden önce kamera hareketinin başlangıç ve bitiş karelerini birbirine bağlayabildiğini kontrol et.**

Skeçte kamera, cips paketleriyle dolu kanepenin üzerinde ayaklardan yüze doğru ilerliyor. Ardından tepki çekimine ve ambalajın gösterimine geçiliyor. Yeniden oluşturulan videoda oyuncu ve atıştırmalık ambalajı değiştirildi.

Kanepedeki çekimin ilk ve son karelerinde bacakların ve şeffaf poşetlerin yerleri birbirini tutmuyordu. Model bu farkı erime geçişiyle kapattı. Önerilen çözüm, iki kareyi de daha geniş kadrajlı tek bir görselden almak ve yalnızca kadrajı değiştirmekti.

Yukarıda anlatılan başarısız denemenin ilk klibinde kullanılan istem.

8,20 saniyelik çıktı bir taslak. İlk çekimde yaklaşık 2,15–2,60 saniyeleri arasında hâlâ erime geçişi var. Düzeltme, planda öneri olarak yer alıyor. Taslak sonuna kadar kaydedilen harcama yaklaşık 1,90 ABD dolarıydı.

<details>
<summary>Klipte kullanılan özgün istem</summary>

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

Durum: Taslak

Type: Demo | Date: 2026-11-10

<a id="case-5"></a>

### Örnek 5: Gloss Moderne parfüm demosu

| [Orijinali oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4) | [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-video-a4bc7ac22594eca7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/reference-poster-9860d96cd90c36ea.jpg" alt="Orijinali oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-video-935c0b379bc5ba3d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/rebuild-poster-85b2a7632a2e9fe1.jpg" alt="Yeniden oluşturulan videoyu oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-video-41bac2262d84f7e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c5/comparison-poster-5fdca2b06e8c364a.jpg" alt="Karşılaştırmayı oynat" width="210"></a> |

**Ürünün her fiziksel hâli için ayrı bir başlangıç karesi hazırla ve hareketi videoda görülebilen aşamalarla tarif et.**

Park hâlindeki arabada yalnızca elleri gösteren demo dört aşamadan oluşuyor: parfümün püskürtülmesi, kapaklı şişe, açık kutu ve ambalajın yakın çekimi. Yeni videoda farklı parfüm ambalajı ve her aşama için ayrı bir girdi karesi kullanıldı.

Püskürtme klibinde aralarında belirgin bir duraklama olan iki kısa püskürtme gerekiyordu. Püskürtme başlığı arada ilk konumuna dönmeliydi. Şişe klibinde kareler tek tek incelendiğinde, video analiz aracının atladığı bir dönme görüldü. Planlanan doğrusal yer değiştirme ise gerçekleşmemişti.

Püskürtme klibinde o tarihte kullanılan istem.

Teslim edilen 7,17 saniyelik taslak kesme zamanlarını ve iki püskürtmeyi korudu. Parfüm sisi hızla dağıldı ve bazı küçük yazılar teslim edilen görüntü kalitesinde bulanıklaştı. Video analizi dâhil o tarihte yaklaşık 2,43 ABD doları harcandı.

<details>
<summary>Klipte kullanılan özgün istem</summary>

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

Durum: Taslak

Type: Demo | Date: 2026-11-10

<a id="case-6"></a>

### Örnek 6: Gym Day vlogu

| [Orijinali oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4) | [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-video-b1f89a716b044b3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/reference-poster-e70d391645d77449.jpg" alt="Orijinali oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-video-587a2a376fd61041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/rebuild-poster-1c0a68aad551b8b4.jpg" alt="Yeniden oluşturulan videoyu oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-video-b77a08a3d8778035.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c6/comparison-poster-1bda13a35e25a4db.jpg" alt="Karşılaştırmayı oynat" width="210"></a> |

**Uzun bir çekimde hareket bozulursa son kullanılabilir kareden devam et.**

Yalnızca içerik üreticisi değiştirildi. Ayna selfie'si, mutfak, kapı ve egzersizden oluşan vlog sırası korundu. Mutfaktaki kaplar markasız dekor olarak kaldı.

İlk hip thrust klibinde kişi bir tekrar yaptıktan sonra doğrulup oturdu. Ekip 3,0. saniyedeki kareyi girdi olarak kullandı, hareketin devamını üretti ve iki klibi hareketin alt konumunda verilen kısa duraklamada birleştirdi.

Hip thrust hareketini sürdürmek için o tarihte kullanılan istem.

Son video 20,08 saniye, referans 20,03 saniye sürdü. Kaydedilen kesme noktaları arasındaki fark 0,2 saniyeyi aşmadı. Yeniden oluşturulan videoda seviyesi dengelenmiş ortam sesi korundu. Hareketin devamı ve video analizi dâhil o tarihte yaklaşık 5,16 ABD doları harcandı.

<details>
<summary>Klipte kullanılan özgün istem</summary>

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

### Örnek 7: Tulumla kameraya konuşma

| [Orijinali oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4) | [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4) |
| :---: | :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-video-c003681a6e134697.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/reference-poster-58941d0353aebc67.jpg" alt="Orijinali oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-video-49cc1fd51df1f336.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/rebuild-poster-b3287c0109df0b88.jpg" alt="Yeniden oluşturulan videoyu oynat" width="96"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-video-ae79ba08feafbe5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/c7/comparison-poster-5397272feab968d5.jpg" alt="Karşılaştırmayı oynat" width="210"></a> |

**Üretimden önce kıyafetin hangi açılardan nasıl görüneceğini belirle. Bir tutarsızlığı kırparak gizleyeceksen önce konuşmayı kontrol et.**

Referans, giysinin yandan nasıl durduğunu gösteren bir açılışla başlıyordu. Ardından kameraya konuşma, kıyafeti gösteren el hareketleri ve bir dönüş geliyordu. Yeni çekimde sağlanan içerik üreticisi ve hedef tarifine göre hazırlanmış sade moka rengi bir tulum kullanıldı.

İkinci üretimde sırt açıklığı hedeflenenden daha aşağıdaydı ve küçük bir dövme belirdi. Seçilen kurguda dönüş, sırt görünmeden önce konuşmadaki bir duraklamada kesildi. Video önden görünen ilk kullanılabilir kareden devam etti.

Yandan çekilen açılışta o tarihte kullanılan istem.

16,62 saniyelik ikinci sürümde kabul edilen dövme hâlâ görünüyor. Kurguda konuşulan bir cümlenin bir bölümü çıkarıldı ve üçüncü kesme referansa göre yaklaşık 1,42 saniye öne alındı. Kaydedilen üretim harcaması yaklaşık 3,02 ABD dolarıydı. Son kurgu eldeki görüntülerle yapıldı.

<details>
<summary>Klipte kullanılan özgün istem</summary>

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

## 🧪 Diğer reklam klonlama testleri

Her testte yeniden oluşturulan video ve yan yana karşılaştırma yer alır.

<a id="n1"></a>

### Katlanabilir güneş enerjili şarj cihazı

| [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-video-1cdf3eeb3c88a2cc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/rebuild-poster-e3d42a7d9134be43.jpg" alt="Yeniden oluşturulan videoyu oynat" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-video-46234333b83e6faf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n1/comparison-poster-153642d019e55d1c.jpg" alt="Karşılaştırmayı oynat" width="240"></a> |

<a id="n2"></a>

### Kırmızı balm kutusu

| [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-video-7745d3ed0b999b77.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/rebuild-poster-3f59db0c8c29c90f.jpg" alt="Yeniden oluşturulan videoyu oynat" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-video-f4c18b856b304dcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n2/comparison-poster-9a6bb937b6e93036.jpg" alt="Karşılaştırmayı oynat" width="240"></a> |

<a id="n3"></a>

### DAILYFORM protein içeceği

| [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-video-9ec5c601155e72ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/rebuild-poster-d42a814f5ae3fad3.jpg" alt="Yeniden oluşturulan videoyu oynat" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-video-114ba7b42e76a807.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n3/comparison-poster-334e3c9ede050560.jpg" alt="Karşılaştırmayı oynat" width="240"></a> |

<a id="n4"></a>

### VELORA serumu

| [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-video-cde7ba7546ad62ee.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/rebuild-poster-dd069f6bdacd31b1.jpg" alt="Yeniden oluşturulan videoyu oynat" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-video-d06d5b94fda2cf3b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n4/comparison-poster-8568c688c02d5f56.jpg" alt="Karşılaştırmayı oynat" width="240"></a> |

<a id="n5"></a>

### PACELO spor ayakkabı kutu açılışı

| [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-video-35d194b9c8cd81d2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/rebuild-poster-a741d26e1334b9cf.jpg" alt="Yeniden oluşturulan videoyu oynat" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-video-ee618c54c93da0b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n5/comparison-poster-551672d081f8de86.jpg" alt="Karşılaştırmayı oynat" width="240"></a> |

<a id="n6"></a>

### VELORA Rose 01 parfümü

| [Yeniden oluşturulan videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4) | [Karşılaştırmayı oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4) |
| :---: | :---: |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-video-ecae6fd16e1d199d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/rebuild-poster-f5667790c211c971.jpg" alt="Yeniden oluşturulan videoyu oynat" width="115"></a> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-video-c87fe39b39885eff.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-ads-clone/n6/comparison-poster-ac8191ee9f874ad3.jpg" alt="Karşılaştırmayı oynat" width="240"></a> |

## 🔗 İlgili depolar

İstemci kurulumu ve araç dokümantasyonu için [EvoLink MCP plugin](https://github.com/Evolink-AI/mcp-plugin).

## 🙏 Teşekkür

Orijinal referans reklamlar kendi yapımcılarına aittir. Bir klibe kaynak eklenmesi, klibin düzeltilmesi veya kaldırılması gerekiyorsa lütfen örneğin adını belirterek bir GitHub issue aç.
