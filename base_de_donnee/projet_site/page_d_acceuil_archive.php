<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="page_d_acceuil.css" />
        <link rel="stylesheet" href="./composant_css/header.css">
        <link rel="stylesheet" href="./composant_css/pfp.css">
        <link rel="stylesheet" href="./composant_css/post.css">
        <link rel="stylesheet" href="./composant_css/follow_button.css">
        <link rel="stylesheet" href="./composant_css/display_user.css">
        <link rel="stylesheet" href="./composant_css/form.css">
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script type="text/javascript" src="follow_share_and_action_for_post.js"></script>
        <title>Blog</title>
    </head>
    <body>
    <header>
        <nav>
            <ul id="topBar">
                <li id="acceuil">
                    <a href="./page_d_acceuil.php">
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
                    <a href="./page_d_acceuil.php#mostRecentPost">Post les plus récents</a>
                    <a href="./page_d_acceuil.php#postRankedByNumberOfShare">Post les plus partagés</a>
                    <?php
                    try {
                        session_start();
                        if (isset($_SESSION['utilisateur'])) {
                            echo '<a href="./accounts/page_d_acceuil.php#postFromFollowed">Post de vos abonnements</a>';
                            echo '<a href="./posts/create_a_post.php">Créer un post</a>';
                        }
                    } catch (Exception $e) {
                        die($e->getMessage());
                    }
                    ?>
                    
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
                    if (isset($_SESSION["utilisateur"])) {
                        $username = $_SESSION["utilisateur"];
                        $pdp = $_SESSION["nom_photo_de_profil"];
                        echo "<li id='username'>
                            $username
                            <img id='pfp' src='./accounts/pfp/$pdp' alt='photo de profil de $username'>
                            <a id='logOut' href='./accounts/log_out.php'>Log out</a>
                        </li>";

                    } else {
                        echo "<li id='connexion'>
                            <a id='signIn' href='./accounts/sign_in.php'>Sign in</a>
                            <a id='signUp' href='./accounts/sign_up.php'>Sign up</a>
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
            <section id="mostPopularUsers">
                <h1>Les utilisateur.ice.s par odre de popularité :</h1>
                    <?php
                    try {
                        $dbh = new PDO('mysql:host=localhost;port=50765;dbname=eouzan', 'azure', '6#vWHD_$');
                        $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                        $sql = "SELECT username, nom_photo_de_profil, nombre_abonne FROM utilisateurs ORDER BY nombre_abonne DESC";
                        $statement = $dbh->query($sql);
                        $users = $statement->fetchAll(PDO::FETCH_ASSOC);
                        if (isset($_SESSION["utilisateur"])) {
                            foreach ($users as $user) {
                                echo "<nav class='user'>                    
                                <ul>
                                    <li><img id='pfp' src='./accounts/pfp/" . $user['nom_photo_de_profil'] . "' alt='photo de profil de  " . $user['username'] . "' width='30' height='30'></li>
                                    <li>" . $user['username'] . "</li>
                                    <li>
                                        <button class='followButton connecte' id='" . $user['username'] . "' onclick='follow(this)'>
                                            <span>Follow</span>
                                            <img src='./assets/signeValidation.png' height='20' width='20'>
                                        </button>
                                    </li>
                                </ul>
                                <p>" . $user['nombre_abonne'] . " followers</p>
                            </nav>";
                            }
                        } else {
                            foreach ($users as $user) {
                                echo "<nav class='user'>                    
                                <ul>
                                    <li><img id='pfp' src='./accounts/pfp/" . $user['nom_photo_de_profil'] . "' alt='photo de profil de " . $user['username'] . "' width='30' height='30'></li>
                                    <li>" . $user['username'] . "</li>
                                    <li>
                                        <button class='followButton' id='" . $user['username'] . "' onclick='follow(this)'>
                                            <span>Follow</span>
                                            <img src='./assets/signeValidation.png' height='20' width='20'>
                                        </button>
                                    </li>
                                </ul>
                                <p>" . $user['nombre_abonne'] . " followers</p>
                            </nav>";
                            }
                        }
                    } catch (Exception $e) {
                        die($e->getMessage());
                    }
                    ?>
            </section>
            <section id="forPost">
                <section id="mostRecentPost">
                    <h1>Les 2 derniers posts les plus récents :</h1>
                    <?php
                    try {
                        $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage, messages.nombreDeCommentaire
                        FROM messages
                        LEFT JOIN commente ON commente.commentaire = messages.signatureMessage
                        WHERE commente.commentaire IS NULL
                        ORDER BY messages.dateEtHeure DESC
                        LIMIT 2";

                        $statement = $dbh->query($sql);
                        $messages = $statement->fetchAll(PDO::FETCH_ASSOC);

                        $sql = "SELECT utilisateurs.username, utilisateurs.nom_photo_de_profil
                        FROM utilisateurs
                        INNER JOIN messages ON messages.auteur = utilisateurs.username
                        LEFT JOIN commente ON commente.commentaire = messages.signatureMessage
                        WHERE commente.commentaire IS NULL
                        ORDER BY messages.dateEtHeure DESC
                        LIMIT 2";

                        $statement = $dbh->query($sql);
                        $auteurs = $statement->fetchAll(PDO::FETCH_ASSOC);

                        if (isset($_SESSION["utilisateur"])) {
                            foreach ($messages as $message) {
                                foreach ($auteurs as $auteur) {
                                    if ($message["auteur"] === $auteur["username"]) {
                                        echo "<article id='" . $message["signatureMessage"] . "'>
                                        <header>
                                            <ul>
                                                <li><img id='pfp' src='./accounts/pfp/" . $auteur["nom_photo_de_profil"] . "' alt='photo de profil de " . $message["auteur"] . "' width='30' height='30'></li>
                                                <li>" . $message["auteur"] . "</li>
                                                <li class='liFollow'>                            
                                                    <button class='followButton connecte' id='" . $message["auteur"] . "' onclick='follow(this)'>
                                                        <span>Follow</span>
                                                        <img src='./assets/signeValidation.png' height='20' width='20'>
                                                    </button>
                                                </li>
                                                <li class='datetime'>" . $message["dateEtHeureFormatee"] . "</li>
                                            </ul>
                                        </header>";

                                        if (!(is_null($message["nom_image"]))) {
                                            echo "<section class='postContent'>
                                            <img src='./posts/post_picture/" . $message["nom_image"] . "' alt='imagePost' />
                                            <br />
                                            <p>" . $message["texte"] . "</p>
                                        </section>";
                                        } else {
                                            echo "<section class='postContent'>
                                            <p>" . $message["texte"] . "</p>
                                        </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $message["auteur"]) {
                                            echo "<footer>
                                            <section class='postFooter'>
                                                <ul>
                                                    <li class='partage'>
                                                        <button class='shareButton connecte' onclick='share(this)'>
                                                        </button>
                                                        <p>" . $message["nombreDePartage"] . "</p>
                                                    </li>
                                                    <li>
                                                        <button class='commentButton connecte' onclick='ouvrirCommentaire(this)'>
                                                            <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                            </svg>
                                                        </button>
                                                        " . $message["nombreDeCommentaire"] . "
                                                    </li>
                                                    <li>
                                                        <button onclick='ouvrirModif(this)'>
                                                            <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                            </svg>
                                                        </button>
                                                    </li>
                                                    <li>
                                                        <button onclick='supprimerPost(this)'>
                                                            <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                            </svg>
                                                        </button>
                                                    </li>
                                                </ul>
                                            </section>";
                                        } else {
                                            echo "<footer>
                                            <section class='postFooter'>
                                                <ul>
                                                    <li class='partage'>
                                                        <button class='shareButton connecte' onclick='share(this)'>
                                                        </button>
                                                        <p>" . $message["nombreDePartage"] . "</p>
                                                    </li>
                                                    <li>
                                                        <button class='commentButton connecte' onclick='ouvrirCommentaire(this)'>
                                                            <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                            </svg>
                                                        </button>
                                                        " . $message["nombreDeCommentaire"] . "
                                                    </li>
                                                </ul>
                                            </section>";
                                        }

                                        $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage
                                        FROM messages
                                        INNER JOIN commente ON commente.commentaire =  messages.signatureMessage
                                        WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $commentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        $sql = "SELECT utilisateurs.nom_photo_de_profil
                                        FROM utilisateurs
                                        INNER JOIN messages ON messages.auteur = utilisateurs.username
                                        INNER JOIN commente ON commente.commentaire = messages.signatureMessage
                                        WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $auteurCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        if(!(is_null($commentaires))) {
                                            echo "<section class='comment'>";

                                            foreach ($commentaires as $commentaire) {
                                                foreach ($auteurCommentaires as $auteurCommentaire) {
                                                    if ($commentaire["auteur"] === $auteurCommentaire["username"]) {
                                                        echo "<article id='" . $commentaire["signaturecommentaire"] . "'>
                                                        <header>
                                                            <ul>
                                                                <li><img id='pfp' src='./accounts/pfp/" . $auteurCommentaire["nom_photo_de_profil"] . "' alt='photo de profil de " . $commentaire["auteur"] . "' width='30' height='30'></li>
                                                                <li>" . $commentaire["auteur"] . "</li>
                                                                <li class='liFollow'>                            
                                                                    <button class='followButton connecte' id='" . $commentaire["auteur"] . "' onclick='follow(this)'>
                                                                        <span>Follow</span>
                                                                        <img src='./assets/signeValidation.png' height='20' width='20'>
                                                                    </button>
                                                                </li>
                                                                <li class='datetime'>" . $commentaire["dateEtHeureFormatee"] . "</li>
                                                            </ul>
                                                        </header>";
                
                                                        if (!(is_null($commentaire["nom_image"]))) {
                                                            echo "<section class='postContent'>
                                                            <img src='./posts/post_picture/" . $commentaire["nom_image"] . "' alt='imagePost' />
                                                            <br />
                                                            <p>" . $commentaire["texte"] . "</p>
                                                        </section>";
                                                        } else {
                                                            echo "<section class='postContent'>
                                                            <p>" . $commentaire["texte"] . "</p>
                                                        </section>";
                                                        }
                
                                                        echo "<footer>
                                                        <section class='postFooter'>";
                
                                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                                            echo "<footer>
                                                            <section class='postFooter'>
                                                                <ul>
                                                                    <li class='partage'>
                                                                        <button class='shareButton connecte' onclick='share(this)'>
                                                                        </button>
                                                                        <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                    </li>
                                                                    <li>
                                                                        <button onclick='ouvrirModif(this)'>
                                                                            <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                                <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                                            </svg>
                                                                        </button>
                                                                    </li>
                                                                    <li>
                                                                        <button onclick='supprimerPost(this)'>
                                                                            <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                                <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                                <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                                <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                                            </svg>
                                                                        </button>
                                                                    </li>
                                                                </ul>
                                                            </section>
                                                            <article class='modification'>
                                                                <header>
                                                                    <form enctype='multipart/form-data' class='modifForm'>
                                                                        <label for='postText'>Texte Post:</label>
                                                                        <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                                        <br /> <label for='image'>Image :</label>
                                                                        <input class='imageModification' type='file' name='image'>
                                                                        <br>
                                                                    </form>
                                                                
                                                                    <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                                </header>
                                                                <footer>
                                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                                    <h1 class='modifPreview'>
                                                                        SENT: <span></span>
                                                                        <img src='#' alt='rien' />
                                                                    </h1>
                                                                </footer>
                                                            </article>
                                                        </footer>";
                                                        } else {
                                                            echo "<footer>
                                                            <section class='postFooter'>
                                                                <ul>
                                                                    <li class='partage'>
                                                                        <button class='shareButton connecte' onclick='share(this)'>
                                                                        </button>
                                                                        <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                    </li>
                                                                </ul>
                                                            </section>
                                                        </footer>";
                                                        }

                                                        echo "</article>";
                                                    }
                                                }
                                            }

                                            echo "<article class='commentFormSection'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='commentForm'>
                                                        Commentaire:
                                                        <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageCommentaire' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='commentPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </section>";
                                        } else {
                                            echo "<section class='comment'>
                                            <article class='commentFormSection'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='commentForm'>
                                                        Commentaire:
                                                        <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageCommentaire' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='commentPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                         echo "<article class='modification'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='modifForm'>
                                                        <label for='postText'>Texte Post:</label>
                                                        <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageModification' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='modifPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </footer>";
                                        } else {
                                            echo "</footer>";
                                        }
                                        echo "</article>";
                                    }
                                }
                            }
                        } else {
                            foreach ($messages as $message) {
                                foreach ($auteurs as $auteur) {
                                    if ($message["auteur"] === $auteur["username"]) {
                                        echo "<article id='" . $message["signatureMessage"] . "'>
                                        <header>
                                            <ul>
                                                <li><img id='pfp' src='./accounts/pfp/" . $auteur["nom_photo_de_profil"] . "' alt='photo de profil de " . $message["auteur"] . "' width='30' height='30'></li>
                                                <li>" . $message["auteur"] . "</li>
                                                <li class='liFollow'>                            
                                                    <button class='followButton' id='" . $message["auteur"] . "' onclick='follow(this)'>
                                                        <span>Follow</span>
                                                        <img src='./assets/signeValidation.png' height='20' width='20'>
                                                    </button>
                                                </li>
                                                <li class='datetime'>" . $message["dateEtHeureFormatee"] . "</li>
                                            </ul>
                                        </header>";

                                        if (!(is_null($message["nom_image"]))) {
                                            echo "<section class='postContent'>
                                            <img src='./posts/post_picture/" . $message["nom_image"] . "' alt='imagePost' />
                                            <br />
                                            <p>" . $message["texte"] . "</p>
                                        </section>";
                                        } else {
                                            echo "<section class='postContent'>
                                            <p>" . $message["texte"] . "</p>
                                        </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $message["auteur"]) {
                                            echo "<footer>
                                            <section class='postFooter'>
                                                <ul>
                                                    <li class='partage'>
                                                        <button class='shareButton' onclick='share(this)'>
                                                        </button>
                                                        <p>" . $message["nombreDePartage"] . "</p>
                                                    </li>
                                                    <li>
                                                        <button class='commentButton' onclick='ouvrirCommentaire(this)'>
                                                            <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                            </svg>
                                                        </button>
                                                        " . $message["nombreDeCommentaire"] . "
                                                    </li>
                                                    <li>
                                                        <button onclick='ouvrirModif(this)'>
                                                            <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                            </svg>
                                                        </button>
                                                    </li>
                                                    <li>
                                                        <button onclick='supprimerPost(this)'>
                                                            <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                            </svg>
                                                        </button>
                                                    </li>
                                                </ul>
                                            </section>";
                                        } else {
                                            echo "<footer>
                                            <section class='postFooter'>
                                                <ul>
                                                    <li class='partage'>
                                                        <button class='shareButton' onclick='share(this)'>
                                                        </button>
                                                        <p>" . $message["nombreDePartage"] . "</p>
                                                    </li>
                                                    <li>
                                                        <button class='commentButton' onclick='ouvrirCommentaire(this)'>
                                                            <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                            </svg>
                                                        </button>
                                                        " . $message["nombreDeCommentaire"] . "
                                                    </li>
                                                </ul>
                                            </section>";
                                        }

                                        $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage
                                        FROM messages
                                        INNER JOIN commente ON commente.commentaire =  messages.signatureMessage
                                        WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $commentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        $sql = "SELECT utilisateurs.username, utilisateurs.nom_photo_de_profil
                                        FROM utilisateurs
                                        INNER JOIN messages ON messages.auteur = utilisateurs.username
                                        INNER JOIN commente ON commente.commentaire = messages.signatureMessage
                                        WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $auteurCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        if(!(is_null($commentaires))) {
                                            echo "<section class='comment'>";

                                            foreach ($commentaires as $commentaire) {
                                                foreach ($auteurCommentaires as $auteurCommentaire) {
                                                    if ($commentaire["auteur"] === $auteurCommentaire["username"]) {
                                                        echo "<article id='" . $commentaire["signaturecommentaire"] . "'>
                                                        <header>
                                                            <ul>
                                                                <li><img id='pfp' src='./accounts/pfp/" . $auteurCommentaire["nom_photo_de_profil"] . "' alt='photo de profil de " . $commentaire["auteur"] . "' width='30' height='30'></li>
                                                                <li>" . $commentaire["auteur"] . "</li>
                                                                <li class='liFollow'>                            
                                                                    <button class='followButton' id='" . $commentaire["auteur"] . "' onclick='follow(this)'>
                                                                        <span>Follow</span>
                                                                        <img src='./assets/signeValidation.png' height='20' width='20'>
                                                                    </button>
                                                                </li>
                                                                <li class='datetime'>" . $commentaire["dateEtHeureFormatee"] . "</li>
                                                            </ul>
                                                        </header>";
                
                                                        if (!(is_null($commentaire["nom_image"]))) {
                                                            echo "<section class='postContent'>
                                                            <img src='./posts/post_picture/" . $commentaire["nom_image"] . "' alt='imagePost' />
                                                            <br />
                                                            <p>" . $commentaire["texte"] . "</p>
                                                        </section>";
                                                        } else {
                                                            echo "<section class='postContent'>
                                                            <p>" . $commentaire["texte"] . "</p>
                                                        </section>";
                                                        }
                
                                                        echo "<footer>
                                                        <section class='postFooter'>";
                
                                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                                            echo "<footer>
                                                            <section class='postFooter'>
                                                                <ul>
                                                                    <li class='partage'>
                                                                        <button class='shareButton' onclick='share(this)'>
                                                                        </button>
                                                                        <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                    </li>
                                                                    <li>
                                                                        <button onclick='ouvrirModif(this)'>
                                                                            <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                                <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                                            </svg>
                                                                        </button>
                                                                    </li>
                                                                    <li>
                                                                        <button onclick='supprimerPost(this)'>
                                                                            <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                                <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                                <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                                <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                                            </svg>
                                                                        </button>
                                                                    </li>
                                                                </ul>
                                                            </section>
                                                            <article class='modification'>
                                                                <header>
                                                                    <form enctype='multipart/form-data' class='modifForm'>
                                                                        <label for='postText'>Texte Post:</label>
                                                                        <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                                        <br /> <label for='image'>Image :</label>
                                                                        <input class='imageModification' type='file' name='image'>
                                                                        <br>
                                                                    </form>
                                                                
                                                                    <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                                </header>
                                                                <footer>
                                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                                    <h1 class='modifPreview'>
                                                                        SENT: <span></span>
                                                                        <img src='#' alt='rien' />
                                                                    </h1>
                                                                </footer>
                                                            </article>
                                                        </footer>";
                                                        } else {
                                                            echo "<footer>
                                                            <section class='postFooter'>
                                                                <ul>
                                                                    <li class='partage'>
                                                                        <button class='shareButton' onclick='share(this)'>
                                                                        </button>
                                                                        <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                    </li>
                                                                </ul>
                                                            </section>
                                                        </footer>";
                                                        }

                                                        echo "</article>";
                                                    }
                                                }
                                            }

                                            echo "<article class='commentFormSection'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='commentForm'>
                                                        Commentaire:
                                                        <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageCommentaire' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='commentPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </section>";
                                        } else {
                                            echo "<section class='comment'>
                                            <article class='commentFormSection'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='commentForm'>
                                                        Commentaire:
                                                        <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageCommentaire' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='commentPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                         echo "<article class='modification'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='modifForm'>
                                                        <label for='postText'>Texte Post:</label>
                                                        <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageModification' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='modifPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </footer>";
                                        } else {
                                            echo "</footer>";
                                        }
                                        echo "</article>";
                                    }
                                }
                            }
                        }
                    } catch (Exception $e) {
                        die($e->getMessage());
                    }
                    ?>
                </section>
                <?php
                try {
                    if (isset($_SESSION["utilisateur"])) {
                        echo "<section id='postFromFollowed'>
                        <h1>Les posts de vos abonnement :</h1>";

                        $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage, messages.nombreDeCommentaire
                        FROM messages
                        LEFT JOIN commente ON commente.commentaire = messages.signatureMessage
                        INNER JOIN sAbonneA ON sAbonneA.abonnement = messages.auteur
                        WHERE commente.commentaire IS NULL AND sAbonneA.abonne = :utilisateur_connecte
                        ORDER BY messages.dateEtHeure DESC";

                        $statement = $dbh->prepare($sql);
                        $statement->bindParam(':utilisateur_connecte', $_SESSION["utilisateur"], PDO::PARAM_STR);
                        $statement->execute();
                        $messages = $statement->fetchAll(PDO::FETCH_ASSOC);

                        $sql = "SELECT utilisateurs.nom_photo_de_profil
                        FROM utilisateurs
                        INNER JOIN messages ON messages.auteur = utilisateurs.username
                        LEFT JOIN commente ON commente.commentaire = messages.signatureMessage
                        INNER JOIN sAbonneA ON sAbonneA.abonnement = messages.auteur
                        WHERE commente.commentaire IS NULL AND sAbonneA.abonne = :utilisateur_connecte
                        ORDER BY messages.dateEtHeure DESC";

                        $statement = $dbh->prepare($sql);
                        $statement->bindParam(':utilisateur_connecte', $_SESSION["utilisateur"], PDO::PARAM_STR);
                        $statement->execute();
                        $auteurs = $statement->fetchAll(PDO::FETCH_ASSOC);

                        if (!(empty($messages))) {
                            echo "<section id='postFromFollowed'>
                            <h1>Les posts de vos abonnement :</h1>";

                            foreach ($messages as $message) {
                                foreach ($auteurs as $auteur) {
                                    if ($message["auteur"] === $auteur["username"]) {
                                        echo "<article id='" . $message["signatureMessage"] . "'>
                                            <header>
                                                <ul>
                                                    <li><img id='pfp' src='./accounts/pfp/" . $auteur["nom_photo_de_profil"] . "' alt='photo de profil de " . $message["auteur"] . "' width='30' height='30'></li>
                                                    <li>" . $message["auteur"] . "</li>
                                                    <li class='liFollow'>                            
                                                        <button class='followButton connecte' id='" . $message["auteur"] . "' onclick='follow(this)'>
                                                            <span>Follow</span>
                                                            <img src='./assets/signeValidation.png' height='20' width='20'>
                                                        </button>
                                                    </li>
                                                    <li class='datetime'>" . $message["dateEtHeureFormatee"] . "</li>
                                                </ul>
                                            </header>";

                                        if (!(is_null($message["nom_image"]))) {
                                            echo "<section class='postContent'>
                                                <img src='./posts/post_picture/" . $message["nom_image"] . "' alt='imagePost' />
                                                <br />
                                                <p>" . $message["texte"] . "</p>
                                            </section>";
                                        } else {
                                            echo "<section class='postContent'>
                                                <p>" . $message["texte"] . "</p>
                                            </section>";
                                        }

                                        echo "<footer>
                                            <section class='postFooter'>";

                                        if ($_SESSION["utilisateur"] === $message["auteur"]) {
                                            echo "<footer>
                                                <section class='postFooter'>
                                                    <ul>
                                                        <li class='partage'>
                                                            <button class='shareButton connecte' onclick='share(this)'>
                                                            </button>
                                                            <p>" . $message["nombreDePartage"] . "</p>
                                                        </li>
                                                        <li>
                                                            <button class='commentButton connecte' onclick='ouvrirCommentaire(this)'>
                                                                <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                    <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                                </svg>
                                                            </button>
                                                            " . $message["nombreDeCommentaire"] . "
                                                        </li>
                                                        <li>
                                                            <button onclick='ouvrirModif(this)'>
                                                                <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                    <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                                </svg>
                                                            </button>
                                                        </li>
                                                        <li>
                                                            <button onclick='supprimerPost(this)'>
                                                                <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                    <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                    <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                    <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                                </svg>
                                                            </button>
                                                        </li>
                                                    </ul>
                                                </section>";
                                        } else {
                                            echo "<footer>
                                                <section class='postFooter'>
                                                    <ul>
                                                        <li class='partage'>
                                                            <button class='shareButton connecte' onclick='share(this)'>
                                                            </button>
                                                            <p>" . $message["nombreDePartage"] . "</p>
                                                        </li>
                                                        <li>
                                                            <button class='commentButton connecte' onclick='ouvrirCommentaire(this)'>
                                                                <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                    <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                                </svg>
                                                            </button>
                                                            " . $message["nombreDeCommentaire"] . "
                                                        </li>
                                                    </ul>
                                                </section>";
                                        }

                                        $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage
                                            FROM messages
                                            INNER JOIN commente ON commente.commentaire =  messages.signatureMessage
                                            WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $commentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        $sql = "SELECT utilisateurs.nom_photo_de_profil
                                            FROM utilisateurs
                                            INNER JOIN messages ON messages.auteur = utilisateurs.username
                                            INNER JOIN commente ON commente.commentaire = messages.signatureMessage
                                            WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $auteurCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        if (!(is_null($commentaires))) {
                                            echo "<section class='comment'>";

                                            foreach ($commentaires as $commentaire) {
                                                foreach ($auteurCommentaires as $auteurCommentaire) {
                                                    if ($commentaire["auteur"] === $auteurCommentaire["username"]) {
                                                        echo "<article id='" . $commentaire["signaturecommentaire"] . "'>
                                                            <header>
                                                                <ul>
                                                                    <li><img id='pfp' src='./accounts/pfp/" . $auteurCommentaire["nom_photo_de_profil"] . "' alt='photo de profil de " . $commentaire["auteur"] . "' width='30' height='30'></li>
                                                                    <li>" . $commentaire["auteur"] . "</li>
                                                                    <li class='liFollow'>                            
                                                                        <button class='followButton connecte' id='" . $commentaire["auteur"] . "' onclick='follow(this)'>
                                                                            <span>Follow</span>
                                                                            <img src='./assets/signeValidation.png' height='20' width='20'>
                                                                        </button>
                                                                    </li>
                                                                    <li class='datetime'>" . $commentaire["dateEtHeureFormatee"] . "</li>
                                                                </ul>
                                                            </header>";

                                                        if (!(is_null($commentaire["nom_image"]))) {
                                                            echo "<section class='postContent'>
                                                                <img src='./posts/post_picture/" . $commentaire["nom_image"] . "' alt='imagePost' />
                                                                <br />
                                                                <p>" . $commentaire["texte"] . "</p>
                                                            </section>";
                                                        } else {
                                                            echo "<section class='postContent'>
                                                                <p>" . $commentaire["texte"] . "</p>
                                                            </section>";
                                                        }

                                                        echo "<footer>
                                                            <section class='postFooter'>";

                                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                                            echo "<footer>
                                                                <section class='postFooter'>
                                                                    <ul>
                                                                        <li class='partage'>
                                                                            <button class='shareButton connecte' onclick='share(this)'>
                                                                            </button>
                                                                            <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                        </li>
                                                                        <li>
                                                                            <button onclick='ouvrirModif(this)'>
                                                                                <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                                    <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                                                </svg>
                                                                            </button>
                                                                        </li>
                                                                        <li>
                                                                            <button onclick='supprimerPost(this)'>
                                                                                <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                                    <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                                    <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                                    <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                                                </svg>
                                                                            </button>
                                                                        </li>
                                                                    </ul>
                                                                </section>
                                                                <article class='modification'>
                                                                    <header>
                                                                        <form enctype='multipart/form-data' class='modifForm'>
                                                                            <label for='postText'>Texte Post:</label>
                                                                            <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                                            <br /> <label for='image'>Image :</label>
                                                                            <input class='imageModification' type='file' name='image'>
                                                                            <br>
                                                                        </form>
                                                                    
                                                                        <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                                    </header>
                                                                    <footer>
                                                                        <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                                        <h1 class='modifPreview'>
                                                                            SENT: <span></span>
                                                                            <img src='#' alt='rien' />
                                                                        </h1>
                                                                    </footer>
                                                                </article>
                                                            </footer>";
                                                        } else {
                                                            echo "<footer>
                                                                <section class='postFooter'>
                                                                    <ul>
                                                                        <li class='partage'>
                                                                            <button class='shareButton connecte' onclick='share(this)'>
                                                                            </button>
                                                                            <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                        </li>
                                                                    </ul>
                                                                </section>
                                                            </footer>";
                                                        }

                                                        echo "</article>";
                                                    }
                                                }
                                            }

                                            echo "<article class='commentFormSection'>
                                                    <header>
                                                        <form enctype='multipart/form-data' class='commentForm'>
                                                            Commentaire:
                                                            <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                            <br /> <label for='image'>Image :</label>
                                                            <input class='imageCommentaire' type='file' name='image'>
                                                            <br>
                                                        </form>
                                                    
                                                        <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                    </header>
                                                    <footer>
                                                        <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                        <h1 class='commentPreview'>
                                                            SENT: <span></span>
                                                            <img src='#' alt='rien' />
                                                        </h1>
                                                    </footer>
                                                </article>
                                            </section>";
                                        } else {
                                            echo "<section class='comment'>
                                                <article class='commentFormSection'>
                                                    <header>
                                                        <form enctype='multipart/form-data' class='commentForm'>
                                                            Commentaire:
                                                            <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                            <br /> <label for='image'>Image :</label>
                                                            <input class='imageCommentaire' type='file' name='image'>
                                                            <br>
                                                        </form>
                                                    
                                                        <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                    </header>
                                                    <footer>
                                                        <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                        <h1 class='commentPreview'>
                                                            SENT: <span></span>
                                                            <img src='#' alt='rien' />
                                                        </h1>
                                                    </footer>
                                                </article>
                                            </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                            echo "<article class='modification'>
                                                    <header>
                                                        <form enctype='multipart/form-data' class='modifForm'>
                                                            <label for='postText'>Texte Post:</label>
                                                            <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                            <br /> <label for='image'>Image :</label>
                                                            <input class='imageModification' type='file' name='image'>
                                                            <br>
                                                        </form>
                                                    
                                                        <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                    </header>
                                                    <footer>
                                                        <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                        <h1 class='modifPreview'>
                                                            SENT: <span></span>
                                                            <img src='#' alt='rien' />
                                                        </h1>
                                                    </footer>
                                                </article>
                                            </footer>";
                                        } else {
                                            echo "</footer>";
                                        }
                                        echo "</article>";
                                    }
                                }
                            }
                        }
                        echo "</section>";
                    }
                } catch (Exception $e) {
                    die($e->getMessage());
                }
                ?>
                <section id="postRankedByNumberOfShare">
                    <h1>Les posts du plus partagés aux plus partagés :</h1>
                    <?php
                    try {
                        $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage, messages.nombreDeCommentaire
                        FROM messages
                        LEFT JOIN commente ON commente.commentaire = messages.signatureMessage
                        WHERE commente.commentaire IS NULL
                        ORDER BY messages.nombreDePartage DESC";

                        $statement = $dbh->query($sql);
                        $messages = $statement->fetchAll(PDO::FETCH_ASSOC);

                        $sql = "SELECT utilisateurs.nom_photo_de_profil
                        FROM utilisateurs
                        INNER JOIN messages ON messages.auteur = utilisateurs.username
                        LEFT JOIN commente ON commente.commentaire = messages.signatureMessage
                        WHERE commente.commentaire IS NULL
                        ORDER BY messages.nombreDePartage DESC";

                        $statement = $dbh->query($sql);
                        $auteurs = $statement->fetchAll(PDO::FETCH_ASSOC);

                        if (isset($_SESSION["utilisateur"])) {
                            foreach ($messages as $message) {
                                foreach ($auteurs as $auteur) {
                                    if ($message["auteur"] === $auteur["username"]) {
                                        echo "<article id='" . $message["signatureMessage"] . "'>
                                        <header>
                                            <ul>
                                                <li><img id='pfp' src='./accounts/pfp/" . $auteur["nom_photo_de_profil"] . "' alt='photo de profil de " . $message["auteur"] . "' width='30' height='30'></li>
                                                <li>" . $message["auteur"] . "</li>
                                                <li class='liFollow'>                            
                                                    <button class='followButton connecte' id='" . $message["auteur"] . "' onclick='follow(this)'>
                                                        <span>Follow</span>
                                                        <img src='./assets/signeValidation.png' height='20' width='20'>
                                                    </button>
                                                </li>
                                                <li class='datetime'>" . $message["dateEtHeureFormatee"] . "</li>
                                            </ul>
                                        </header>";

                                        if (!(is_null($message["nom_image"]))) {
                                            echo "<section class='postContent'>
                                            <img src='./posts/post_picture/" . $message["nom_image"] . "' alt='imagePost' />
                                            <br />
                                            <p>" . $message["texte"] . "</p>
                                        </section>";
                                        } else {
                                            echo "<section class='postContent'>
                                            <p>" . $message["texte"] . "</p>
                                        </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $message["auteur"]) {
                                            echo "<footer>
                                            <section class='postFooter'>
                                                <ul>
                                                    <li class='partage'>
                                                        <button class='shareButton connecte' onclick='share(this)'>
                                                        </button>
                                                        <p>" . $message["nombreDePartage"] . "</p>
                                                    </li>
                                                    <li>
                                                        <button class='commentButton connecte' onclick='ouvrirCommentaire(this)'>
                                                            <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                            </svg>
                                                        </button>
                                                        " . $message["nombreDeCommentaire"] . "
                                                    </li>
                                                    <li>
                                                        <button onclick='ouvrirModif(this)'>
                                                            <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                            </svg>
                                                        </button>
                                                    </li>
                                                    <li>
                                                        <button onclick='supprimerPost(this)'>
                                                            <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                            </svg>
                                                        </button>
                                                    </li>
                                                </ul>
                                            </section>";
                                        } else {
                                            echo "<footer>
                                            <section class='postFooter'>
                                                <ul>
                                                    <li class='partage'>
                                                        <button class='shareButton connecte' onclick='share(this)'>
                                                        </button>
                                                        <p>" . $message["nombreDePartage"] . "</p>
                                                    </li>
                                                    <li>
                                                        <button class='commentButton connecte' onclick='ouvrirCommentaire(this)'>
                                                            <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                            </svg>
                                                        </button>
                                                        " . $message["nombreDeCommentaire"] . "
                                                    </li>
                                                </ul>
                                            </section>";
                                        }

                                        $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage
                                        FROM messages
                                        INNER JOIN commente ON commente.commentaire =  messages.signatureMessage
                                        WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $commentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        $sql = "SELECT utilisateurs.nom_photo_de_profil
                                        FROM utilisateurs
                                        INNER JOIN messages ON messages.auteur = utilisateurs.username
                                        INNER JOIN commente ON commente.commentaire = messages.signatureMessage
                                        WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $auteurCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        if (!(is_null($commentaires))) {
                                            echo "<section class='comment'>";

                                            foreach ($commentaires as $commentaire) {
                                                foreach ($auteurCommentaires as $auteurCommentaire) {
                                                    if ($commentaire["auteur"] === $auteurCommentaire["username"]) {
                                                        echo "<article id='" . $commentaire["signaturecommentaire"] . "'>
                                                        <header>
                                                            <ul>
                                                                <li><img id='pfp' src='./accounts/pfp/" . $auteurCommentaire["nom_photo_de_profil"] . "' alt='photo de profil de " . $commentaire["auteur"] . "' width='30' height='30'></li>
                                                                <li>" . $commentaire["auteur"] . "</li>
                                                                <li class='liFollow'>                            
                                                                    <button class='followButton connecte' id='" . $commentaire["auteur"] . "' onclick='follow(this)'>
                                                                        <span>Follow</span>
                                                                        <img src='./assets/signeValidation.png' height='20' width='20'>
                                                                    </button>
                                                                </li>
                                                                <li class='datetime'>" . $commentaire["dateEtHeureFormatee"] . "</li>
                                                            </ul>
                                                        </header>";

                                                        if (!(is_null($commentaire["nom_image"]))) {
                                                            echo "<section class='postContent'>
                                                            <img src='./posts/post_picture/" . $commentaire["nom_image"] . "' alt='imagePost' />
                                                            <br />
                                                            <p>" . $commentaire["texte"] . "</p>
                                                        </section>";
                                                        } else {
                                                            echo "<section class='postContent'>
                                                            <p>" . $commentaire["texte"] . "</p>
                                                        </section>";
                                                        }

                                                        echo "<footer>
                                                        <section class='postFooter'>";

                                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                                            echo "<footer>
                                                            <section class='postFooter'>
                                                                <ul>
                                                                    <li class='partage'>
                                                                        <button class='shareButton connecte' onclick='share(this)'>
                                                                        </button>
                                                                        <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                    </li>
                                                                    <li>
                                                                        <button onclick='ouvrirModif(this)'>
                                                                            <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                                <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                                            </svg>
                                                                        </button>
                                                                    </li>
                                                                    <li>
                                                                        <button onclick='supprimerPost(this)'>
                                                                            <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                                <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                                <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                                <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                                            </svg>
                                                                        </button>
                                                                    </li>
                                                                </ul>
                                                            </section>
                                                            <article class='modification'>
                                                                <header>
                                                                    <form enctype='multipart/form-data' class='modifForm'>
                                                                        <label for='postText'>Texte Post:</label>
                                                                        <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                                        <br /> <label for='image'>Image :</label>
                                                                        <input class='imageModification' type='file' name='image'>
                                                                        <br>
                                                                    </form>
                                                                
                                                                    <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                                </header>
                                                                <footer>
                                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                                    <h1 class='modifPreview'>
                                                                        SENT: <span></span>
                                                                        <img src='#' alt='rien' />
                                                                    </h1>
                                                                </footer>
                                                            </article>
                                                        </footer>";
                                                        } else {
                                                            echo "<footer>
                                                            <section class='postFooter'>
                                                                <ul>
                                                                    <li class='partage'>
                                                                        <button class='shareButton connecte' onclick='share(this)'>
                                                                        </button>
                                                                        <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                    </li>
                                                                </ul>
                                                            </section>
                                                        </footer>";
                                                        }

                                                        echo "</article>";
                                                    }
                                                }
                                            }

                                            echo "<article class='commentFormSection'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='commentForm'>
                                                        Commentaire:
                                                        <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageCommentaire' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='commentPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </section>";
                                        } else {
                                            echo "<section class='comment'>
                                            <article class='commentFormSection'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='commentForm'>
                                                        Commentaire:
                                                        <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageCommentaire' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='commentPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                            echo "<article class='modification'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='modifForm'>
                                                        <label for='postText'>Texte Post:</label>
                                                        <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageModification' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='modifPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </footer>";
                                        } else {
                                            echo "</footer>";
                                        }
                                        echo "</article>";
                                    }
                                }
                            }
                        } else {
                            foreach ($messages as $message) {
                                foreach ($auteurs as $auteur) {
                                    if ($message["auteur"] === $auteur["username"]) {
                                        echo "<article id='" . $message["signatureMessage"] . "'>
                                        <header>
                                            <ul>
                                                <li><img id='pfp' src='./accounts/pfp/" . $auteur["nom_photo_de_profil"] . "' alt='photo de profil de " . $message["auteur"] . "' width='30' height='30'></li>
                                                <li>" . $message["auteur"] . "</li>
                                                <li class='liFollow'>                            
                                                    <button class='followButton' id='" . $message["auteur"] . "' onclick='follow(this)'>
                                                        <span>Follow</span>
                                                        <img src='./assets/signeValidation.png' height='20' width='20'>
                                                    </button>
                                                </li>
                                                <li class='datetime'>" . $message["dateEtHeureFormatee"] . "</li>
                                            </ul>
                                        </header>";

                                        if (!(is_null($message["nom_image"]))) {
                                            echo "<section class='postContent'>
                                            <img src='./posts/post_picture/" . $message["nom_image"] . "' alt='imagePost' />
                                            <br />
                                            <p>" . $message["texte"] . "</p>
                                        </section>";
                                        } else {
                                            echo "<section class='postContent'>
                                            <p>" . $message["texte"] . "</p>
                                        </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $message["auteur"]) {
                                            echo "<footer>
                                            <section class='postFooter'>
                                                <ul>
                                                    <li class='partage'>
                                                        <button class='shareButton' onclick='share(this)'>
                                                        </button>
                                                        <p>" . $message["nombreDePartage"] . "</p>
                                                    </li>
                                                    <li>
                                                        <button class='commentButton' onclick='ouvrirCommentaire(this)'>
                                                            <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                            </svg>
                                                        </button>
                                                        " . $message["nombreDeCommentaire"] . "
                                                    </li>
                                                    <li>
                                                        <button onclick='ouvrirModif(this)'>
                                                            <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                            </svg>
                                                        </button>
                                                    </li>
                                                    <li>
                                                        <button onclick='supprimerPost(this)'>
                                                            <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                            </svg>
                                                        </button>
                                                    </li>
                                                </ul>
                                            </section>";
                                        } else {
                                            echo "<footer>
                                            <section class='postFooter'>
                                                <ul>
                                                    <li class='partage'>
                                                        <button class='shareButton' onclick='share(this)'>
                                                        </button>
                                                        <p>" . $message["nombreDePartage"] . "</p>
                                                    </li>
                                                    <li>
                                                        <button class='commentButton' onclick='ouvrirCommentaire(this)'>
                                                            <svg viewBox='0 0 48 48' width='22' height='19'>
                                                                <path d='M47.5 46.1l-2.8-11c1.8-3.3 2.8-7.1 2.8-11.1C47.5 11 37 .5 24 .5S.5 11 .5 24 11 47.5 24 47.5c4 0 7.8-1 11.1-2.8l11 2.8c.8.2 1.6-.6 1.4-1.4zm-3-22.1c0 4-1 7-2.6 10-.2.4-.3.9-.2 1.4l2.1 8.4-8.3-2.1c-.5-.1-1-.1-1.4.2-1.8 1-5.2 2.6-10 2.6-11.4 0-20.6-9.2-20.6-20.5S12.7 3.5 24 3.5 44.5 12.7 44.5 24z'></path>
                                                            </svg>
                                                        </button>
                                                        " . $message["nombreDeCommentaire"] . "
                                                    </li>
                                                </ul>
                                            </section>";
                                        }

                                        $sql = "SELECT messages.signatureMessage, messages.auteur, DATE_FORMAT(messages.dateEtHeure, '%d/%m/%Y %H:%i:%s') AS dateEtHeureFormatee, messages.nom_image, messages.texte, messages.nombreDePartage
                                        FROM messages
                                        INNER JOIN commente ON commente.commentaire =  messages.signatureMessage
                                        WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $commentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        $sql = "SELECT utilisateurs.username, utilisateurs.nom_photo_de_profil
                                        FROM utilisateurs
                                        INNER JOIN messages ON messages.auteur = utilisateurs.username
                                        INNER JOIN commente ON commente.commentaire = messages.signatureMessage
                                        WHERE commente.messageCommente = :messageSignature";

                                        $statement = $dbh->prepare($sql);
                                        $statement->bindParam(':messageSignature', $message["signatureMessage"], PDO::PARAM_STR);
                                        $statement->execute();
                                        $auteurCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

                                        if (!(is_null($commentaires))) {
                                            echo "<section class='comment'>";

                                            foreach ($commentaires as $commentaire) {
                                                foreach ($auteurCommentaires as $auteurCommentaire) {
                                                    if ($commentaire["auteur"] === $auteurCommentaire["username"]) {
                                                        echo "<article id='" . $commentaire["signaturecommentaire"] . "'>
                                                        <header>
                                                            <ul>
                                                                <li><img id='pfp' src='./accounts/pfp/" . $auteurCommentaire["nom_photo_de_profil"] . "' alt='photo de profil de " . $commentaire["auteur"] . "' width='30' height='30'></li>
                                                                <li>" . $commentaire["auteur"] . "</li>
                                                                <li class='liFollow'>                            
                                                                    <button class='followButton' id='" . $commentaire["auteur"] . "' onclick='follow(this)'>
                                                                        <span>Follow</span>
                                                                        <img src='./assets/signeValidation.png' height='20' width='20'>
                                                                    </button>
                                                                </li>
                                                                <li class='datetime'>" . $commentaire["dateEtHeureFormatee"] . "</li>
                                                            </ul>
                                                        </header>";

                                                        if (!(is_null($commentaire["nom_image"]))) {
                                                            echo "<section class='postContent'>
                                                            <img src='./posts/post_picture/" . $commentaire["nom_image"] . "' alt='imagePost' />
                                                            <br />
                                                            <p>" . $commentaire["texte"] . "</p>
                                                        </section>";
                                                        } else {
                                                            echo "<section class='postContent'>
                                                            <p>" . $commentaire["texte"] . "</p>
                                                        </section>";
                                                        }

                                                        echo "<footer>
                                                        <section class='postFooter'>";

                                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                                            echo "<footer>
                                                            <section class='postFooter'>
                                                                <ul>
                                                                    <li class='partage'>
                                                                        <button class='shareButton' onclick='share(this)'>
                                                                        </button>
                                                                        <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                    </li>
                                                                    <li>
                                                                        <button onclick='ouvrirModif(this)'>
                                                                            <svg fill='#000000' width='22' height='19' viewBox='-2.5 -2.5 24 24' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin'>
                                                                                <path d='M12.238 5.472 3.2 14.51l-.591 2.016 1.975-.571 9.068-9.068-1.414-1.415zM13.78 3.93l1.414 1.414 1.318-1.318a.5.5 0 0 0 0-.707l-.708-.707a.5.5 0 0 0-.707 0L13.781 3.93zm3.439-2.732.707.707a2.5 2.5 0 0 1 0 3.535L5.634 17.733l-4.22 1.22a1 1 0 0 1-1.237-1.241l1.248-4.255 12.26-12.26a2.5 2.5 0 0 1 3.535 0z'/>
                                                                            </svg>
                                                                        </button>
                                                                    </li>
                                                                    <li>
                                                                        <button onclick='supprimerPost(this)'>
                                                                            <svg fill='#000000' width='22' height='19' viewBox='0 0 36 36' version='1.1'  preserveAspectRatio='xMidYMid meet' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
                                                                                <path class='clr-i-solid clr-i-solid-path-1' d='M6,9V31a2.93,2.93,0,0,0,2.86,3H27.09A2.93,2.93,0,0,0,30,31V9Zm9,20H13V14h2Zm8,0H21V14h2Z'></path>
                                                                                <path class='clr-i-solid clr-i-solid-path-2' d='M30.73,5H23V4A2,2,0,0,0,21,2h-6.2A2,2,0,0,0,13,4V5H5A1,1,0,1,0,5,7H30.73a1,1,0,0,0,0-2Z'></path>
                                                                                <rect x='0' y='0' width='36' height='36' fill-opacity='0'/>
                                                                            </svg>
                                                                        </button>
                                                                    </li>
                                                                </ul>
                                                            </section>
                                                            <article class='modification'>
                                                                <header>
                                                                    <form enctype='multipart/form-data' class='modifForm'>
                                                                        <label for='postText'>Texte Post:</label>
                                                                        <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                                        <br /> <label for='image'>Image :</label>
                                                                        <input class='imageModification' type='file' name='image'>
                                                                        <br>
                                                                    </form>
                                                                
                                                                    <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                                </header>
                                                                <footer>
                                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                                    <h1 class='modifPreview'>
                                                                        SENT: <span></span>
                                                                        <img src='#' alt='rien' />
                                                                    </h1>
                                                                </footer>
                                                            </article>
                                                        </footer>";
                                                        } else {
                                                            echo "<footer>
                                                            <section class='postFooter'>
                                                                <ul>
                                                                    <li class='partage'>
                                                                        <button class='shareButton' onclick='share(this)'>
                                                                        </button>
                                                                        <p>" . $commentaire["nombreDePartage"] . "</p>
                                                                    </li>
                                                                </ul>
                                                            </section>
                                                        </footer>";
                                                        }

                                                        echo "</article>";
                                                    }
                                                }
                                            }

                                            echo "<article class='commentFormSection'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='commentForm'>
                                                        Commentaire:
                                                        <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageCommentaire' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='commentPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </section>";
                                        } else {
                                            echo "<section class='comment'>
                                            <article class='commentFormSection'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='commentForm'>
                                                        Commentaire:
                                                        <textarea class='texteCommentaire' name='texteCommentaire' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageCommentaire' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitCommentForm' onclick='soumettreCommentaire(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='commentPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </section>";
                                        }

                                        if ($_SESSION["utilisateur"] === $commentaire["auteur"]) {
                                            echo "<article class='modification'>
                                                <header>
                                                    <form enctype='multipart/form-data' class='modifForm'>
                                                        <label for='postText'>Texte Post:</label>
                                                        <textarea class='texteModification' name='texteModification' rows='5' cols='40'></textarea>
                                                        <br /> <label for='image'>Image :</label>
                                                        <input class='imageModification' type='file' name='image'>
                                                        <br>
                                                    </form>
                                                
                                                    <button class='submitModifForm' onclick='soumettreModification(this)'><span>submit the form!</span></button>
                                                </header>
                                                <footer>
                                                    <!-- JUST SOME FEEDBACK TO LET US KNOW WHAT IS SENT -->
                                                    <h1 class='modifPreview'>
                                                        SENT: <span></span>
                                                        <img src='#' alt='rien' />
                                                    </h1>
                                                </footer>
                                            </article>
                                        </footer>";
                                        } else {
                                            echo "</footer>";
                                        }
                                        echo "</article>";
                                    }
                                }
                            }
                        }
                    } catch (Exception $e) {
                        die($e->getMessage());
                    }
                    ?>
                </section>
            </section>
        </section>
    </body>
</html>