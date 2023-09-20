// loader.js

// Function to show the loader
function showLoader() {
    // Create a loader element
    var loader = document.createElement('div');
    loader.className = 'loader';
    document.body.appendChild(loader);

    // Optionally, you can add a loading message
    var loadingMessage = document.createElement('div');
    loadingMessage.className = 'loading-message';
    loadingMessage.innerText = 'Loading...';
    loader.appendChild(loadingMessage);

    // Disable scrolling while the loader is displayed
    document.body.style.overflow = 'hidden';
}

// Add an event listener to the Sign Up link
document.getElementById('signup-link').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the default link behavior (page navigation)

    // Show the loader
    showLoader();

    // Redirect to the Sign Up page after a delay (for demonstration purposes)
    setTimeout(function () {
        window.location.href = event.target.href;
    }, 2000); // Delay in milliseconds (2 seconds in this example)
});

// Add an event listener to the Sign In link
document.getElementById('signin-link').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the default link behavior (page navigation)

    // Show the loader
    showLoader();

    // Redirect to the Sign In page after a delay (for demonstration purposes)
    setTimeout(function () {
        window.location.href = event.target.href;
    }, 2000); // Delay in milliseconds (2 seconds in this example)
});
