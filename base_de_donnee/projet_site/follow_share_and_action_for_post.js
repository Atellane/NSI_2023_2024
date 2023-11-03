function follow(obj) {    
    if (obj.className === "followButton") {
        // Redirigez l'utilisateur vers signIn.php
        window.location.href = "/2023-2024-terminales-NSI/leouzan/accounts/sign_in.php";
        return; // Sortez de la fonction pour éviter l'exécution du reste du code
    }
    
    // Send an AJAX request to the PHP file when the button is clicked
    if (obj.classList.contains("followed")) {
        obj.classList.remove("followed");
        $.ajax({
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/follow.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "remove",
                abonnement: obj.id
            },
            success: function (response) {
                // Handle the response from the PHP file if needed
                console.log("Signal sent successfully.");
                console.log("Response from PHP: " + response);
            },
            error: function (xhr, status, error) {
                // Handle errors if the request fails
                console.error("Error: " + error);
            }
        });
    } else {
        $.ajax({
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/follow.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "create",
                abonnement: obj.id
            },
            success: function (response) {
                // Handle the response from the PHP file if needed
                console.log("Signal sent successfully.");
                console.log("Response from PHP: " + response);
            },
            error: function (xhr, status, error) {
                // Handle errors if the request fails
                console.error("Error: " + error);
            }
        });
        obj.classList.add("followed");
    }
};

function share(obj) {
    let postId = obj.parentNode.parentNode.parentNode.parentNode.parentNode.id;


    if (obj.className === "shareButton") {
        // Redirigez l'utilisateur vers signIn.php
        window.location.href = "/2023-2024-terminales-NSI/leouzan/accounts/sign_in.php";
        return; // Sortez de la fonction pour éviter l'exécution du reste du code
    }

    // Send an AJAX request to the PHP file when the button is clicked
    if (obj.classList.contains("shared")) {
        let pElement = obj.parentNode.querySelector(":scope > p");
        let currentValue = parseInt(pElement.innerText); // Récupérer la valeur actuelle en tant qu'entier

        if (!isNaN(currentValue)) {
            pElement.innerText = currentValue - 1; // Incrémenter la valeur et la mettre à jour dans l'élément p
        }

        obj.classList.remove("shared");
        $.ajax({
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/posts/share.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "remove",
                post: postId
            },
            success: function (response) {
                // Handle the response from the PHP file if needed
                console.log("Signal sent successfully.");
                console.log("Response from PHP: " + response);
            },
            error: function (xhr, status, error) {
                // Handle errors if the request fails
                console.error("Error: " + error);
            }
        });
    } else {
        let pElement = obj.parentNode.querySelector(":scope > p");
        let currentValue = parseInt(pElement.innerText); // Récupéclass='followButton'r la valeur actuelle en tant qu'entier

        if (!isNaN(currentValue)) {
            pElement.innerText = currentValue + 1; // Incrémenter la valeur et la mettre à jour dans l'élément p
        }

        $.ajax({
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/posts/share.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "create",
                post: postId
            },
            success: function (response) {
                // Handle the response from the PHP file if needed
                console.log("Signal sent successfully.");
                console.log("Response from PHP: " + response);
            },
            error: function (xhr, status, error) {
                // Handle errors if the request fails
                console.error("Error: " + error);
            }
        });
        obj.classList.add("shared");
    }
};

function afficherPreviewImage(input, imgElement) {
    if (input.name !== "") {
      var reader = new FileReader();
      reader.onload = function (e) {
        imgElement.src = e.target.result;
      };
      reader.readAsDataURL(input);
    } else {
        imgElement.src = "";
    }
  }

function soumettreCommentaire(obj) {
    let pElement = obj.parentNode.parentNode.parentNode.parentNode.querySelector(":scope > .postFooter > ul > li:not(.partage) > p");
    let currentValue = parseInt(pElement.innerText); // Récupérer la valeur actuelle en tant qu'entier

    if (!isNaN(currentValue)) {
        pElement.innerText = currentValue + 1; // Incrémenter la valeur et la mettre à jour dans l'élément p
    }

    // get the form object's data
    let postId = obj.parentNode.parentNode.parentNode.parentNode.parentNode.id;
    // Récupérer la date et l'heure actuelles
    const maintenant = new Date();
    // padStart sert à s'assurer que les chaines de caractères feront toujours 2 chiffres
    const jour = String(maintenant.getDate()).padStart(2, '0');
    const mois = String(maintenant.getMonth() + 1).padStart(2, '0');
    const annee = maintenant.getFullYear();
    const heures = String(maintenant.getHours()).padStart(2, '0');
    const minutes = String(maintenant.getMinutes()).padStart(2, '0');
    const secondes = String(maintenant.getSeconds()).padStart(2, '0');
    const datetime = `${jour}/${mois}/${annee} ${heures}:${minutes}:${secondes}`;
    let commentaire = new FormData(obj.parentNode.querySelector(".commentForm"));
    commentaire.append("idDuPost", postId);

    $.ajax({
        url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/posts/add_comment.php",
        type: "POST",
        data: commentaire,
        contentType: false,
        processData: false,
        success: function(data, response) {
            // -------------------------------------------
            // for your information:
            // just show what we got back from the server
            // -------------------------------------------
            commentId = reponse;
            // -------------------------------------------
            console.log("Signal sent successfully.");
            console.log("Response from PHP: " + response);
        },
        error: function (xhr, status, error) {
        // Handle errors if the request fails
        console.error("Error: " + error);
        }
   });
   let input = commentaire.get("imageCommentaire");
   let preview = obj.parentNode.parentNode.parentNode.querySelector(":scope > .preview");
   preview.classList.add("previewOuverte");
   preview.querySelector(":scope > header > ul > .datetime").innerText = datetime;
   if (input.name !== "") {
        if (preview.querySelector(":scope > .postContent > img") === null) {
            preview.querySelector(":scope > .postContent").innerHTML = '<img src="#" alt="imagePost" /> \
            <br /> \
            <p>#</p>';
        }
        afficherPreviewImage(input, preview.querySelector(":scope > .postContent > img"));
    } else {
        if (preview.querySelector(":scope > .postContent > img") !== null) {
            preview.querySelector(":scope > .postContent > img").remove();
            preview.querySelector(":scope > .postContent > br").remove();
        }
    }
    preview.querySelector(":scope > .postContent > p").innerText = commentaire.get("texteCommentaire");
   
   obj.parentNode.querySelector('.commentForm').reset();
};

function soumettreModification(obj) {
    // get the form object's data
    let post = obj.parentNode.parentNode.parentNode.parentNode;
    let postId = post.id;
    let modification = new FormData(obj.parentNode.querySelector(".modifForm"));
    modification.append("idDuPost", postId);
    // -------------------------------------------
    // for your information:
    // this is the format of what we are sending over
    // -------------------------------------------
    const maintenant = new Date();
    // padStart sert à s'assurer que les chaines de caractères feront toujours 2 chiffres
    const jour = String(maintenant.getDate()).padStart(2, '0');
    const mois = String(maintenant.getMonth() + 1).padStart(2, '0');
    const annee = maintenant.getFullYear();
    const heures = String(maintenant.getHours()).padStart(2, '0');
    const minutes = String(maintenant.getMinutes()).padStart(2, '0');
    const secondes = String(maintenant.getSeconds()).padStart(2, '0');
    const datetime = `${jour}/${mois}/${annee} ${heures}:${minutes}:${secondes}`;
    let input = modification.get("imageModification");
    post.querySelector(":scope > .postContent > p").innerText = modification.get("texteModification");
    post.querySelector(":scope > header > ul > .datetime").innerText = datetime;
    if (input.name !== "") {
        if (post.querySelector(":scope > .postContent > img") === null) {
            post.querySelector(":scope > .postContent").innerHTML = '<img src="#" alt="imagePost" /> \
            <br /> \
            <p>#</p>';
        }
        afficherPreviewImage(input, post.querySelector(":scope > .postContent > img"));
    } else {
        if (post.querySelector(":scope > .postContent > img") !== null) {
            post.querySelector(":scope > .postContent > img").remove();
            post.querySelector(":scope > .postContent > br").remove();
        }
    }
    // -------------------------------------------

//     $.ajax({
//         url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/posts/modify_a_post.php",
//         type: "POST",
//         data: modification,
//         contentType: false,
//         processData: false,
//         success: function(data, response) {
//             // -------------------------------------------
//             // for your information:
//             // just show what we got back from the server
//             // -------------------------------------------

//             // -------------------------------------------
//             console.log("Signal sent successfully.");
//             console.log("Response from PHP: " + response);
//         },
//         error: function (xhr, status, error) {
//         // Handle errors if the request fails
//         console.error("Error: " + error);
//         }
//    });
   
   obj.parentNode.querySelector('.modifForm').reset();
};

function ouvrirCommentaire(obj) {
    if (obj.className === "commentButton") {
        // Redirigez l'utilisateur vers signIn.php
        window.location.href = "/2023-2024-terminales-NSI/leouzan/accounts/sign_in.php";
        return; // Sortez de la fonction pour éviter l'exécution du reste du code
    }

    const commentSection = obj.parentNode.parentNode.parentNode.parentNode.querySelector(".comment");
    if (commentSection.classList.contains("comOuvert")) {
        commentSection.classList.remove("comOuvert");
    } else {
        commentSection.classList.add("comOuvert");
    }
};

function ouvrirModif(obj) {
    const commentSection = obj.parentNode.parentNode.parentNode.parentNode.querySelector(":scope > .modification");
    if (commentSection.classList.contains("modifOuverte")) {
        commentSection.classList.remove("modifOuverte");
    } else {
        commentSection.classList.add("modifOuverte");
    }
};

function supprimerPost(obj) {
    postId = obj.parentNode.parentNode.parentNode.parentNode.parentNode.id;
    $.ajax({
        url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/posts/delete_a_post.php",
        method: "POST", // or "GET" depending on your needs
        data: {
            post: postId
        },
        success: function (response) {
            // Handle the response from the PHP file if needed
            console.log("Signal sent successfully.");
            console.log("Response from PHP: " + response);
            window.location.reload();
        },
        error: function (xhr, status, error) {
            // Handle errors if the request fails
            console.error("Error: " + error);
        }
    });

};