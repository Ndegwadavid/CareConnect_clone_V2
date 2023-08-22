// Hover Effects

const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(dropdown => {

  dropdown.addEventListener('mouseover', () => {
    dropdown.querySelector('.dropdown-menu').style.display = 'block';
  });

  dropdown.addEventListener('mouseout', () => {
    dropdown.querySelector('.dropdown-menu').style.display = 'none';
  });

});

const doctorProfiles = document.querySelectorAll('.doctor-profile');

doctorProfiles.forEach(profile => {

  profile.addEventListener('mouseover', () => {
    profile.style.transform = 'scale(1.1)';
  });
  
  profile.addEventListener('mouseout', () => {
    profile.style.transform = 'scale(1)';
  });

});
// Slideshow 

let slideIndex = 0;
const slides = document.querySelectorAll('.slideshow img');

function showSlides() {

  slides[slideIndex].style.opacity = 0;
  
  slideIndex++;
  
  if (slideIndex >= slides.length) {
    slideIndex = 0; 
  }
  
  slides[slideIndex].style.opacity = 1;

  setTimeout(showSlides, 2000); // transition time
}

window.addEventListener('load', showSlides);