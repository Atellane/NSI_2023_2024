<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../composant_css/sign_in_sign_up_and_create_post.css">
    <link rel="stylesheet" href="../composant_css/header.css">
    <link rel="stylesheet" href="../composant_css/pfp.css">
    <link rel="stylesheet" href="../composant_css/form.css">
    <link rel="stylesheet" href="../composant_css/reponse_php.css">
    <title>Sign in</title>
</head>
<body>
    <header>
        <nav>
            <ul id="topBar">
                <li id="acceuil">
                    <a href="../page_d_acceuil.php">
                        <svg version="1.1" id="homeIcon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                        viewBox="0 0 460.298 460.297" xml:space="preserve" >
                            <path d="M230.149,120.939L65.986,256.274c0,0.191-0.048,0.472-0.144,0.855c-0.094,0.38-0.144,0.656-0.144,0.852v137.041
                            c0,4.948,1.809,9.236,5.426,12.847c3.616,3.613,7.898,5.431,12.847,5.431h109.63V303.664h73.097v109.64h109.629
                            c4.948,0,9.236-1.814,12.847-5.435c3.617-3.607,5.432-7.898,5.432-12.847V257.981c0-0.76-0.104-1.334-0.288-1.707L230.149,120.939
                            z"/>
    
                            <path d="M457.122,225.438L394.6,173.476V56.989c0-2.663-0.856-4.853-2.574-6.567c-1.704-1.712-3.894-2.568-6.563-2.568h-54.816
                            c-2.666,0-4.855,0.856-6.57,2.568c-1.711,1.714-2.566,3.905-2.566,6.567v55.673l-69.662-58.245
                            c-6.084-4.949-13.318-7.423-21.694-7.423c-8.375,0-15.608,2.474-21.698,7.423L3.172,225.438c-1.903,1.52-2.946,3.566-3.14,6.136
                            c-0.193,2.568,0.472,4.811,1.997,6.713l17.701,21.128c1.525,1.712,3.521,2.759,5.996,3.142c2.285,0.192,4.57-0.476,6.855-1.998
                            L230.149,95.817l197.57,164.741c1.526,1.328,3.521,1.991,5.996,1.991h0.858c2.471-0.376,4.463-1.43,5.996-3.138l17.703-21.125
                            c1.522-1.906,2.189-4.145,1.991-6.716C460.068,229.007,459.021,226.961,457.122,225.438z"/>
                        </svg>
                    </a>
                    <a href="../page_d_acceuil.php#mostRecentPost">Post les plus récents</a>
                    <a href="../page_d_acceuil.php#postRankedByNumberOfShare">Post les plus partagés</a>
                    <?php
                    try {
                        session_start();
                        if (isset($_SESSION['utilisateur'])) {
                            echo '<a href="../page_d_acceuil.php#postFromFollowed">Post de vos abonnements</a>';
                            echo '<a href="../posts/create_a_post.php">Créer un post</a>';
                        }
                    } catch (Exception $e) {
                        die($e->getMessage());
                    }
                    ?>
                    
                </li>
                <?php
                try {
                    if (isset($_SESSION["utilisateur"])) {
                        $username = $_SESSION["utilisateur"];
                        $pdp = $_SESSION["nom_photo_de_profil"];
                        echo "<li id='username'>
                            $username
                            <img id='pfp' src='./pfp/$pdp' alt='photo de profil de $username'>
                            <a id='logOut' href='./log_out.php'>Log out</a>
                        </li>";

                    } else {
                        echo "<li id='connexion'>
                            <a id='signIn' href='./sign_in.php'>Sign in</a>
                            <a id='signUp' href='./sign_up.php'>Sign up</a>
                        </li>";
                    }
                } catch (Exception $e) {
                    echo "" . $e->getMessage() . "";
                }
                ?>
            </ul>
        </nav>
    </header>
    <section id="pageContent">
        <?php
        try {
            if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                $dbh = new PDO('mysql:host=localhost;port=50765;dbname=eouzan', 'azure', '6#vWHD_$');
                $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                $username = htmlspecialchars($_POST['username']);

                $sql = "SELECT username, mot_de_passe, nom_photo_de_profil FROM utilisateurs WHERE username = :username";
                $statement = $dbh->prepare($sql);
                $statement->bindParam(':username', $username, PDO::PARAM_STR);
                $statement->execute();
                
                // Vérifier si l'utilisateur existe
                if ($statement->rowCount() === 0) {
                    // L'utilisateur n'existe pas
                    die("<section id='reponsePhp'>
                        <p>Nom d'utilisateur incorrect</p>
                        <button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>
                    </section>");
                }
                
                $user = $statement->fetch(PDO::FETCH_ASSOC);
                
                // Comparaison du mot de passe
                if (password_verify(htmlspecialchars($_POST['password']), $user['mot_de_passe'])) {
                    // Mot de passe correct, connecter l'utilisateur
                    $_SESSION["utilisateur"] = $user['username'];
                    $_SESSION['nom_photo_de_profil'] = $user['nom_photo_de_profil'];
                
                    // Redirection vers la page appropriée
                    header("Location: ../page_d_acceuil.php");
                    exit();
                } else {
                    // Mot de passe incorrect
                    die("<section id='reponsePhp'>
                        <p>Mot de passe incorrect</p>
                        <button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>
                    </section>");
                }
            } else {
                echo "<h1>Se connecter :</h1>
                <form method='post'>
                    <div>
                        <label for='username'>Nom d'utilisateur :</label>
                        <input type='text' id='username' name='username'>
                    </div>
                    <div>
                        <label for='password'>Mot de passe :</label>
                        <input type='password' id='password' name='password'>
                    </div>
                    <div id='submitInput'>
                        <input type='submit' value='Envoyer'>
                    </div>
                </form>";
            }
        } catch (Exception $e) {
            die("". $e->getMessage());
        }
        ?>
    </section>
</body>
</html>