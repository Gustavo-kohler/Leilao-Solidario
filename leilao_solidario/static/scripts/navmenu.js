
const dropdown = document.querySelector(".navbar-dropdown");
const button = document.querySelector(".ham-button")

function toggleMenu() {
    if(dropdown.classList.contains("menu-click")) {
        dropdown.classList.remove("menu-click");
    } else {
        dropdown.classList.add("menu-click");
    }
}

button.addEventListener("click", toggleMenu);
