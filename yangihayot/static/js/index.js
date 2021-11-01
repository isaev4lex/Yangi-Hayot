document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.querySelector('#hamburger'),
    mobile = document.querySelector('#mobile'),
    blur = document.querySelector('#blur');

  hamburger.addEventListener('click', () => {
    blur.classList.toggle('hidden');
    blur.classList.toggle('fixed');
    mobile.classList.toggle('hidden');
  });

  blur.addEventListener('click', () => {
    blur.classList.toggle('hidden');
    blur.classList.toggle('fixed');
    mobile.classList.toggle('hidden');
  });
});
