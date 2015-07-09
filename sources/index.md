---
title: บุญจด ฟอนต์หรรษา
author: สังศิต ไสววรรณ
date: ๙ กรกฎาคม ๒๕๕๘
---

# ภาษาไทยมาตรฐาน

ฝุ่นน้ำท้องฟ้า  
ทุ่งหญ้าป้ำเป๋อ  
ชนชั้นกระฎุมพี  
เป่าปี่กตัญญู

<small>ถึงหน้าตาจะขี้เล่น แต่บุญจดรู้เรื่องการวางตำแหน่งตัวอักษรและเข้าใจวิธีเขียนภาษาไทยมาตรฐานในเว็บบราวเซอร์สมัยใหม่นะฮะ</small>

# ภาษาบาลี/สันสกฤต

<p lang="pi-Thai">ฐาตุํ ญาติํ อุปฺปฏฺฐานํ ปุํลิงฺคํ วาปิํ ปํสุํ วฏฺฏุํ</p>

~~~html
<p lang="pi-Thai">ฐาตุํ ญาติํ อุปฺปฏฺฐานํ ปุํลิงฺคํ วาปิํ ปํสุํ วฏฺฏุํ</p>
~~~

~~~css
body { font-feature-settings: "locl"; }
~~~

<small>แถมใช้บุญจดเขียนบาลี/สันสกฤตใน HTML ได้ด้วย `lang="pi-Thai"` แต่ต้องใช้ CSS ช่วยนิดหน่อย</small>

# ภาษาชาติพันธุ์

ปะเฺติ็ลฺ โฺญฺ็จฺ ปั็วฮฺ ทฺ็อง เปฺิ็ว มูํย แต็่ง เจฺํอ  
เปรฺิ่ห์ โจ๊่ เปฺี่ย โฺทร ม็่อง เติ็ง อาื ยาึ จือรฺุ การฺู

<small>บุญจดรับมือวิธีเขียนที่ซับซ้อนกว่าภาษาไทยมาตรฐานได้แต่กำเนิดอีกต่างหาก <span style="font-size:120px;line-height:2.1em;">ฮฺูุ็ํ้!!!</span></small>

# Thai Ligatures

ฤๅ ฦๅ ๏่่ ๏..

~~~
ฤๅ ฦๅ ๏่่ ๏..
~~~

~~~css
body { font-variant: common-ligatures; }
~~~

<small>อันนี้ของแถมสำหรับภาษาไทย เปิดใช้งาน Ligatures ได้ด้วย CSS</small>

# Mixed language paragraphs

<p style="font-size:18px; text-align:left;">
ฝุ่นน้ำท้องฟ้า ทุ่งหญ้าป้ำเป๋อ ชนชั้นกระฎุมพี เป่าปี่กตัญญู <span lang="pi-Thai">ฐาตุํ ญาติํ อุปฺปฏฺฐานํ ปุํลิงฺคํ วาปิํ ปํสุํ วฏฺฏุํ</span> ปะเฺติ็ลฺ โฺญฺ็จฺ ปั็วฮฺ ทฺ็อง เปฺิ็ว มูํย แต็่ง เจฺํอ เปรฺิ่ห์ โจ๊่ เปฺี่ย โฺทร ม็่อง เติ็ง อาื ยาึ จือรฺุ การฺู Quick zephyrs blow, vexing daft Jim. Do bạch kim rất quý, sẽ để lắp vô xương. „Fix, Schwyz!“ quäkt Jürgen blöd vom Paß. „Oh, welch Zynismus!“, quiekte Xavers jadegrüne Bratpfanne. Voyez le brick géant que j'examine près du wharf Quel vituperabile xenofobo zelante assaggia il whisky ed esclama: alleluja! Queda gazpacho, fibra, látex, jamón, kiwi y viñas. Luís argüia à Júlia que «brações, fé, chá, óxido, pôr, zângão» eram palavras do português.</p>

<p style="font-size:18px; text-align:left;">
Jove xef, porti whisky amb quinze glaçons d'hidrogen, coi! Laŭ Ludoviko Zamenhof bongustas freŝa ĉeĥa manĝaĵo kun spicoj. Høj bly gom vandt fræk sexquiz på wc Vår sære Zulu fra badeøya spilte jo whist og quickstep i min taxi. Pójdźże, kiń tę chmurność w głąb flaszy! Příliš žluťoučký kůň úpěl ďábelské ódy Kæmi ný öxi hér ykist þjófum nú bæði víl og ádrepa. <span lang="ro">Gheorghe, obezul, a reuşit să obţină jucându-se un flux în Quebec de o mie kilowaţioră.</span> Egy hűtlen vejét fülöncsípő, dühös mexikói úr Wesselényinél mázol Quitóban.
</p>

~~~css
body { font-kerning: normal; }
~~~

<small>Enable font kerning with CSS code above if you want this feature for small texts.</small>

# Subscripts & Superscripts

H<sub>2</sub>O &times; 9.87<sup>654</sup> &#x2260; &radic;&pi; &divide; World<sup>3</sup>!

~~~html
H<sub>2</sub>O &times; 9.87<sup>654</sup> &#x2260; &radic;&pi; &divide; World<sup>3</sup>!
~~~

~~~css
sub { font-feature-settings: "sups"; }
sup { font-feature-settings: "sups"; }
~~~

<small>You can easily write subscripts & superscripts with `<sub>` & `<sup>` elements, just enable BoonJot&rsquo;s features.</small>

# Fractions

1&thinsp;&frac14; 5&thinsp;&frac12; 9&thinsp;&frac34; <span class="frac">1/3 2/3 1/8 3/8 5/8 7/8</span>

<p class="frac">
  123456789123456789/98765432109876543210
</p>

~~~html
1&thinsp;&frac14; 5&thinsp;&frac12; 9&thinsp;&frac34; <span class="frac">1/3 2/3 1/8 3/8 5/8 7/8</span>
<span class="frac">123456789123456789/98765432109876543210</span>
~~~

~~~css
.frac { font-feature-settings: "frac"; }
~~~

<small>BoonJot supports both pre-composed & arbitrary fractions.</small>

# Localized forms

<p lang="ro">Gheorghe, obezul, a reuşit să obţină jucându-se un flux în Quebec de o mie kilowaţioră.</p>

~~~html
<p lang="ro">Gheorghe, obezul, a reuşit să obţină jucându-se un flux în Quebec de o mie kilowaţioră.</p>
~~~

<small>Don&rsquo;t worry about old encoded texts, BoonJot can correct Romanian/Moldovan for you.</small>
