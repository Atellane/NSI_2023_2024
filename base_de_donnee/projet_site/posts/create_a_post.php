<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="create_a_post.css">
    <link rel="stylesheet" href="../composant_css/sign_in_sign_up_and_create_post.css">
    <link rel="stylesheet" href="../composant_css/header.css">
    <link rel="stylesheet" href="../composant_css/pfp.css">
    <link rel="stylesheet" href="../composant_css/reponse_php.css">
    <link rel="stylesheet" href="../composant_css/post.css">
    <link rel="stylesheet" href="../composant_css/follow_button.css">
    <link rel="stylesheet" href="../composant_css/form.css">
    <title>Créer un post</title>
</head>
<body>
<header>
        <nav>
            <ul id="topBar">
                <li id="acceuil">
                    <a href="../index.php">
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
                    <a href="../index.php#mostRecentPost">Post les plus récents</a>
                    <a href="../index.php#postRankedByNumberOfShare">Post les plus partagés</a>
                    <?php
                    try {
                        session_start();
                        if (isset($_SESSION['utilisateur'])) {
                            echo '<a href="../accounts/index.php#postFromFollowed">Post de vos abonnements</a>';
                            echo '<a href="./create_a_post.php">Créer un post</a>';
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
                            <img id='pfp'src='../accounts/pfp/$pdp' alt='photo de profil de $username'>
                            <a id='logOut' href='../accounts/log_out.php'>Log out</a>
                        </li>";

                    } else {
                        echo "<li id='connexion'>
                            <a id='signIn' href='../accounts/sign_in.php'>Sign in</a>
                            <a id='signUp' href='../accounts/sign_up.php'>Sign up</a>
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
            if (isset($_SESSION["utilisateur"])) {
                if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                    $dbh = new PDO('mysql:host=localhost;port=50929;dbname=eouzan', 'azure', '6#vWHD_$');
                    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                    $nombreDePartage = 0;
                    $nombreDeCommentaire = 0;

                    $postText = $_POST["postText"];

                    date_default_timezone_set('Europe/Paris');
                    $dateEtHeure = date('Y-m-d H:i:s'); // Format DATETIME requis pour MySQL

                    $signatureMessage = $_SESSION["utilisateur"] . $dateEtHeure;

                    $postPicture = $_FILES["postPicture"];
    
                    if (!(empty($postPicture["name"]))) {
                        $upload_dir = "./post_picture/";
                        $base_postPicture_name = $postPicture["name"];
                        $postPicture_tmp = $postPicture["tmp_name"];
                        $postPicture_extension = pathinfo($base_postPicture_name, PATHINFO_EXTENSION);
                        $postPicture_name = uniqid() . '_' . date('Ymd') . '.' . $postPicture_extension;
        
                        $extensions_valides = array( 'jpg' , 'jpeg', 'png', 'svg', 'gif' );
    
                        if (!in_array($postPicture_extension, $extensions_valides)) {
                            die("<section id='reponsePhp'>
                                <p>seul les fichiers aux extensions jpg, jpeg, png, svg et gif sont acceptés</p>
                                <button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>
                            </section>");
                        }
    
                        $size = getimagesize($postPicture_tmp);
                        $file = fopen($postPicture_tmp, "rb");
                        $contents = file_get_contents($postPicture_tmp);
                        
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
                        
                        if (($ressource = imagecreatefrompng($postPicture_tmp)) !== false) {
                            // Création d'une nouvelle image sans les métadonnées pour éviter toute injection de code via les dites métadonnées
                            imagepng($ressource, $postPicture_tmp);
                        
                            imagedestroy($ressource);
                        }
    
                        $newContents = file_get_contents($postPicture_tmp);
    
                        if ((strpos($newContents, 'php')) || (strpos($newContents, '<?php')) || (strpos($newContents, '<scipt')) || (strpos($newContents, '</script>'))) {
                            echo "<section id='reponsePhp'>
                            <p>Attaque potentielle par téléchargement de fichiers. Voici plus d'informations :</p><br />";
                            print_r($_FILES);
                            echo "<button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>";
                            echo "</section>";
                            die("$newContents");
                        }
                        
                        $upload_file = $upload_dir . basename($postPicture_name);
    
                        if (!move_uploaded_file($postPicture_tmp, $upload_file)) {
                            echo "<section id='reponsePhp'>
                            <p>Attaque potentielle par téléchargement de fichiers. Voici plus d'informations :</p><br />";
                            print_r($_FILES);
                            echo "<button onclick='history.replaceState(null, null, location.href);location.reload();'>réessayer</button>";
                            echo "</section>";
                            die("$contents");
                        }

                        $sql = "INSERT INTO messages (signatureMessage, auteur, dateEtHeure, nom_image, texte, nombreDePartage, nombreDeCommentaire) VALUES (:signatureMessage, :auteur, :dateEtHeure, :nom_image, :texte, :nombreDePartage, :nombreDeCommentaire)";
                        
                        $statement = $dbh->prepare($sql);
                        $statement->bindParam(':signatureMessage', $signatureMessage, PDO::PARAM_STR);
                        $statement->bindParam(':auteur', $_SESSION["utilisateur"], PDO::PARAM_STR);
                        $statement->bindParam(":dateEtHeure", $dateEtHeure, PDO::PARAM_STR);
                        $statement->bindParam(":nom_image", $postPicture_name, PDO::PARAM_STR);
                        $statement->bindParam(":texte", $postText, PDO::PARAM_STR);
                        $statement->bindParam(":nombreDePartage", $nombreDePartage, PDO::PARAM_INT);
                        $statement->bindParam(":nombreDeCommentaire", $nombreDeCommentaire, PDO::PARAM_INT);
                        $statement->execute();
                    } else {
                        $sql = "INSERT INTO messages (signatureMessage, auteur, dateEtHeure, texte, nombreDePartage, nombreDeCommentaire) VALUES (:signatureMessage, :auteur, :dateEtHeure, :texte, :nombreDePartage, :nombreDeCommentaire)";
                        
                        $statement = $dbh->prepare($sql);
                        $statement->bindParam(':signatureMessage', $signatureMessage, PDO::PARAM_STR);
                        $statement->bindParam(':auteur', $_SESSION["utilisateur"], PDO::PARAM_STR);
                        $statement->bindParam(":dateEtHeure", $dateEtHeure, PDO::PARAM_STR);
                        $statement->bindParam(":texte", $postText, PDO::PARAM_STR);
                        $statement->bindParam(":nombreDePartage", $nombreDePartage, PDO::PARAM_INT);
                        $statement->bindParam(":nombreDeCommentaire", $nombreDeCommentaire, PDO::PARAM_INT);
                        $statement->execute();
                    }
                    $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage, messages.nombreDeCommentaire, utilisateurs.nom_photo_de_profil
                            FROM messages
                            LEFT JOIN utilisateurs ON messages.auteur = utilisateurs.username
                            WHERE messages.signatureMessage = :signatureMessage";

                    $statement = $dbh->prepare($sql);
                    $statement->bindParam(":signatureMessage", $signatureMessage, PDO::PARAM_STR);
                    $statement->execute();
                    $messages = $statement->fetchAll(PDO::FETCH_ASSOC);
                    $message = $messages[0];

                    echo "<section id='reponsePhp'>
                    <p>ça a marché !</p>
                    <img src='../assets/signeValidation.png' alt='image signe validation'>
                </section>";

                    echo "<article class='blogPost' id='" . $message["signatureMessage"] . "'>
                            <header>
                                <ul>
                                    <li><img id='pfp' src='../accounts/pfp/" . $message["nom_photo_de_profil"] . "' alt='photo de profil de " . $message["auteur"] . "' width='30' height='30'></li>
                                    <li>" . $message["auteur"] . "</li>
                                    <li class='datetime'>" . $message["dateEtHeureFormatee"] . "</li>
                                </ul>
                            </header>";

                    if (!(is_null($message["nom_image"]))) {
                        echo "<section class='postContent'>
                                <img src='../posts/post_picture/" . $message["nom_image"] . "' alt='imagePost' />
                                <br />
                                <p>" . $message["texte"] . "</p>
                            </section>";
                    } else {
                        echo "<section class='postContent'>
                                <p>" . $message["texte"] . "</p>
                            </section>";
                    }

                    echo "<footer>
                            <section class='postFooter'>
                                <p>Preview de votre post</p>
                            </section>
                        </footer>
                    </article>";
                } else {
                    echo "<h1>Créer un post :</h1>
                    <form enctype='multipart/form-data' method='post'>
                        <div>
                            <label for='postText'>Texte du post :</label>
                            <input type='text' id='postText' name='postText'  rows='5' cols='40'>
                        </div>
                        <div>
                            <label for='postPicture'>Photo pour le post (optionnel) :</label>
                            <input type='file' name='postPicture' id='postPicture'>
                        </div>
                        <div id='submitInput'>
                            <input type='submit' value='Envoyer'>
                        </div>
                    </form>";
                }
            } else {
                die("<section id='reponsePhp'>
                <p>Vous n'êtes pas autorisé à accéder à cette page sans être connecté !</p>
            </section>");
            }
        } catch (Exception $e) {
            die($e->getMessage());
        }
        ?>
    </section>
</body>
</html>