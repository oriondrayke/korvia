const params=new URLSearchParams(location.search);const key=params.get('for')||'cheso';const d=window.PROSPECTS[key]||window.PROSPECTS.cheso;
document.documentElement.style.setProperty('--accent',d.color);document.title=`${d.name} · Unofficial presentation concept`;
const put=(id,value)=>document.getElementById(id).textContent=value;
put('monogram',(d.short.match(/[A-Z]/g)||[d.short[0]]).slice(0,3).join(''));put('shortName',d.short);put('type',d.type);put('headline',d.headline);put('intro',d.intro);put('signal',d.tags.join(' · '));put('aboutTitle',d.name);put('aboutText',d.about);put('sourceNote',d.source);put('impactTitle',d.impact);put('impactText',d.impactText);put('quote',d.quote);put('footerName',d.name);
document.getElementById('heroImage').style.backgroundImage=`url("${d.image}")`;
document.getElementById('cards').innerHTML=d.programs.map((x,i)=>`<article class="card"><span class="number">0${i+1}</span><h3>${x[0]}</h3><p>${x[1]}</p></article>`).join('');
document.getElementById('tags').innerHTML=d.tags.map(x=>`<span>${x}</span>`).join('');
const email=document.getElementById('emailLink');email.href=`mailto:${d.email}`;email.textContent=`Contact ${d.short} ↗`;
