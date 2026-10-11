(function () {
'use strict';
var platforms = [{"key": "android", "name": "اندروید موبایل", "en": "Android", "version": "3.9.3", "format": "APK", "path": "/wp-content/uploads/2026/09/FilmKio3.9.3.apk?build=793668d9", "note": "برای موبایل و تبلت اندرویدی", "title": "سینمای شما،<br>همیشه همراه شما.", "desc": "فیلم و سریال دلخواهتان را پیدا کنید، تماشا را ادامه دهید و با همان حساب فیلمکیو، روی موبایل همراهش داشته باشید.", "image": "android", "href": "/download/android/"}, {"key": "tv", "name": "اندروید تی‌وی", "en": "Android TV", "version": "2.9", "format": "APK", "path": "/wp-content/uploads/2026/07/FilmkioTv.2.9.apk", "note": "تلویزیون، گوگل تی‌وی و اندروید باکس", "title": "تماشا روی<br>بزرگ‌ترین صفحهٔ خانه.", "desc": "نسخهٔ مخصوص تلویزیون و اندروید باکس، با رابط مناسب نمایشگر بزرگ و کنترل با ریموت.", "image": "tv", "href": "/download/tv/"}, {"key": "windows", "name": "ویندوز", "en": "Windows", "version": "1.5.3", "format": "EXE", "path": "/wp-content/uploads/2026/03/FilmKio-Setup-1.5.3.exe", "note": "برای کامپیوتر و لپ‌تاپ ویندوزی", "title": "از دسکتاپ،<br>به دنیای سینما.", "desc": "فیلمکیو را روی کامپیوتر نصب کنید و مستقیم از دسکتاپ به آرشیو فیلم و سریال دسترسی داشته باشید.", "image": "windows", "href": "/download/windows/"}, {"key": "mac", "name": "مک", "en": "macOS", "version": "1.5.3", "format": "PKG", "path": "/wp-content/uploads/2026/03/FilmKio-1.5.3.pkg", "note": "نصب با بستهٔ macOS", "title": "وقت تماشا،<br>روی مک شما.", "desc": "نسخهٔ دسکتاپ فیلمکیو برای مک؛ دسترسی به آرشیو با همان حساب و اشتراکی که در سایت دارید.", "image": "mac", "href": "/download/mac/"}, {"key": "linux", "name": "لینوکس", "en": "Linux", "version": "1.5.3-2", "format": "DEB", "path": "/wp-content/uploads/filmkio-releases/linux/FilmKio-1.5.3-2-amd64.deb", "note": "آزمایشی · Ubuntu 24.04 / Mint 22 · x86_64", "title": "فیلمکیو،<br>حالا روی لینوکس.", "desc": "نسخهٔ آزمایشی برای کامپیوترهای ۶۴ بیتی اینتل و AMD. بستهٔ DEB برای اوبونتو و مینت و راهنمای نصب برای آرچ.", "image": "mac", "href": "/download/linux/"}, {"key": "tvweb", "name": "ال‌جی و سامسونگ", "en": "TV Browser", "version": "", "format": "", "path": "", "note": "در مرورگر تلویزیون، بدون نصب", "title": "تلویزیون شما،<br>سینمای شما.", "desc": "فیلمکیو را در مرورگر تلویزیون ال‌جی یا سامسونگ باز کنید و با ریموت کنترل کنید؛ بدون نیاز به فایل نصب.", "image": "tv", "href": "#tv-browser"}];
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
})();