
const navbarDropdown = document.querySelector(".navbar-dropdown");
const hamButton = document.querySelector(".ham-button")

function toggleMenu() {
    if(navbarDropdown.classList.contains("menu-click")) {
        navbarDropdown.classList.remove("menu-click");
    } else {
        navbarDropdown.classList.add("menu-click");
    }
}

hamButton.addEventListener("click", toggleMenu);
