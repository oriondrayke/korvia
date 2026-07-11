/* Korvia shared UI behaviors — theme switcher and sliding options panel */

(function () {
    const STORAGE_KEY = 'korvia-theme';

    function initTheme() {
        const switcher = document.getElementById('kv-theme-switch');
        if (!switcher) return;

        const slider = switcher.querySelector('.kv-theme-slider');
        const options = switcher.querySelectorAll('.kv-theme-option');

        function positionSlider(value) {
            const active = switcher.querySelector(`[data-value="${value}"]`);
            if (!active || !slider) return;
            slider.style.left = active.offsetLeft + 'px';
            slider.style.width = active.offsetWidth + 'px';
        }

        function setTheme(value) {
            if (value === 'auto') {
                document.documentElement.removeAttribute('data-theme');
                localStorage.removeItem(STORAGE_KEY);
            } else {
                document.documentElement.setAttribute('data-theme', value);
                localStorage.setItem(STORAGE_KEY, value);
            }
            options.forEach(btn => btn.classList.toggle('active', btn.dataset.value === value));
            positionSlider(value);
        }

        const saved = localStorage.getItem(STORAGE_KEY) || 'auto';
        setTheme(saved);
        window.addEventListener('resize', () => positionSlider(saved));

        options.forEach(btn => {
            btn.addEventListener('click', () => setTheme(btn.dataset.value));
        });
    }

    function initOptionsPanel() {
        const toggle = document.getElementById('kv-options-toggle');
        const close = document.getElementById('kv-options-close');
        const panel = document.getElementById('kv-options-panel');
        const backdrop = document.getElementById('kv-options-backdrop');

        if (!panel) return;

        function open(opened) {
            panel.classList.toggle('open', opened);
            if (backdrop) backdrop.classList.toggle('open', opened);
        }

        if (toggle) toggle.addEventListener('click', () => open(true));
        if (close) close.addEventListener('click', () => open(false));
        if (backdrop) backdrop.addEventListener('click', () => open(false));
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            initTheme();
            initOptionsPanel();
        });
    } else {
        initTheme();
        initOptionsPanel();
    }
})();
