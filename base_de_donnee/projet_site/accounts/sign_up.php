<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="sign_in_and_up.css">
    <link rel="stylesheet" href="../header.css">
    <link rel="stylesheet" href="../form.css">
    <title>Sign up</title>
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
                    <?php
                    try {
                        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                            if (isset($_POST['utilisateur'])) {
                                echo '<a href="../page_d_acceuil.php#postFromFollowed">Post de vos abonnements</a>';
                            }
                        }
                    } catch (Exception $e) {
                        die($e->getMessage());
                    }
                    ?>
                    <a href="../page_d_acceuil.php#postRankedByNumberOfShare">Post les plus partagés</a>
                    <a href="../posts/createAPost.php">Créer un post</a>
                </li>
                <li>
                    <form id="searchBar" action="../search_answer.php" method="get">
                        <div>
                            <label for="keyword">recherche :</label>
                            <input type="text" id="keyword" name="keyword">
                        </div>
                        <div>
                            <button type="submit" >
                                <svg focusable="false" viewBox="0 0 24 24">
                                    <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
                                </svg>
                            </button>
                        </div>
                    </form>
                </li>
                <?php
                try {
                    session_start();

                    if (isset($_SESSION["utilisateur"])) {
                        $username = $_SESSION["utilisateur"];
                        $pdp = $_SESSION["nom_photo_de_profil"];
                        echo "<li id='username'>
                            $username
                            <img src='./pfp/$pdp' alt='photo de profil de $username'>
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

                $username = $_POST["username"];

                if (strlen($username) === 0) {
                    die("<section id='reponsePhp'>
                    <p>Vous devez renseigner un nom d'utilisateur.</p>
                    <button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>
                </section>");
                }

                $sql = "SELECT username FROM utilisateurs WHERE username = :username";
                $statement = $dbh->prepare($sql);
                $statement->bindParam(':username', $username, PDO::PARAM_STR);
                $statement->execute();

                // Vérifier le résultat
                $user = $statement->fetch(PDO::FETCH_ASSOC);

                if ($user) {
                    // Le nom d'utilisateur existe déjà dans la base de données
                    die("<section id='reponsePhp'>
                        <p>Le nom d'utilisateur existe déjà. Veuillez en choisir un autre.</p>
                        <button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>
                    </section>");
                }

                if (strlen($_POST["password"]) === 0) {
                    die("<section id='reponsePhp'>
                    <p>Vous devez renseigner un mot de passe</p>
                    <button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>
                </section>");
                }

                $mot_de_passe = password_hash($_POST["password"], PASSWORD_DEFAULT);

                $pfp = $_FILES["pfp"];
                $upload_dir = "./pfp/";
                $upload_file = $upload_dir . basename("default_pfp.png");

                if ($pfp['size'] !== 0) {
                    $base_pfp_name = $pfp["name"];
                    $pfp_tmp = $pfp["tmp_name"];
                    $pfp_extension = pathinfo($base_pfp_name, PATHINFO_EXTENSION);
                    $pfp_name = uniqid() . '_' . date('Ymd') . '.' . $pfp_extension;
    
                    $extensions_valides = array( 'jpg' , 'jpeg', 'png', 'svg', 'gif' );

                    if (!in_array($pfp_extension, $extensions_valides)) {
                        die("<section id='reponsePhp'>
                            <p>seul les fichiers aux extensions jpg, jpeg, png, svg et gif sont acceptés</p>
                            <button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>
                        </section>");
                    }

                    $size = getimagesize($pfp_tmp);
                    $file = fopen($pfp_tmp, "rb");
                    $contents = file_get_contents($pfp_tmp);
                    
                    if ($size && $file) {
                        if (substr($size["mime"], 0, 6) !== "image/") {
                            echo "<section id='reponsePhp'>
                            <p>Attaque potentielle par téléchargement de fichiers. Voici plus d'informations :</p><br />";
                            print_r($_FILES);
                            echo "<button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>";
                            echo "</section>";
                            die("$contents");
                        }
                    }

                    $png_header = "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A";
                    $jpg_header = "\xFF\xD8";
                    $gif_header_87a = "GIF87a";
                    $gif_header_89a = "GIF89a";
                    $isPng = (substr($contents, 0, strlen($png_header)) === $png_header);
                    $isJpg = (substr($contents, 0, strlen($jpg_header)) === $jpg_header);
                    $isGif = (substr($contents, 0, strlen($gif_header_87a)) === $gif_header_87a) || (substr($contents, 0, strlen($gif_header_89a)) === $gif_header_89a);
                    $isSvg = (strpos($contents, '<svg'));

                    if (!$isPng && !$isJpg && !$isGif && !$isSvg) {
                        echo "<section id='reponsePhp'>
                        <p>Attaque potentielle par téléchargement de fichiers. Voici plus d'informations :</p><br />";
                        print_r($_FILES);
                        echo "<button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>";
                        echo "</section>";
                        die("$contents");
                    }
                    
                    if (($ressource = imagecreatefrompng($pfp_tmp)) !== false) {
                        // Création d'une nouvelle image sans les métadonnées pour éviter toute injection de code via les dites métadonnées
                        imagepng($ressource, $pfp_tmp);
                    
                        imagedestroy($ressource);
                    }

                    $newContents = file_get_contents($pfp_tmp);

                    if ((strpos($newContents, 'php')) || (strpos($newContents, '<?php')) || (strpos($newContents, '<scipt')) || (strpos($newContents, '</script>'))) {
                        echo "<section id='reponsePhp'>
                        <p>Attaque potentielle par téléchargement de fichiers. Voici plus d'informations :</p><br />";
                        print_r($_FILES);
                        echo "<button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>";
                        echo "</section>";
                        die("$newContents");
                    }

                    $upload_file = $upload_dir . basename($pfp_name);

                    if (!move_uploaded_file($pfp_tmp, $upload_file)) {
                        echo "<section id='reponsePhp'>
                        <p>Attaque potentielle par téléchargement de fichiers. Voici plus d'informations :</p><br />";
                        print_r($_FILES);
                        echo "<button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>";
                        echo "</section>";
                        die("$contents");
                    }
                }
                
                $sql = "INSERT INTO utilisateurs (username, mot_de_passe, emplacement_photo_de_profil) VALUES (:username, :mot_de_passe, :upload_file)";
                $statement = $dbh->prepare($sql);
                $statement->bindParam(':username', $username, PDO::PARAM_STR);
                $statement->bindParam(':mot_de_passe', $mot_de_passe, PDO::PARAM_STR);
                $statement->bindParam(':upload_file', $upload_file, PDO::PARAM_STR);
                $statement->execute();

                die("<section id='reponsePhp'>
                    <p>ça a marché !</p>
                    <img src='../assets/signeValidation.png' alt='image signe validation'>
                    <a href='./sign_in.php'>se connecter</a>
                </section>");
            } else {
                echo "<h1>S'inscrire :</h1>
                <form enctype='multipart/form-data' method='post'>
                    <div>
                        <label for='username'>Nom d'utilisateur :</label>
                        <input type='text' id='username' name='username'>
                    </div>
                    <div>
                        <label for='password'>Mot de passe :</label>
                        <input type='password' id='password' name='password'>
                    </div>
                    <div>
                        <label for='pfp'>Photo de profil :</label>
                        <input type='file' name='pfp' id='pfp'>
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