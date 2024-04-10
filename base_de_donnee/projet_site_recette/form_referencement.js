function afficherOuMasquer(formulaire) {
    array = document.getElementsByClassName("livre");
    if (formulaire.value === "oui") {
        for (let index = 0; index < array.length; index++) {
            array[index].style.display = "block";
        }
    } else {
        for (let index = 0; index < array.length; index++) {
            array[index].style.display = "none";
        }
    }
};