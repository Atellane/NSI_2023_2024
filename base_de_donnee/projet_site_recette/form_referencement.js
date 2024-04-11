function afficherOuMasquer(formulaire) {
    array = document.getElementsByClassName("livre");
    if (formulaire.value === "oui") {
        for (let index = 0; index < array.length; index++) {
            array[index].style.display = "block";
            array[index].setAttribute("required", "required");
        }
    } else {
        for (let index = 0; index < array.length; index++) {
            array[index].style.display = "none";
            array[index].removeAttribute("required");
        }
    }
};