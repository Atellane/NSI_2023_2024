<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>créer BDD</title>
    </head>
    <body>
        <?php
        try {
            $dbh = new PDO('mysql:host=localhost;port=50765;dbname=eouzan', 'azure', '6#vWHD_$');
            $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            $utilisateurs = 'CREATE TABLE utilisateurs(
                username VARCHAR(255) PRIMARY KEY NOT NULL,
                mot_de_passe VARCHAR(255) NOT NULL,
                nom_photo_de_profil VARCHAR(255) NOT NULL,
                nombre_abonne INT NOT NULL
            )';
            
            $dbh->exec($utilisateurs);
            
            $sAbonneA= 'CREATE TABLE sAbonneA(
                id VARCHAR(510) PRIMARY KEY NOT NULL,
                abonne VARCHAR(255) NOT NULL,
                abonnement VARCHAR(255) NOT NULL,
                CONSTRAINT abonne FOREIGN KEY (abonne) REFERENCES utilisateurs(username) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT abonnement FOREIGN KEY (abonnement) REFERENCES utilisateurs(username) ON DELETE CASCADE ON UPDATE CASCADE
            )';

            $dbh->exec($sAbonneA);

            $message = 'CREATE TABLE messages(
                signatureMessage VARCHAR(275) PRIMARY KEY NOT NULL,
                auteur VARCHAR(255) NOT NULL,
                dateEtHeure DATETIME NOT NULL,
                nom_image VARCHAR(255),
                texte VARCHAR(4000) NOT NULL,
                nombreDePartage INT NOT NULL,
                nombreDeCommentaire INT NOT NULL,
                CONSTRAINT auteur FOREIGN KEY (auteur) REFERENCES utilisateurs(username) ON DELETE CASCADE ON UPDATE CASCADE

            )';

            $dbh->exec($message);

            $partage = 'CREATE TABLE partage(
                id VARCHAR(530) PRIMARY KEY NOT NULL,
                utilisateur VARCHAR(255) NOT NULL,
                messagepartage VARCHAR(275) NOT NULL,
                CONSTRAINT utilisateur FOREIGN KEY (utilisateur) REFERENCES utilisateurs(username) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT messagepartage FOREIGN KEY (messagepartage) REFERENCES messages(signatureMessage) ON DELETE CASCADE ON UPDATE CASCADE
            )';

            $dbh->exec($partage);

            $commente = 'CREATE TABLE commente(
                id VARCHAR(550) PRIMARY KEY NOT NULL,
                messageCommente VARCHAR(275) NOT NULL,
                commentaire VARCHAR(275) NOT NULL,
                CONSTRAINT messageCommente FOREIGN KEY (messageCommente) REFERENCES messages(signatureMessage) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT commentaire FOREIGN KEY (commentaire) REFERENCES messages(signatureMessage) ON DELETE CASCADE ON UPDATE CASCADE
            )';

            $dbh->exec($commente);

            echo "tout OK";
        } catch (PDOException $e) {
            die("Erreur !: " . $e->getMessage());
        }
        ?>
    </body>
</html>