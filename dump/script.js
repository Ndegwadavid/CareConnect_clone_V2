// Fetch news data from an API
fetch('https://api.thunder.com/news') //to be determined which api 
  .then(response => response.json())
  .then(data => {
    const newsContainer = document.getElementById('news-container');
    data.articles.forEach(article => {
      const newsItem = document.createElement('div');
      newsItem.innerHTML = `
        <h3>${article.title}</h3>
        <p>${article.description}</p>
        <a href="${article.url}" target="_blank">Read more</a>
      `;
      newsContainer.appendChild(newsItem);
    });
  })
  .catch(error => console.error(error));

// Slideshow functionality
let slideIndex = 0;
showSlides();

function showSlides() {
  const slides = document.getElementsByClassName('slide');
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = 'block';
  setTimeout(showSlides, 3000);
}