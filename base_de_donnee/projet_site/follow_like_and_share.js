function follow(obj) {
    console.log(obj.id + " " + obj.className);
    
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
                abonne: obj.classList[1],
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
                abonne: obj.classList[1],
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

function like(obj) {
    console.log(obj.id + " " + obj.className);
    var postId = obj.parentNode.parentNode.parentNode.parentNode.parentNode.id
    console.log(postId);
    
    if (obj.className === "likeButton") {
        // Redirigez l'utilisateur vers signIn.php
        window.location.href = "./accounts/sign_in.html";
        return; // Sortez de la fonction pour éviter l'exécution du reste du code
    }
    
    // Send an AJAX request to the PHP file when the button is clicked
    if (obj.classList.contains("liked")) {
        obj.classList.remove("liked");
        obj.classList.add("unliked");
        $.ajax({
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/like.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "remove",
                user: obj.classList[1],
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
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/like.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "create",
                user: obj.classList[1],
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
        if (obj.classList.contains("unliked")) {
            obj.classList.remove("unliked");
        }
        obj.classList.add("liked");
    }
};

function share(obj) {
    console.log(obj.id + " " + obj.className);
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
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/share.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "remove",
                user: obj.classList[1],
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
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/share.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "create",
                user: obj.classList[1],
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

function afficherPreviewImage(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $('.commentPreview img')
          .attr('src', e.target.result);
      };
      reader.readAsDataURL(input.files[0]);
    } else {
        $(".commentPreview img").attr("src", "");
    }
  }

function soumettreCommentaire(obj) {
    // get the form object's data
    var postId = obj.parentNode.parentNode.parentNode.parentNode.parentNode.id;
    console.log(postId);
    var commentaire = new FormData(obj.parentNode.querySelector(".commentForm"));
    commentaire.append("idDuPost", postId);
    // -------------------------------------------
    // for your information:
    // this is the format of what we are sending over
    // -------------------------------------------
    obj.parentNode.parentNode.querySelector("footer").querySelector(".commentPreview").querySelector("span").innerText = commentaire.get("texteCommentaire");
    afficherPreviewImage(obj.parentNode.querySelector('.commentForm').querySelector(".imageCommentaire"));
    // -------------------------------------------

    $.ajax({
        url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/addComment.php",
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

function ouvrirCommentaire(obj) {
    const commentSection = obj.parentNode.parentNode.parentNode.parentNode.querySelector(".comment");
    if (commentSection.classList.contains("comOuvert")) {
        commentSection.classList.remove("comOuvert");
    } else {
        commentSection.classList.add("comOuvert");
    }
};

function ouvrirModification(obj) {
    const commentSection = obj.parentNode.parentNode.parentNode.parentNode.querySelector(".modification");
    if (commentSection.classList.contains("modifOuverte")) {
        commentSection.classList.remove("modifOuverte");
    } else {
        commentSection.classList.add("modifOuverte");
    }
};