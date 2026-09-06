// ===== LOADER =====
window.addEventListener('load', () => {
  setTimeout(() => document.getElementById('loader').classList.add('done'), 1200);
});

// ===== MOBILE DETECTION =====
const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) || window.innerWidth < 769;

// ===== CURSOR GLOW (desktop only) =====
if (!isMobile) {
  const glow = document.getElementById('cursorGlow');
  if (glow) {
    document.addEventListener('mousemove', e => {
      glow.style.left = e.clientX + 'px';
      glow.style.top = e.clientY + 'px';
    });
  }
}

// ===== NAVBAR SOLID ON SCROLL =====
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('solid', window.scrollY > 60);
});

// ===== HAMBURGER MENU =====
const burger = document.getElementById('hamburger');
const nLinks = document.getElementById('navLinks');
burger.addEventListener('click', () => {
  burger.classList.toggle('open');
  nLinks.classList.toggle('open');
});
nLinks.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    burger.classList.remove('open');
    nLinks.classList.remove('open');
  });
});

// ===== SCROLL REVEAL =====
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

// ===== PARTICLES (desktop only, reduced count) =====
if (!isMobile) {
  const pc = document.getElementById('particles');
  if (pc) {
    const count = window.innerWidth < 1024 ? 10 : 18;
    for (let i = 0; i < count; i++) {
      const p = document.createElement('div');
      p.classList.add('particle');
      p.style.left = Math.random() * 100 + '%';
      p.style.animationDuration = (8 + Math.random() * 10) + 's';
      p.style.animationDelay = Math.random() * 8 + 's';
      const size = (2 + Math.random() * 3) + 'px';
      p.style.width = size;
      p.style.height = size;
      p.style.boxShadow = '0 0 ' + (4 + Math.random() * 8) + 'px rgba(37, 99, 235, 0.3)';
      pc.appendChild(p);
    }
  }
}

// ===== ANIMATED COUNTERS =====
const counters = document.querySelectorAll('[data-target]');
const counterObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.getAttribute('data-target'));
      if (el.dataset.counted) return;
      el.dataset.counted = 'true';
      let current = 0;
      const increment = target / 40;
      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          current = target;
          clearInterval(timer);
        }
        // اگر عدد هدف بزرگتر از ۱۰۰۰ باشه، به صورت K نشون بده
        if (target >= 1000) {
            el.textContent = Math.floor(current / 1000) + 'K+';
        } else {
            el.textContent = Math.floor(current) + '+';
        }
      }, 40);
      counterObs.unobserve(el);
    }
  });
}, { threshold: 0.5 });
counters.forEach(c => counterObs.observe(c));

// ===== CONTACT FORM =====
function handleSubmit(e) {
  e.preventDefault();
  const btn = e.target.querySelector('button');
  btn.textContent = '\u2713 پیام شما ارسال شد';
  btn.style.background = 'linear-gradient(135deg, #25d366, #128c7e)';
  setTimeout(() => {
    btn.textContent = 'ارسال پیام';
    btn.style.background = '';
    e.target.reset();
  }, 3000);
}

// ===== SMOOTH SCROLL =====
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', function(e) {
    e.preventDefault();
    const t = document.querySelector(this.getAttribute('href'));
    if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

