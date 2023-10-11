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
                abonne: obj.className,
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
                abonne: obj.className,
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
    var postId = obj.parentNode.parentNode.parentNode.parentNode.id
    console.log(postId);
    
    if (obj.className === "likeButton") {
        // Redirigez l'utilisateur vers signIn.php
        window.location.href = "./accounts/sign_in.html";
        return; // Sortez de la fonction pour éviter l'exécution du reste du code
    }
    
    // Send an AJAX request to the PHP file when the button is clicked
    if (obj.classList.contains("liked")) {
        obj.classList.remove("liked");
        $.ajax({
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/follow.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "remove",
                user: obj.className,
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
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/follow.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "create",
                user: obj.className,
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
        obj.classList.add("liked");
    }
};

function share(obj) {
    console.log(obj.id + " " + obj.className);
    var postId = obj.parentNode.parentNode.parentNode.parentNode.id
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
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/follow.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "remove",
                user: obj.className,
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
            url: "https://webravel.azurewebsites.net/2023-2024-terminales-NSI/leouzan/accounts/follow.php",
            method: "POST", // or "GET" depending on your needs
            data: {
                // You can send any data you need here
                action: "create",
                user: obj.className,
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