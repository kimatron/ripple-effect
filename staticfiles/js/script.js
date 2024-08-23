document.addEventListener('DOMContentLoaded', function () {
  const menuIcon = document.getElementById('menu-icon');
  const navMenu = document.querySelector('.nav-menu');

  menuIcon.addEventListener('click', function () {
    menuIcon.classList.toggle('active');
    navMenu.classList.toggle('active');
  });

  // Close menu when a nav link is clicked
  document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
    menuIcon.classList.remove('active');
    navMenu.classList.remove('active');
  }));
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