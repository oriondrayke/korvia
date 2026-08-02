const header = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-button');
const nav = document.querySelector('#primary-nav');

menuButton.addEventListener('click', () => {
  const open = header.classList.toggle('menu-open');
  menuButton.setAttribute('aria-expanded', String(open));
});

nav.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    header.classList.remove('menu-open');
    menuButton.setAttribute('aria-expanded', 'false');
  });
});

const audienceContent = {
  patient: {
    label: 'For patients',
    title: 'You do not have to carry the emotional weight of cancer alone.',
    copy: 'Learn what psycho-oncology support can include, prepare questions for your care team, and understand when emotional distress deserves professional attention.',
    action: 'View a proposed support pathway',
    points: [
      'Understanding common emotional responses',
      'Preparing to speak with a care professional',
      'Finding verified local services as the network grows',
    ],
  },
  caregiver: {
    label: 'For caregivers',
    title: 'Supporting someone should not mean becoming invisible yourself.',
    copy: 'Find practical guidance for caregiver strain, difficult conversations, grief, treatment routines and asking family or professionals for support.',
    action: 'Explore caregiver support concepts',
    points: [
      'Recognising exhaustion and emotional distress',
      'Preparing for difficult care conversations',
      'Finding support for your own wellbeing',
    ],
  },
  professional: {
    label: 'For professionals',
    title: 'Build psycho-oncology skills into everyday cancer care.',
    copy: 'Connect with training, emerging practice resources, peer learning and a multidisciplinary professional network working across Uganda.',
    action: 'Explore the professional pathway',
    points: [
      'Training and continuing professional learning',
      'Practice tools and Ugandan research',
      'Membership and multidisciplinary connection',
    ],
  },
};

const tabs = [...document.querySelectorAll('[data-audience]')];
const audiencePanel = document.querySelector('#panel-audience');
const label = document.querySelector('#audience-label');
const title = document.querySelector('#audience-title');
const copy = document.querySelector('#audience-copy');
const action = document.querySelector('#audience-action');
const pointList = document.querySelector('#audience-points');

function selectAudience(key) {
  const content = audienceContent[key];
  tabs.forEach((tab) => tab.setAttribute('aria-selected', String(tab.dataset.audience === key)));
  audiencePanel.setAttribute('aria-labelledby', `tab-${key}`);
  label.textContent = content.label;
  title.textContent = content.title;
  copy.textContent = content.copy;
  action.textContent = content.action;
  pointList.innerHTML = content.points.map((point, index) => `<li><span>0${index + 1}</span>${point}</li>`).join('');
}

tabs.forEach((tab) => {
  tab.addEventListener('click', () => selectAudience(tab.dataset.audience));
  tab.addEventListener('keydown', (event) => {
    if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
    event.preventDefault();
    const current = tabs.indexOf(tab);
    const offset = event.key === 'ArrowRight' ? 1 : -1;
    const next = tabs[(current + offset + tabs.length) % tabs.length];
    next.focus();
    selectAudience(next.dataset.audience);
  });
});

const filterButtons = [...document.querySelectorAll('[data-filter]')];
const resourceCards = [...document.querySelectorAll('[data-resource]')];

filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filterButtons.forEach((item) => item.classList.toggle('active', item === button));
    resourceCards.forEach((card) => {
      const categories = card.dataset.resource.split(' ');
      card.hidden = filter !== 'all' && !categories.includes(filter);
    });
  });
});

const supportModal = document.querySelector('#support-modal');
const membershipModal = document.querySelector('#membership-modal');

document.querySelectorAll('[data-open-support]').forEach((button) => {
  button.addEventListener('click', () => supportModal.showModal());
});

document.querySelectorAll('[data-open-membership]').forEach((button) => {
  button.addEventListener('click', () => membershipModal.showModal());
});

document.querySelectorAll('[data-close-modal]').forEach((button) => {
  button.addEventListener('click', () => button.closest('dialog').close());
});

[supportModal, membershipModal].forEach((modal) => {
  modal.addEventListener('click', (event) => {
    if (event.target === modal) modal.close();
  });
});

document.querySelector('#membership-form').addEventListener('submit', (event) => event.preventDefault());
