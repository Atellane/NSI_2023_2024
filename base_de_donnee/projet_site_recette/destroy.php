<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>détruire BDD</title>
    </head>
    <body>
        <?php
        try {
            $dbh = new PDO('mysql:host=localhost;port=50929;dbname=eouzan', 'azure', '6#vWHD_$');
            $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            $deleteForeignKeys = 'ALTER TABLE recettes DROP FOREIGN KEY livre';
            $dbh->exec($deleteForeignKeys);
            $recettes= 'DROP TABLE recettes';
            $dbh->exec($recettes);

            $livres = 'DROP TABLE livres';
            $dbh->exec($livres);

            echo "tout OK";
        } catch (PDOException $e) {
            die("Erreur !: " . $e->getMessage());
        }
        ?>
    </body>
</html>