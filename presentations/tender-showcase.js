const params = new URLSearchParams(location.search);
const key = params.get('for') || 'ke-ksa';
const base = window.PROSPECTS[key];
if (!base) {
  document.body.innerHTML = '<div style="padding:80px; color:#fff; text-align:center;">Concept not found.</div>';
  throw new Error('No concept for ' + key);
}

const accent = base.color || '#6b8cff';
document.documentElement.style.setProperty('--accent', accent);
document.title = `${base.name} · Unofficial presentation concept`;

const put = (id, value) => {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
};

put('type', base.type);
put('headline', base.headline.replace(base.short, `<span>${base.short}</span>`));
put('intro', base.intro);
put('aboutTitle', base.name);
put('aboutText', base.about);
put('sourceNote', base.source);
put('impactTitle', base.impact);
put('impactText', base.impactText);
put('quote', base.quote);
put('footerName', base.name);

// Headline may contain HTML
const headlineEl = document.getElementById('headline');
if (headlineEl) {
  headlineEl.innerHTML = base.headline.replace(
    new RegExp(`(${base.short}|${base.name.split(' ').slice(-1)[0]})`, 'i'),
    '<span>$1</span>'
  );
}

const cardsEl = document.getElementById('cards');
if (cardsEl && base.programs) {
  cardsEl.innerHTML = base.programs.map((x, i) => `
    <article class="card">
      <div class="card-num">0${i + 1}</div>
      <h3>${x[0]}</h3>
      <p>${x[1]}</p>
    </article>
  `).join('');
}

const tagsEl = document.getElementById('tags');
if (tagsEl && base.tags) {
  tagsEl.innerHTML = base.tags.map(x => `<span>${x}</span>`).join('');
}

const emailLink = document.getElementById('emailLink');
const contactLink = document.getElementById('contactLink');
if (emailLink && base.email) emailLink.href = `mailto:${base.email}`;
if (contactLink && base.email) {
  contactLink.href = `mailto:${base.email}`;
  contactLink.textContent = `Contact ${base.short}`;
}

// Reveal on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('in-view');
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
