<?php
try {
    $dbh = new PDO('mysql:host=localhost;port=50765;dbname=eouzan', 'azure', '6#vWHD_$');
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $postId = $_POST["idDuPost"];
    $texteModif = $_POST["texteModification"];
    date_default_timezone_set('Europe/Paris');
    $dateEtHeure = date('Y-m-d H:i:s'); // Format DATETIME requis pour MySQL

    $postPicture = $_FILES["imageModification"];
    
    if (!(empty($postPicture["name"]))) {
        $sql = "SELECT messages.nom_image
        FROM messages
        WHERE messages.signatureMessage = :postId";

        $statement = $dbh->prepare($sql);
        $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
        $statement->execute();
        $nomImages = $statement->fetchAll(PDO::FETCH_ASSOC);
        $nomImage = "./post_picture/" . $nomImages[0]["nom_image"];
        unlink($nomImage);

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
        
        $sql = "UPDATE messages
                SET nom_image = :postPicture_name, texte = :texteModif, dateEtHeure = :dateEtHeure
                WHERE signatureMessage = :postId";
        
        $statement = $dbh->prepare($sql);
        $statement->bindParam(":postPicture_name", $postPicture_name, PDO::PARAM_STR);
        $statement->bindParam(":texteModif", $texteModif, PDO::PARAM_STR);
        $statement->bindParam(":dateEtHeure", $dateEtHeure, PDO::PARAM_STR);
        $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
        $statement->execute();
        die("c'est bon image !");
    } else {
        $sql = "UPDATE messages
                SET texte = :texteModif, dateEtHeure = :dateEtHeure
                WHERE signatureMessage = :postId";

        $statement = $dbh->prepare($sql);
        $statement->bindParam(":texteModif", $texteModif, PDO::PARAM_STR);
        $statement->bindParam(":dateEtHeure", $dateEtHeure, PDO::PARAM_STR);
        $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
        $statement->execute();
        die("c'est bon !");
    }
} catch (Exception $e) {
    die("". $e->getMessage());
}
?>