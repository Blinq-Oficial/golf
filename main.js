// Scroll Reveal via Intersection Observer
document.addEventListener('DOMContentLoaded', () => {
  const reveals = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Optional: Stop observing once revealed if you only want it to animate once
        // observer.unobserve(entry.target); 
      }
    });
  }, {
    root: null,
    rootMargin: '0px',
    threshold: 0.15 // Trigger when 15% of element is visible
  });

  reveals.forEach(reveal => {
    revealObserver.observe(reveal);
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
}

function closeModal() {
  modal.classList.remove('active');
  document.body.classList.remove('modal-open');
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
