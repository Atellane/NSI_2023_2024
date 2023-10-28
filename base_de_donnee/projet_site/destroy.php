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
            
            $utilisateurs = 'DROP TABLE utilisateurs';
            
            $dbh->exec($utilisateurs);
            
            $sAbonneA= 'DROP TABLE sAbonneA';

            $dbh->exec($sAbonneA);

            $partage = 'DROP TABLE partage';

            $dbh->exec($partage);

            $message = 'DROP TABLE messages';

            $dbh->exec($message);

            $commente = 'DROP TABLE commente';

            $dbh->exec($commente);

            echo "tout OK";
        } catch (PDOException $e) {
            die("Erreur !: " . $e->getMessage());
        }
        ?>
    </body>
</html>