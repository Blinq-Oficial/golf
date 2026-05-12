// Initialize Lenis Smooth Scroll
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1,
  smoothTouch: false,
  touchMultiplier: 2,
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// Magnetic Buttons
const magneticElements = document.querySelectorAll('.magnetic');

magneticElements.forEach((elem) => {
  elem.addEventListener('mousemove', (e) => {
    const { left, top, width, height } = elem.getBoundingClientRect();
    const x = e.clientX - left - width / 2;
    const y = e.clientY - top - height / 2;
    
    // Magnetic pull
    elem.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
    
    // Optional: inner text parallax
    const text = elem.querySelector('.magnetic-text');
    if (text) {
      text.style.transform = `translate(${x * 0.2}px, ${y * 0.2}px)`;
    }
  });

  elem.addEventListener('mouseleave', () => {
    elem.style.transform = 'translate(0px, 0px)';
    const text = elem.querySelector('.magnetic-text');
    if (text) {
      text.style.transform = 'translate(0px, 0px)';
    }
  });
});

// Scroll Reveal via Intersection Observer (Staggered)
document.addEventListener('DOMContentLoaded', () => {
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // observer.unobserve(entry.target); // keep active to re-trigger if desired, but Aman/Macallan usually only animate once. We'll leave it to re-trigger for demo purposes.
      } else {
        // Optional: remove class when out of view to replay animation
        // entry.target.classList.remove('active');
      }
    });
  }, {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  });

  revealElements.forEach(reveal => {
    revealObserver.observe(reveal);
  });

  // Staggered Reveal for Grid items
  const staggerContainers = document.querySelectorAll('.stagger-container');
  
  staggerContainers.forEach(container => {
    const items = container.querySelectorAll('.stagger-item');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          items.forEach((item, index) => {
            setTimeout(() => {
              item.classList.add('active');
            }, index * 150); // 150ms stagger
          });
          observer.unobserve(container);
        }
      });
    }, { threshold: 0.2 });
    
    observer.observe(container);
  });

  // Navbar Scroll Effect
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
});

// Modal Logic
const modal = document.getElementById('contactModal');

function openModal() {
  modal.classList.add('active');
  document.body.classList.add('modal-open');
  lenis.stop(); // Stop scroll when modal is open
}

function closeModal() {
  modal.classList.remove('active');
  document.body.classList.remove('modal-open');
  lenis.start(); // Resume scroll
}

// Close modal on outside click
modal.addEventListener('click', (e) => {
  if (e.target === modal) {
    closeModal();
  }
});

// Form submission simulation
function submitForm(e) {
  e.preventDefault();
  const btn = e.target.querySelector('button[type="submit"]');
  const originalText = btn.innerHTML;
  
  btn.innerHTML = 'Procesando...';
  btn.style.pointerEvents = 'none';

  setTimeout(() => {
    btn.innerHTML = '¡Solicitud Enviada!';
    btn.style.backgroundColor = 'var(--color-primary-light)';
    
    setTimeout(() => {
      closeModal();
      e.target.reset();
      btn.innerHTML = originalText;
      btn.style.pointerEvents = 'auto';
      btn.style.backgroundColor = ''; // Reset to default CSS
    }, 2000);
  }, 1500);
}
