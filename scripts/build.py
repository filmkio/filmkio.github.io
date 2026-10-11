from pathlib import Path
import json, shutil, re, html
P=Path(__file__).resolve().parents[1]
platforms=[
 dict(key='android',name='اندروید موبایل',en='Android',version='3.9.3',format='APK',path='/wp-content/uploads/2026/09/FilmKio3.9.3.apk?build=793668d9',note='برای موبایل و تبلت اندرویدی',title='سینمای شما،<br>همیشه همراه شما.',desc='فیلم و سریال دلخواهتان را پیدا کنید، تماشا را ادامه دهید و با همان حساب فیلمکیو، روی موبایل همراهش داشته باشید.',image='android'),
 dict(key='tv',name='اندروید تی‌وی',en='Android TV',version='2.9',format='APK',path='/wp-content/uploads/2026/07/FilmkioTv.2.9.apk',note='تلویزیون، گوگل تی‌وی و اندروید باکس',title='تماشا روی<br>بزرگ‌ترین صفحهٔ خانه.',desc='نسخهٔ مخصوص تلویزیون و اندروید باکس، با رابط مناسب نمایشگر بزرگ و کنترل با ریموت.',image='tv'),
 dict(key='windows',name='ویندوز',en='Windows',version='1.5.3',format='EXE',path='/wp-content/uploads/2026/03/FilmKio-Setup-1.5.3.exe',note='برای کامپیوتر و لپ‌تاپ ویندوزی',title='از دسکتاپ،<br>به دنیای سینما.',desc='فیلمکیو را روی کامپیوتر نصب کنید و مستقیم از دسکتاپ به آرشیو فیلم و سریال دسترسی داشته باشید.',image='windows'),
 dict(key='mac',name='مک',en='macOS',version='1.5.3',format='PKG',path='/wp-content/uploads/2026/03/FilmKio-1.5.3.pkg',note='نصب با بستهٔ macOS',title='وقت تماشا،<br>روی مک شما.',desc='نسخهٔ دسکتاپ فیلمکیو برای مک؛ دسترسی به آرشیو با همان حساب و اشتراکی که در سایت دارید.',image='mac'),
 dict(key='linux',name='لینوکس',en='Linux',version='1.5.3-2',format='DEB',path='/wp-content/uploads/filmkio-releases/linux/FilmKio-1.5.3-2-amd64.deb',note='آزمایشی · Ubuntu 24.04 / Mint 22 · x86_64',title='فیلمکیو،<br>حالا روی لینوکس.',desc='نسخهٔ آزمایشی برای کامپیوترهای ۶۴ بیتی اینتل و AMD. بستهٔ DEB برای اوبونتو و مینت و راهنمای نصب برای آرچ.',image='mac'),
 dict(key='tvweb',name='ال‌جی و سامسونگ',en='TV Browser',version='',format='',path='',note='در مرورگر تلویزیون، بدون نصب',title='تلویزیون شما،<br>سینمای شما.',desc='فیلمکیو را در مرورگر تلویزیون ال‌جی یا سامسونگ باز کنید و با ریموت کنترل کنید؛ بدون نیاز به فایل نصب.',image='tv')]
icons={
'android':'<rect x="6" y="3" width="12" height="18" rx="3"/><path d="M10 6h4M11 18h2"/>',
 'tv':'<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
 'windows':'<path d="M3 5l8-1v7H3V5Zm10-1 8-1v8h-8V4ZM3 13h8v7l-8-1v-6Zm10 0h8v8l-8-1v-7Z"/>',
 'mac':'<rect x="5" y="3" width="14" height="12" rx="1"/><path d="m5 15-3 5h20l-3-5M10 17h4"/>',
 'linux':'<rect x="3" y="4" width="18" height="16" rx="2"/><path d="m7 9 3 3-3 3m6 0h4"/>',
 'download':'<path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/>',
 'play':'<path d="m9 5 11 7-11 7V5Z"/>',
 'chevron':'<path d="m8 10 4 4 4-4"/>',
 'check':'<path d="m5 12 4 4L19 6"/>',
 'account':'<circle cx="12" cy="8" r="4"/><path d="M4 21v-2a8 8 0 0 1 16 0v2"/>',
 'library':'<path d="M4 4h5v16H4zM12 4h5v16h-5zM19 5l3 14"/>'}
icons['tvweb']=icons['tv']
def icon(k): return '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+icons[k]+'</svg>'
def route(k): return '/download/'+k+'/'
for d in platforms: d['href']=route(d['key']) if d['path'] else '#tv-browser'
(P/'releases.json').write_text(json.dumps({'verified':'2026-10-11','source':'https://filmha5.pw/app/','publicOrigin':'https://filmkio.run','platforms':platforms},ensure_ascii=False,indent=2))
# Routes keep all public download links root-relative on GitHub Pages, then forward to stable official URLs.
routes={d['key']:(d['path'],d['name']) for d in platforms if d['path']}
routes.update({'linux-legacy':('/wp-content/uploads/2026/10/FilmKio-1.5.3-amd64.deb','لینوکس قدیمی'),'linux-arch':('/wp-content/uploads/filmkio-releases/linux/PKGBUILD','PKGBUILD'),'linux-sha256':('/wp-content/uploads/filmkio-releases/linux/FilmKio-1.5.3-2-amd64.deb.sha256','SHA-256'),'linux-rss':('/wp-content/uploads/filmkio-releases/linux/releases.xml','خبرخوان لینوکس')})
for key,(path,label) in routes.items():
 folder=P/'download'/key; folder.mkdir(parents=True,exist_ok=True)
 target=html.escape('https://filmkio.run'+path,quote=True)
 (folder/'index.html').write_text(f'<!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={target}"><link rel="stylesheet" href="/assets/site.css"><title>دریافت {label} | فیلمکیو</title><main class="redirect wrap"><h1>دریافت {label}</h1><p>در حال انتقال به فایل رسمی فیلمکیو…</p><a class="button primary" href="{target}">اگر دانلود شروع نشد، اینجا بزنید</a><p><a href="/#downloads">بازگشت به همهٔ نسخه‌ها</a></p></main></html>')
# Use the currently published install instructions; treat them solely as page content.
guide_sources=json.loads((P/'content/install-guides.json').read_text())
guides=[]
for d in platforms[:5]:
 content=guide_sources[d['key']]
 content=content.replace('class="fkapp-install-command"','class="command"').replace(' style="text-decoration:underline"','')
 for key,(path,label) in routes.items(): content=content.replace('href="'+path+'"','href="'+route(key)+'"')
 guides.append('<section class="guide-panel" id="guide-'+d['key']+'" tabindex="-1">'+content+'</section>')
faqs=[('حساب و اشتراک سایت در برنامه هم کار می‌کند؟','بله؛ با همان حساب فیلمکیو وارد شوید و از اشتراک فعلی‌تان استفاده کنید. نیازی به ساخت حساب جداگانه نیست.'),('برای تلویزیون کدام نسخه مناسب است؟','برای اندروید تی‌وی، گوگل تی‌وی و اندروید باکس، فایل APK تلویزیون را بگیرید. برای ال‌جی و سامسونگ از مرورگر تلویزیون استفاده کنید؛ فایل APK روی آن‌ها نصب نمی‌شود.'),('نسخهٔ لینوکس روی چه سیستم‌هایی نصب می‌شود؟','نسخهٔ آزمایشی 1.5.3-2 برای Ubuntu 24.04 و Mint 22 با معماری x86_64 است. برای Ubuntu 22.04 و Mint 21 از نسخهٔ قدیمی موجود در راهنما استفاده کنید. نصب روی ARM پشتیبانی این بسته نیست.'),('اگر پخش یا دانلود مشکل داشت چه کنم؟','کیفیت دیگری و یک عنوان دیگر را امتحان کنید. برای دانلود، لینک تازه بگیرید و فضای خالی دستگاه را بررسی کنید. اگر مشکل ادامه داشت، نام عنوان، کیفیت، مدل دستگاه و متن خطا را در تیکت پشتیبانی بنویسید.'),('زیرنویس را چطور فعال کنم؟','در تنظیمات زیرنویس پلیر، فارسی را انتخاب کنید. نسخهٔ «بدون زیرنویس» زیرنویس همراه ندارد و زیرنویس «هاردساب» روی تصویر است و خاموش نمی‌شود.')]
buttons=''.join(f'<button type="button" class="device" data-device="{d["key"]}" aria-pressed="{str(i==0).lower()}" aria-controls="device-preview">{icon(d["key"])}<span>{d["name"]}</span><small dir="ltr">{d["en"]}</small></button>' for i,d in enumerate(platforms))
cards=''
for d in platforms:
 version=f'نسخهٔ <bdi>{d["version"]}</bdi>' if d['version'] else 'بدون نیاز به نصب'
 cards+=f'<article class="release"><div class="release-icon">{icon(d["key"])}</div><div class="release-info"><h3>{d["name"]}</h3><p>{d["note"]}</p><span class="version">{version}</span></div><div class="release-actions"><a class="button download" href="{d["href"]}">{icon("download" if d["version"] else "play")}<span>{"دانلود " + d["format"] if d["version"] else "راهنمای تماشا"}</span></a>'+(f'<a class="guide-link" href="#guide-{d["key"]}">راهنمای نصب</a>' if d['version'] else '<span class="guide-link">با کنترل تلویزیون</span>')+'</div></article>'
schema={'@context':'https://schema.org','@graph':[{'@type':'WebPage','url':'https://filmkio.github.io/','name':'دانلود اپلیکیشن فیلمکیو','inLanguage':'fa-IR'},{'@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'item':{'@type':'SoftwareApplication','name':'فیلمکیو '+d['name'],'operatingSystem':d['en'],'applicationCategory':'EntertainmentApplication','softwareVersion':d['version'],'downloadUrl':'https://filmkio.github.io'+d['href']}} for i,d in enumerate(platforms[:5])]}, {'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in faqs]}]}
page='''<!doctype html>
<html lang="fa" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>دانلود فیلمکیو | اندروید، تلویزیون، ویندوز، مک و لینوکس</title>
<meta name="description" content="نسخهٔ رسمی فیلمکیو برای اندروید، اندروید تی‌وی، ویندوز، مک و لینوکس؛ همراه با راهنمای نصب و تماشا در مرورگر تلویزیون‌های ال‌جی و سامسونگ.">
<meta name="robots" content="index,follow,max-image-preview:large"><meta name="theme-color" content="#101319">
<meta name="google-site-verification" content="cX1XcpwmOI-I8Bc0euwlaq72qp1mdd3fgt9zG9Ximvk">
<link rel="canonical" href="https://filmkio.github.io/"><link rel="icon" href="/assets/images/favicon-v.png"><link rel="preload" href="/assets/fonts/YekanBakh-Regular.woff2" as="font" type="font/woff2" crossorigin>
<meta property="og:type" content="website"><meta property="og:locale" content="fa_IR"><meta property="og:site_name" content="FilmKio"><meta property="og:title" content="فیلمکیو، روی دستگاه شما"><meta property="og:description" content="دانلود برنامه‌های فیلمکیو و راهنمای تماشا روی تلویزیون"><meta property="og:url" content="https://filmkio.github.io/"><meta property="og:image" content="https://filmkio.github.io/assets/images/filmkio-showcase-android.png"><meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script>
<script type="application/ld+json">SCHEMA</script></head><body>
<a class="skip" href="#main">رفتن به محتوای اصلی</a>
<header class="header wrap"><a class="brand" href="/" aria-label="فیلمکیو، خانه"><img src="/assets/images/FilmKio-logo-v4.png" width="143" height="35" alt="FilmKio"></a><nav aria-label="منوی اصلی"><a href="#downloads">دانلود برنامه</a><a href="#install">راهنمای نصب</a><a href="#faq">پرسش‌ها</a></nav><a class="site-link" href="https://filmkio.run/">ورود به سایت ICONPLAY</a></header>
<main id="main"><section class="hero wrap" aria-labelledby="hero-title"><div class="hero-copy"><p class="intro"><span></span>اپلیکیشن‌های رسمی فیلمکیو</p><h1 id="hero-title">سینمای شما،<br>همیشه همراه شما.</h1><p id="hero-desc" class="lead">فیلم و سریال دلخواهتان را پیدا کنید، تماشا را ادامه دهید و با همان حساب فیلمکیو، روی موبایل همراهش داشته باشید.</p><div class="hero-actions"><a id="hero-download" class="button primary" href="/download/android/">ICONDOWNLOAD<span>دانلود اندروید موبایل</span></a><a class="text-link" href="#downloads">همهٔ نسخه‌ها</a></div><p id="hero-version" class="hero-meta">نسخهٔ <bdi>3.9.3</bdi> <span>·</span> فایل APK</p></div><figure id="device-preview" class="hero-visual"><img id="hero-image" src="/assets/images/filmkio-showcase-android.png" width="1200" height="800" fetchpriority="high" alt="نمای برنامه‌های فیلمکیو روی موبایل و نمایشگرهای بزرگ"><figcaption id="hero-caption">از صفحهٔ کوچک تا پردهٔ بزرگ</figcaption></figure></section>
<section class="device-section wrap" aria-label="انتخاب دستگاه"><div class="device-label">کجا تماشا می‌کنید؟<span>دستگاهتان را انتخاب کنید</span></div><div class="devices">BUTTONS</div></section>
<section class="features wrap" aria-label="امکانات فیلمکیو"><article>ICONLIBRARY<div><h2>آرشیو فیلم و سریال</h2><p>دسترسی به عنوان‌های دلخواهتان در برنامه</p></div></article><article>ICONPLAY<div><h2>ادامهٔ تماشا</h2><p>در نسخهٔ موبایل، از جایی که مانده‌اید</p></div></article><article>ICONACCOUNT<div><h2>همان حساب فیلمکیو</h2><p>ورود با حساب و استفاده از اشتراک فعلی</p></div></article></section>
<section id="downloads" class="downloads section wrap"><div class="section-heading"><div><h2>فیلمکیو برای دستگاه شما</h2><p>نسخهٔ مناسب را بگیرید؛ راهنمای نصب هم همین‌جاست.</p></div><span class="verified">به‌روز شده در ۱۹ مهر ۱۴۰۵</span></div><div class="releases">CARDS</div></section>
<section id="tv-browser" class="tv-section wrap"><div class="tv-copy"><span class="tag">بدون نصب برنامه</span><h2>روی ال‌جی و سامسونگ،<br>فقط مرورگر را باز کنید.</h2><p>نسخهٔ وب تلویزیون با ریموت کار می‌کند. با همان حساب فیلمکیو وارد شوید؛ فایل APK لازم ندارید.</p><ol><li>مرورگر تلویزیون را باز کنید: <bdi>Web Browser</bdi> در ال‌جی یا <bdi>Internet</bdi> در سامسونگ.</li><li>آدرس <a href="https://filmkio.run/app/"><bdi>filmkio.run/app</bdi></a> را وارد کنید.</li><li>دکمهٔ «ورود به فیلمکیو روی تلویزیون» را بزنید و از بخش حساب کاربری وارد شوید.</li></ol><a class="button primary" href="https://filmkio.run/?filmkio_tv_launch=1">ICONPLAY ورود به نسخهٔ تلویزیون</a><p class="fine">سازگاری به مدل تلویزیون و نسخهٔ مرورگر بستگی دارد.</p></div><figure class="tv-visual"><img src="/assets/images/filmkio-showcase-tv.png" width="1200" height="800" loading="lazy" alt="رابط اندروید تی‌وی فیلمکیو روی نمایشگر بزرگ"><figcaption>تصویر نمونه: نسخهٔ اندروید تی‌وی</figcaption><div class="remote-note">کلیدهای جهت‌دار برای جابه‌جایی <span>OK برای انتخاب</span></div></figure></section>
<section id="install" class="section wrap"><div class="section-heading"><div><h2>از دانلود تا اولین تماشا</h2><p>راهنمای مخصوص دستگاهتان را انتخاب کنید.</p></div></div><div class="install-layout"><nav class="guide-choices" aria-label="انتخاب راهنمای نصب">GUIDEBUTTONS</nav><div class="guide-content">GUIDES</div></div></section>
<section id="faq" class="faq section wrap"><div class="faq-intro"><h2>قبل از شروع تماشا</h2><p>پاسخ چند پرسش پرتکرار.</p><a class="text-link" href="https://filmkio.run/dashboard/">پشتیبانی در حساب کاربری</a></div><div class="faq-items">FAQS</div></section>
</main><footer class="wrap footer"><div><strong>فیلمکیو</strong><span>از صفحهٔ کوچک تا پردهٔ بزرگ.</span></div><a href="https://filmkio.run/">سایت فیلمکیو</a><a href="#downloads">دریافت اپلیکیشن‌ها</a><p>نصب برنامه رایگان است؛ استفاده از محتوا تابع شرایط اشتراک فیلمکیو است.</p></footer></body></html>'''
replacements={'SCHEMA':json.dumps(schema,ensure_ascii=False),'BUTTONS':buttons,'CARDS':cards,'GUIDES':''.join(guides),'GUIDEBUTTONS':''.join(f'<a href="#guide-{d["key"]}" data-guide="{d["key"]}">{icon(d["key"])}{d["name"]}</a>' for d in platforms[:5]),'FAQS':''.join(f'<details><summary>{q}{icon("chevron")}</summary><p>{a}</p></details>' for q,a in faqs),'ICONPLAY':icon('play'),'ICONDOWNLOAD':icon('download'),'ICONLIBRARY':icon('library'),'ICONACCOUNT':icon('account')}
for k in sorted(replacements,key=len,reverse=True): page=page.replace(k,replacements[k])
(P/'index.html').write_text(page)
(P/'assets/site.js').write_text('''(function () {
'use strict';
var platforms = '''+json.dumps(platforms,ensure_ascii=False)+''';
var devices = document.querySelectorAll('[data-device]');
function selectDevice(key) {
 var d, i;
 for (i=0;i<platforms.length;i++) if(platforms[i].key===key) d=platforms[i];
 if (!d) return;
 document.getElementById('hero-title').innerHTML=d.title;
 document.getElementById('hero-desc').textContent=d.desc;
 var link=document.getElementById('hero-download');
 link.href=d.href; link.querySelector('span').textContent=d.version?'دانلود '+d.name:'راهنمای تماشا در مرورگر';
 document.getElementById('hero-version').textContent=d.version?'نسخهٔ '+d.version+' · '+(key==='linux'?'آزمایشی · x86_64':'فایل '+d.format):'بدون فایل نصب · کنترل با ریموت';
 var shot=document.getElementById('hero-image'); shot.src='/assets/images/filmkio-showcase-'+d.image+'.png'; shot.alt='نمای برنامهٔ فیلمکیو: '+(key==='linux'?'تصویر نمونهٔ نسخهٔ مک':key==='tvweb'?'تصویر نمونهٔ اندروید تی‌وی':d.name);
 document.getElementById('hero-caption').textContent=key==='linux'?'تصویر نمونه: نسخهٔ مک':key==='tvweb'?'تصویر نمونه: نسخهٔ اندروید تی‌وی':d.name+' · FilmKio';
 for(i=0;i<devices.length;i++) devices[i].setAttribute('aria-pressed',devices[i].getAttribute('data-device')===key?'true':'false');
}
for(var i=0;i<devices.length;i++) devices[i].addEventListener('click',function(){selectDevice(this.getAttribute('data-device'));});
var panels=document.querySelectorAll('.guide-panel'), choices=document.querySelectorAll('[data-guide]');
function selectGuide(key) {
 var found=false,i;
 for(i=0;i<panels.length;i++) if(panels[i].id==='guide-'+key) found=true;
 if(!found) return;
 for(i=0;i<panels.length;i++) panels[i].hidden=panels[i].id!=='guide-'+key;
 for(i=0;i<choices.length;i++) {if(choices[i].getAttribute('data-guide')===key) choices[i].setAttribute('aria-current','true'); else choices[i].removeAttribute('aria-current');}
}
function hashGuide(){var m=/^#guide-(android|tv|windows|mac|linux)$/.exec(location.hash);if(m){selectGuide(m[1]);document.getElementById('guide-'+m[1]).scrollIntoView();}}
selectGuide('android');
var anchors=document.querySelectorAll('a[href^="#guide-"]');
for(i=0;i<anchors.length;i++) anchors[i].addEventListener('click',function(){selectGuide(this.getAttribute('href').replace('#guide-',''));});
window.addEventListener('hashchange',hashGuide);hashGuide();
})();''')
(P/'.nojekyll').write_text('')
(P/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://filmkio.github.io/sitemap.xml\n')
(P/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://filmkio.github.io/</loc><lastmod>2026-10-11</lastmod></url></urlset>')
print('Built',P)
