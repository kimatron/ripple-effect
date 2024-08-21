document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');

  hamburger.addEventListener('click', function () {
    navLinks.classList.toggle('active');
  });
});



document.addEventListener('DOMContentLoaded', function () {
  // Parallax scrolling effect
  window.addEventListener('scroll', function () {
    let heroSection = document.querySelector('.hero-section');
    let scrollPosition = window.pageYOffset;

    heroSection.style.backgroundPositionY = 50 + scrollPosition * 0.5 + '%';
  });

  // Smooth scroll-down animation
  let scrollDownButton = document.querySelector('.scroll-down');
  scrollDownButton.addEventListener('click', function (e) {
    e.preventDefault();
    let aboutSection = document.getElementById('about');
    aboutSection.scrollIntoView({
      behavior: 'smooth'
    });
  });
});