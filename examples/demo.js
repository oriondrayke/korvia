const params=new URLSearchParams(location.search);
const category=params.get('category')||document.body.className;
const theme=Math.max(0,Math.min(9,Number(params.get('theme')||0)));
const palettes=[
  ['#173b68','#f1b94c','#f5f2e9','18px'],['#7a4d2d','#e7b86b','#f6efe5','28px'],['#111','#ffe45e','#f6f1db','2px'],['#332b36','#cfa66e','#f2ece4','0'],['#416b4b','#b8dc83','#f1f6ed','34px'],['#65459a','#e58e63','#f4f0fa','18px'],['#713d33','#d5ab79','#f5f0e7','0'],['#111','#ef3d2f','#fff','0'],['#83572d','#e9c360','#f7f0dc','12px'],['#9a5575','#f0b5c9','#faf0f4','28px']
];
const p=palettes[theme];document.body.dataset.theme=theme;document.documentElement.style.setProperty('--brand',p[0]);document.documentElement.style.setProperty('--accent',p[1]);document.documentElement.style.setProperty('--paper',p[2]);document.querySelectorAll('.visual,.card,.band').forEach(el=>el.style.borderRadius=p[3]);
const labels={school:'school',ngo:'NGO',health:'healthcare',hospitality:'hospitality',institution:'institution',business:'business'};
const bar=document.createElement('div');bar.className='survey-bar';bar.innerHTML=`<a href="gallery.html?category=${category}">← Continue viewing ${labels[category]||category} designs</a><span>This is a sample. Your website will be custom-designed.</span><a class="survey-wa" href="https://wa.me/255682087992?text=Hello%20Korvia%20Studio%2C%20I%20need%20a%20custom%20${encodeURIComponent(labels[category]||category)}%20website." target="_blank">Contact on WhatsApp ↗</a>`;document.body.appendChild(bar);
