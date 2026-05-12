// ── Lenis Smooth Scroll ──
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// ── Scroll Reveal (Staggered Cascade) ──
document.addEventListener('DOMContentLoaded', () => {
  const reveals = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, { root: null, rootMargin: '0px', threshold: 0.12 });

  reveals.forEach(el => revealObserver.observe(el));

  // ── Navbar Scroll ──
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 60);
  });

  // ── Parallax on scroll ──
  const parallaxEls = document.querySelectorAll('[data-parallax]');
  if (parallaxEls.length) {
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      parallaxEls.forEach(el => {
        const speed = parseFloat(el.dataset.parallax) || 0.2;
        el.style.transform = `translateY(${scrollY * speed}px) scale(1.1)`;
      });
    }, { passive: true });
  }

  // ── Magnetic Buttons ──
  const magneticWraps = document.querySelectorAll('.magnetic-wrap');
  magneticWraps.forEach(wrap => {
    const btn = wrap.querySelector('.btn');
    if (!btn) return;

    wrap.addEventListener('mousemove', (e) => {
      const rect = wrap.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
    });

    wrap.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0, 0)';
      btn.style.transition = 'transform 400ms cubic-bezier(0.23, 1, 0.32, 1)';
      setTimeout(() => { btn.style.transition = ''; }, 400);
    });

    wrap.addEventListener('mouseenter', () => {
      btn.style.transition = 'none';
    });
  });
});

// ── Modal ──
const modal = document.getElementById('contactModal');

function openModal() {
  modal.classList.add('active');
  document.body.classList.add('modal-open');
}

function closeModal() {
  modal.classList.remove('active');
  document.body.classList.remove('modal-open');
}

modal.addEventListener('click', (e) => {
  if (e.target === modal) closeModal();
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
});

// ── Form ──
function submitForm(e) {
  e.preventDefault();
  const btn = e.target.querySelector('button[type="submit"]');
  const orig = btn.innerHTML;
  btn.innerHTML = 'Procesando...';
  btn.style.pointerEvents = 'none';

  setTimeout(() => {
    btn.innerHTML = '¡Solicitud Enviada!';
    setTimeout(() => {
      closeModal();
      e.target.reset();
      btn.innerHTML = orig;
      btn.style.pointerEvents = 'auto';
    }, 2000);
  }, 1500);
}
