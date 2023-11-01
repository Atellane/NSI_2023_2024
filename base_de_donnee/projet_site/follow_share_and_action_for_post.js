function follow(obj) {    
    if (obj.className === "followButton") {
        // Redirigez l'utilisateur vers signIn.php
        window.location.href = "./accounts/sign_in.html";
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
    var postId = obj.parentNode.parentNode.parentNode.parentNode.parentNode.id
    console.log(postId);
    
    if (obj.className === "shareButton") {
        // Redirigez l'utilisateur vers signIn.php
        window.location.href = "./accounts/sign_in.html";
        return; // Sortez de la fonction pour éviter l'exécution du reste du code
    }
    
    // Send an AJAX request to the PHP file when the button is clicked
    if (obj.classList.contains("shared")) {
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

function afficherPreviewImage(input, className) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $(className + ' img')
          .attr('src', e.target.result);
      };
      reader.readAsDataURL(input.files[0]);
    }  else {
        $(className + " img").attr("src", "");
    }
  }

function soumettreCommentaire(obj) {
    // get the form object's data
    var postId = obj.parentNode.parentNode.parentNode.parentNode.parentNode.id;
    var commentaire = new FormData(obj.parentNode.querySelector(".commentForm"));
    commentaire.append("idDuPost", postId);
    // -------------------------------------------
    // for your information:
    // this is the format of what we are sending over
    // -------------------------------------------
    obj.parentNode.parentNode.querySelector("footer").querySelector(".commentPreview").querySelector("span").innerText = commentaire.get("texteCommentaire");
    afficherPreviewImage(obj.parentNode.querySelector('.commentForm').querySelector(".imageCommentaire"), ".commentPreview");
    // -------------------------------------------

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

            // -------------------------------------------
            console.log("Signal sent successfully.");
            console.log("Response from PHP: " + response);
        },
        error: function (xhr, status, error) {
        // Handle errors if the request fails
        console.error("Error: " + error);
        }
   });
   
   obj.parentNode.querySelector('.commentForm').reset();
};

function soumettreModification(obj) {
    // get the form object's data
    var postId = obj.parentNode.parentNode.parentNode.parentNode.id;
    var modification = new FormData(obj.parentNode.querySelector(".modifForm"));
    modification.append("idDuPost", postId);
    // -------------------------------------------
    // for your information:
    // this is the format of what we are sending over
    // -------------------------------------------
    obj.parentNode.parentNode.querySelector("footer").querySelector(".modifPreview").querySelector("span").innerText = modification.get("texteModification");
    afficherPreviewImage(obj.parentNode.querySelector('.modifForm').querySelector(".imageModification"), ".modifPreview");
    // -------------------------------------------

    $.ajax({
        url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/posts/modify_a_post.php",
        type: "POST",
        data: modification,
        contentType: false,
        processData: false,
        success: function(data, response) {
            // -------------------------------------------
            // for your information:
            // just show what we got back from the server
            // -------------------------------------------

            // -------------------------------------------
            console.log("Signal sent successfully.");
            console.log("Response from PHP: " + response);
        },
        error: function (xhr, status, error) {
        // Handle errors if the request fails
        console.error("Error: " + error);
        }
   });
   
   obj.parentNode.querySelector('.modifForm').reset();
};

function ouvrirCommentaire(obj) {
    if (obj.className === "commentButton") {
        // Redirigez l'utilisateur vers signIn.php
        window.location.href = "./accounts/sign_in.html";
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