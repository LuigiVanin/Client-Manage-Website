let inputs = document.querySelectorAll("input");

inputs.forEach((i) => {
    i.addEventListener("focusin", (event) => {
        i.parentElement.classList.add("side-bar");
    });
    i.addEventListener("focusout", (event) => {
        i.parentElement.classList.remove("side-bar");
    });
});
