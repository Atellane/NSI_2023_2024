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
            
            $utilisateurs = 'CREATE TABLE utilisateurs(
                username VARCHAR(255) PRIMARY KEY,
                mot_de_passe VARCHAR(255) NOT NULL,
                emplacement_photo_de_profil VARCHAR(255),
                ON DELETE CASCADE,
                ON UPDATE CASCADE,
            )';
            
            $dbh->exec($utilisateurs);
            
            $sAbonneA= 'CREATE TABLE sAbonneA(
                id VARCHAR(510) PRIMARY KEY,
                abonné VARCHAR(255),
                abonnement VARCHAR(255),
                CONSTRAINT abonné FOREIGN KEY (abonné) REFERENCES utilisateurs(username),
                CONSTRAINT abonnement FOREIGN KEY (abonnement) REFERENCES utilisateurs(username),
                ON DELETE CASCADE,
                ON UPDATE CASCADE,
            )';

            $dbh->exec($sAbonneA);

            $partage = 'CREATE TABLE partage(
                id VARCHAR(530) PRIMARY KEY,
                utilisateur VARCHAR(255),
                messagepartage VARCHAR(275),
                CONSTRAINT utilisateur FOREIGN KEY (utilisateur) REFERENCES utilisateurs(username),
                CONSTRAINT messagelike FOREIGN KEY (messagepartage) REFERENCES messages(signatureMessage),
                ON DELETE CASCADE,
                ON UPDATE CASCADE,
            )';

            $dbh->exec($partage);

            $message = 'CREATE TABLE messages(
                signatureMessage VARCHAR(275) PRIMARY KEY,
                autheur VARCHAR(255),
                dateEtHeure TIMESTAMP,
                emplacementImage VARCHAR(255),
                texte VARCHAR(1000),
                nombreDeLike INT,
                nombreDePartage INT,
                CONSTRAINT autheur FOREIGN KEY (autheur) REFERENCES utilisateurs(username),
                ON DELETE CASCADE,
                ON UPDATE CASCADE,
            )';

            $dbh->exec($message);

            $commente = 'CREATE TABLE commente(
                id VARCHAR(550) PRIMARY KEY,
                messageCommente VARCHAR(275),
                commentaire VARCHAR(275),
                CONSTRAINT messageCommente FOREIGN KEY (messageCommente) REFERENCES messages(signatureMessage),
                CONSTRAINT commentaire FOREIGN KEY (commentaire) REFERENCES messages(signatureMessage),
                ON DELETE CASCADE,
                ON UPDATE CASCADE,
            )';

            $dbh->exec($commente);

            echo "tout OK";
        } catch (PDOException $e) {
            die("Erreur !: " . $e->getMessage());
        }
        ?>
    </body>
</html>