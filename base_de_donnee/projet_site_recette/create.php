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
            $dbh = new PDO('mysql:host=localhost;port=50929;dbname=eouzan', 'azure', '6#vWHD_$');
            $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            $livres = 'CREATE TABLE livres(
                idLivre INT PRIMARY KEY NOT NULL,
                titre VARCHAR(255) NOT NULL,
                auteur CHAR(30) NOT NULL,
                dateDePublication DATETIME NOT NULL
            )';

            $dbh->exec($livres);

            $recettes = 'CREATE TABLE recettes(
                idRecette CHAR(255) PRIMARY KEY NOT NULL,
                livre INT NULL,
                CONSTRAINT livre FOREIGN KEY (livre) REFERENCES livres(idLivre) ON DELETE CASCADE ON UPDATE CASCADE,
                numeroDePage INT,
                nom VARCHAR(255) NOT NULL,
                nomDuChef VARCHAR(255) NOT NULL,
                tempsDePreparation INT NOT NULL,
                tempsDeCuisson INT NOT NULL,
                ingredients TEXT NOT NULL
            )';

            $dbh->exec($recettes);

            echo "tout OK";
        } catch (PDOException $e) {
            die("Erreur !: " . $e->getMessage());
        }
        ?>
    </body>
</html>