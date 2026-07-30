const concepts = [
  ['01','North Sea Modern','northsea'], ['02','Highland Editorial','editorial'],
  ['03','Civic Commons','civic'], ['04','Archive Ledger','ledger'],
  ['05','Gallery Quiet','gallery'], ['06','River Signal','river'],
  ['07','Field Notes','field'], ['08','Modernist Museum','modernist'],
  ['09','Kinship','kinship'], ['10','Northern Light','northern'],
  ['11','Public Programme','programme-view'], ['12','Stone & Sea','stone'],
  ['13','Living Archive','living'], ['14','Highland Signal','signal'],
  ['15','Open Institution','open']
];

const stage = document.querySelector('#stage');
const template = document.querySelector('#site-template');
const menu = document.querySelector('#menu');
const counter = document.querySelector('#counter');
const menuButton = document.querySelector('#viewMenu');
let current = Math.max(0, Math.min(concepts.length - 1, Number(location.hash.replace('#view-','')) - 1 || 0));

concepts.forEach(([number,name,slug], index) => {
  const panel = template.content.firstElementChild.cloneNode(true);
  panel.classList.add(slug);
  panel.dataset.index = index;
  panel.querySelector('.concept-tag b').textContent = `VIEW ${number}`;
  panel.querySelector('.concept-tag span').textContent = name;
  stage.append(panel);
  const button = document.createElement('button');
  button.type = 'button';
  button.innerHTML = `<b>${number}</b><span>${name}</span>`;
  button.addEventListener('click', () => show(index));
  menu.append(button);
});

function show(index, updateHash = true) {
  current = (index + concepts.length) % concepts.length;
  document.querySelectorAll('.site-view').forEach((view, i) => view.classList.toggle('active', i === current));
  [...menu.children].forEach((button, i) => button.classList.toggle('active', i === current));
  counter.textContent = `${concepts[current][0]} / 15`;
  menu.classList.remove('open');
  menuButton.setAttribute('aria-expanded','false');
  if (updateHash) history.replaceState(null,'',`#view-${current + 1}`);
  stage.scrollTo({top:0,behavior:'instant'});
  document.title = `${concepts[current][1]} — Timespan Display Views`;
}

document.querySelector('#previous').addEventListener('click', () => show(current - 1));
document.querySelector('#next').addEventListener('click', () => show(current + 1));
menuButton.addEventListener('click', () => {
  const open = menu.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
});
document.addEventListener('keydown', event => {
  if (event.key === 'ArrowRight') show(current + 1);
  if (event.key === 'ArrowLeft') show(current - 1);
  if (event.key === 'Escape') menu.classList.remove('open');
});
show(current, false);
