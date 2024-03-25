<?php
try {
    session_start();
    $dbh = new PDO('mysql:host=localhost;port=50929;dbname=eouzan', 'azure', '6#vWHD_$');
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $nombreDePartage = 0;
    $nombreDeCommentaire = 0;

    $postText = $_POST["texteCommentaire"];

    date_default_timezone_set('Europe/Paris');
    $dateEtHeure = date('Y-m-d H:i:s'); // Format DATETIME requis pour MySQL

    $signatureMessage = $_SESSION["utilisateur"] . $dateEtHeure;
    $idComment = $_POST["idDuPost"] . $signatureMessage;

    $postPicture = $_FILES["imageCommentaire"];

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

    $sql = "INSERT INTO commente (id, messageCommente, commentaire) VALUES (:idComment, :messageCommente, :commentaire)";

    $statement = $dbh->prepare($sql);
    $statement->bindParam(":idComment", $idComment, PDO::PARAM_STR);
    $statement->bindParam(":messageCommente", $_POST["idDuPost"], PDO::PARAM_STR);
    $statement->bindParam(":commentaire", $signatureMessage, PDO::PARAM_STR);
    $statement->execute();

    $sql = "SELECT nombreDeCommentaire FROM messages WHERE signatureMessage = :postId";
    $statement = $dbh->prepare($sql);
    $statement->bindParam("postId", $_POST["idDuPost"], PDO::PARAM_STR);
    $statement->execute();
    $nombreDeCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);
    $nombreDeCommentaire = $nombreDeCommentaires[0]["nombreDeCommentaire"];
    $nombreDeCommentaire += 1;

    $sql = "UPDATE messages
            SET nombreDeCommentaire = :nombreDeCommentaire
            WHERE signatureMessage = :postId";
    $statement = $dbh->prepare($sql);
    $statement->bindParam(":nombreDeCommentaire", $nombreDeCommentaire, PDO::PARAM_STR);
    $statement->bindParam(":postId", $_POST["idDuPost"], PDO::PARAM_STR);
    $statement->execute();

    $sql = "SELECT nombreDeCommentaire FROM messages WHERE signatureMessage = :postId";
    $statement = $dbh->prepare($sql);
    $statement->bindParam("postId", $_POST["idDuPost"], PDO::PARAM_STR);
    $statement->execute();
    $nombreDeCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);
    $nombreDeCommentaire = $nombreDeCommentaires[0]["nombreDeCommentaire"];
} catch (Exception $e) {
    die("". $e->getMessage());
}
?>