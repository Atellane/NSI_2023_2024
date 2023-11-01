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
            $dbh = new PDO('mysql:host=localhost;port=50765;dbname=eouzan', 'azure', '6#vWHD_$');
            $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            $deleteForeignKeys = 'ALTER TABLE sAbonneA DROP FOREIGN KEY abonne';
            $dbh->exec($deleteForeignKeys);
            $deleteForeignKeys = 'ALTER TABLE sAbonneA DROP FOREIGN KEY abonnement';
            $dbh->exec($deleteForeignKeys);
            $sAbonneA= 'DROP TABLE sAbonneA';
            $dbh->exec($sAbonneA);

            $deleteForeignKeys = 'ALTER TABLE partage DROP FOREIGN KEY utilisateur';
            $dbh->exec($deleteForeignKeys);
            $deleteForeignKeys = 'ALTER TABLE partage DROP FOREIGN KEY messagepartage';
            $dbh->exec($deleteForeignKeys);
            $partage = "DROP TABLE partage";
            $dbh->exec($partage);

            $deleteForeignKeys = 'ALTER TABLE commente DROP FOREIGN KEY messageCommente';
            $dbh->exec($deleteForeignKeys);
            $deleteForeignKeys = 'ALTER TABLE commente DROP FOREIGN KEY commentaire';
            $dbh->exec($deleteForeignKeys);
            $commente = "DROP TABLE commente";
            $dbh->exec($commente);

            $deleteForeignKeys = 'ALTER TABLE messages DROP FOREIGN KEY auteur';
            $dbh->exec($deleteForeignKeys);
            $message = "DROP TABLE messages";
            $dbh->exec($message);

            $utilisateurs = 'DROP TABLE utilisateurs';
            $dbh->exec($utilisateurs);

            echo "tout OK";
        } catch (PDOException $e) {
            die("Erreur !: " . $e->getMessage());
        }
        ?>
    </body>
</html>