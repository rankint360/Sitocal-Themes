const motion = matchMedia('(prefers-reduced-motion: reduce)');
const dialog = document.querySelector('.preview-dialog');
const fullFrame = dialog.querySelector('iframe');
dialog.addEventListener('close', () => fullFrame.removeAttribute('src'));

for (const card of document.querySelectorAll('[data-preview]')) {
  const viewport = card.querySelector('.preview-window');
  const number = card.querySelector('.section-number');
  const sectionName = card.querySelector('.section-name');
  const title = card.querySelector('h2').textContent;
  let frame, active = false, animation = 0, sections = [], started;

  function resize() {
    if (frame) frame.style.transform = `scale(${viewport.clientWidth / 1100})`;
  }

  function scroll(time) {
    if (!active || !frame.contentDocument) return;
    const page = frame.contentWindow;
    const max = Math.max(0, frame.contentDocument.documentElement.scrollHeight - 700);
    started ??= time;
    const offset = motion.matches ? 0 : Math.min(max, Math.max(0, time - started - 350) * .17);
    page.scrollTo({top: offset, behavior: 'instant'});
    const index = Math.max(0, sections.findLastIndex(item => item.top <= offset + 220));
    number.textContent = String(index + 1).padStart(2, '0');
    sectionName.textContent = sections[index]?.name || 'Homepage';
    if (!motion.matches && offset < max) animation = requestAnimationFrame(scroll);
  }

  function play() {
    if (!active || !frame.contentDocument) return;
    cancelAnimationFrame(animation);
    started = undefined;
    sections = [...frame.contentDocument.querySelectorAll('main h1, main h2')]
      .map(heading => ({
        name: heading.textContent.trim().replace(/\s+/g, ' '),
        top: heading.getBoundingClientRect().top + frame.contentWindow.scrollY
      })).filter(item => item.name);
    viewport.classList.add('ready');
    number.hidden = sectionName.hidden = false;
    animation = requestAnimationFrame(scroll);
  }

  function start() {
    if (active) return;
    active = true;
    card.classList.add('previewing');
    if (!frame) {
      frame = document.createElement('iframe');
      frame.title = `${title} homepage mockup`;
      frame.tabIndex = -1;
      frame.setAttribute('aria-hidden', 'true');
      frame.setAttribute('sandbox', 'allow-same-origin');
      frame.addEventListener('load', play);
      frame.src = card.dataset.preview;
      viewport.append(frame);
      resize();
    } else if (viewport.classList.contains('ready') || frame.contentDocument?.readyState === 'complete') {
      play();
    }
  }

  function stop() {
    active = false;
    cancelAnimationFrame(animation);
    card.classList.remove('previewing');
    number.hidden = sectionName.hidden = true;
  }

  new ResizeObserver(resize).observe(viewport);
  card.addEventListener('pointerenter', event => { if (event.pointerType !== 'touch') start(); });
  card.addEventListener('pointerleave', () => { if (!card.contains(document.activeElement)) stop(); });
  card.addEventListener('focusin', start);
  card.addEventListener('focusout', event => {
    if (!card.contains(event.relatedTarget) && !card.matches(':hover')) stop();
  });
  card.querySelector('[data-full]').onclick = () => {
    document.getElementById('preview-title').textContent = title;
    fullFrame.src = card.dataset.preview;
    dialog.showModal();
  };
}
