// ===== فیلتر دسته‌بندی =====
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    
    const filter = btn.dataset.filter;
    document.querySelectorAll('.portfolio-page-card').forEach(card => {
      if (filter === 'all' || card.dataset.category === filter) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

// ===== اسلایدر =====
function slideNext(btn) {
  const slider = btn.closest('[data-slider]');
  const track = slider.querySelector('.portfolio-slider-track');
  const total = track.children.length;
  let current = parseInt(slider.dataset.current || 0);
  current = (current + 1) % total;
  slider.dataset.current = current;
  track.style.transform = `translateX(${current * 100}%)`;
  updateDots(slider, current);
}

function slidePrev(btn) {
  const slider = btn.closest('[data-slider]');
  const track = slider.querySelector('.portfolio-slider-track');
  const total = track.children.length;
  let current = parseInt(slider.dataset.current || 0);
  current = (current - 1 + total) % total;
  slider.dataset.current = current;
  track.style.transform = `translateX(${current * 100}%)`;
  updateDots(slider, current);
}

function slideTo(dot, index) {
  const slider = dot.closest('[data-slider]');
  const track = slider.querySelector('.portfolio-slider-track');
  slider.dataset.current = index;
  track.style.transform = `translateX(${index * 100}%)`;
  updateDots(slider, index);
}

function updateDots(slider, current) {
  const dots = slider.querySelectorAll('.portfolio-slider-dots span');
  dots.forEach((dot, i) => {
    dot.classList.toggle('active', i === current);
  });
}