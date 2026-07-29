const params=new URLSearchParams(location.search);const key=params.get('for')||'cheso';const d=window.PROSPECTS[key]||window.PROSPECTS.cheso;
document.documentElement.style.setProperty('--accent',d.color);document.title=`${d.name} · Unofficial presentation concept`;
const put=(id,value)=>document.getElementById(id).textContent=value;
put('monogram',(d.short.match(/[A-Z]/g)||[d.short[0]]).slice(0,3).join(''));put('shortName',d.short);put('type',d.type);put('headline',d.headline);put('intro',d.intro);put('signal',d.tags.join(' · '));put('aboutTitle',d.name);put('aboutText',d.about);put('sourceNote',d.source);put('impactTitle',d.impact);put('impactText',d.impactText);put('quote',d.quote);put('footerName',d.name);
document.getElementById('heroImage').style.backgroundImage=`url("${d.image}")`;
document.getElementById('cards').innerHTML=d.programs.map((x,i)=>`<article class="card"><span class="number">0${i+1}</span><h3>${x[0]}</h3><p>${x[1]}</p></article>`).join('');
document.getElementById('tags').innerHTML=d.tags.map(x=>`<span>${x}</span>`).join('');
const email=document.getElementById('emailLink');email.href=`mailto:${d.email}`;email.textContent=`Contact ${d.short} ↗`;

if(d.locale==='fr-BI'){
  document.documentElement.lang='fr';
  const nav=[...document.querySelectorAll('header nav a')];['À propos','Nos actions','Impact','Contact'].forEach((x,i)=>{if(nav[i])nav[i].textContent=x});
  document.querySelector('.concept strong').textContent='Concept de présentation non officiel';
  document.querySelector('.concept span').textContent="Préparé indépendamment par Korvia Studio à partir d’informations publiques. Ceci n’est pas le site officiel de l’organisation.";
  document.querySelector('.menu').textContent='Menu';
  const actions=document.querySelectorAll('.actions a');actions[0].textContent='Découvrir nos actions';actions[1].textContent='Nous contacter';
  document.querySelector('.signal span').textContent='Axes de présentation';
  document.querySelector('.about .eyebrow').textContent='Qui sommes-nous';
  document.querySelector('.work .eyebrow').textContent='Nos actions';
  document.querySelector('.work h2').textContent='Une mission comprise dès le premier regard.';
  document.querySelector('.section-head>p').textContent="Ce concept organise les priorités publiques de l’organisation dans une expérience claire, crédible et adaptée au téléphone.";
  document.querySelector('.impact .eyebrow').textContent='Une plateforme pour progresser';
  document.querySelector('.quote>span').textContent='Conçu pour';
  document.querySelector('.quote small').textContent='Direction conceptuelle · Korvia Studio';
  document.querySelector('.contact .eyebrow').textContent='Développer l’expérience complète';
  document.querySelector('.contact h2').textContent='Ceci est une première page, pas une limite.';
  document.querySelector('.contact p').textContent="Le site complet peut intégrer des témoignages vérifiés, des photographies authentiques, des rapports, des formulaires, des pages partenaires et le processus de publication choisi par l’organisation.";
  email.textContent=`Contacter ${d.short} ↗`;
  document.querySelector('footer div:first-child span').textContent='Concept de présentation';
  document.querySelector('footer div:last-child span').textContent='Concept par';
  const switcher=document.createElement('div');switcher.className='language-switcher';switcher.innerHTML='<button class="active" data-lang="fr">Français</button><button data-lang="rn">Kirundi</button><button data-lang="en">English</button>';document.querySelector('header').insertBefore(switcher,document.querySelector('header nav'));
  const note=document.createElement('div');note.className='language-note';note.setAttribute('role','status');document.body.appendChild(note);
  switcher.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;if(b.dataset.lang==='fr'){note.textContent='La démonstration est actuellement présentée en français.'}else if(b.dataset.lang==='rn'){note.textContent="La version Kirundi sera activée lors du déploiement final après validation de la traduction par l’équipe de l’organisation."}else{note.textContent="The English version can be activated in the final website after the organization reviews and approves the translation."}note.classList.add('show');clearTimeout(window.langTimer);window.langTimer=setTimeout(()=>note.classList.remove('show'),4200)});
}
