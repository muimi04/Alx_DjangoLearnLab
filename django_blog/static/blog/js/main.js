// blog/static/blog/js/main.js

// A simple script to show a welcome message in the console
document.addEventListener("DOMContentLoaded", function() {
    console.log("Welcome to Django Blog!");

    // Example: Highlight all links on hover
    let links = document.querySelectorAll("nav a");
    links.forEach(link => {
        link.addEventListener("mouseenter", () => {
            link.style.color = "#f39c12";  // orange
        });
        link.addEventListener("mouseleave", () => {
            link.style.color = "white";
        });
    });
});
