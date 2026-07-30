const query=document.querySelector('#query');
const cards=[...document.querySelectorAll('#resourceGrid article')];
const checks=[...document.querySelectorAll('.filters input')];
const count=document.querySelector('#resultCount');
const empty=document.querySelector('#empty');
let audience='all';

function filter(){
  const term=query.value.toLowerCase().trim();
  const selected=checks.filter(input=>input.checked).map(input=>input.value);
  let visible=0;
  cards.forEach(card=>{
    const tags=card.dataset.tags;
    const text=card.textContent.toLowerCase();
    const matchesTerm=!term||text.includes(term)||tags.includes(term.replaceAll(' ','-'));
    const matchesFilters=!selected.length||selected.every(value=>tags.includes(value));
    const matchesAudience=audience==='all'||tags.includes(audience)||tags.includes('all');
    const show=matchesTerm&&matchesFilters&&matchesAudience;
    card.hidden=!show;if(show)visible++;
  });
  count.textContent=visible;empty.hidden=visible!==0;
}
checks.forEach(input=>input.addEventListener('change',filter));
query.addEventListener('input',filter);
document.querySelector('#searchButton').addEventListener('click',filter);
document.querySelectorAll('[data-query]').forEach(button=>button.addEventListener('click',()=>{query.value=button.dataset.query;filter()}));
document.querySelectorAll('[data-audience]').forEach(button=>button.addEventListener('click',()=>{audience=button.dataset.audience;document.querySelectorAll('[data-audience]').forEach(item=>item.classList.toggle('active',item===button));filter()}));
function clear(){query.value='';audience='all';checks.forEach(input=>input.checked=false);document.querySelectorAll('[data-audience]').forEach(item=>item.classList.toggle('active',item.dataset.audience==='all'));filter()}
document.querySelector('#clear').addEventListener('click',clear);empty.querySelector('button').addEventListener('click',clear);
document.querySelector('#contrast').addEventListener('click',()=>document.body.classList.toggle('high-contrast'));
document.querySelector('[data-audience="all"]').classList.add('active');
