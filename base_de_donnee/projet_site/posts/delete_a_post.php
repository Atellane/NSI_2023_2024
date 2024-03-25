<?php
try {
    $dbh = new PDO('mysql:host=localhost;port=50929;dbname=eouzan', 'azure', '6#vWHD_$');
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $postId = $_POST["post"];

    $sqlRecupIdCommentaires = "SELECT commentaire
                               FROM commente
                               WHERE messageCommente = :postId";
    $statement = $dbh->prepare($sqlRecupIdCommentaires);
    $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
    $statement->execute();
    $idCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);

    foreach ($idCommentaires as $idCommentaire) {

        $sqlDeleteComments = "DELETE FROM messages WHERE messages.signatureMessage = :postId";
        $statementDeleteComments = $dbh->prepare($sqlDeleteComments);
        $statementDeleteComments->bindParam(":postId", $idCommentaire["commentaire"], PDO::PARAM_STR);
        $statementDeleteComments->execute();

        $sql = "SELECT nombreDeCommentaire FROM messages WHERE signatureMessage = :postId";
        $statement = $dbh->prepare($sql);
        $statement->bindParam("postId", $postId, PDO::PARAM_STR);
        $statement->execute();
        $nombreDeCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);
        $nombreDeCommentaire = $nombreDeCommentaires[0]["nombreDeCommentaire"];
        $nombreDeCommentaire -= 1;
    
        $sql = "UPDATE messages
                SET nombreDeCommentaire = :nombreDeCommentaire
                WHERE signatureMessage = :postId";
        $statement = $dbh->prepare($sql);
        $statement->bindParam(":nombreDeCommentaire", $nombreDeCommentaire, PDO::PARAM_STR);
        $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
        $statement->execute();
    
        $sql = "SELECT nombreDeCommentaire FROM messages WHERE signatureMessage = :postId";
        $statement = $dbh->prepare($sql);
        $statement->bindParam("postId", $postId, PDO::PARAM_STR);
        $statement->execute();
        $nombreDeCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);
        $nombreDeCommentaire = $nombreDeCommentaires[0]["nombreDeCommentaire"];
    }

    $sql = "SELECT messageCommente
            FROM commente
            WHERE commentaire = :postId";
    $statement = $dbh->prepare($sql);
    $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
    $statement->execute();
    $messageCommentes = $statement->fetchAll(PDO::FETCH_ASSOC);
    $messageCommente = $messageCommentes[0]["messageCommente"];

    if ($statement->rowCount() > 0) {
        $sql = "SELECT nombreDeCommentaire FROM messages WHERE signatureMessage = :postId";
        $statement = $dbh->prepare($sql);
        $statement->bindParam("postId", $messageCommente, PDO::PARAM_STR);
        $statement->execute();
        $nombreDeCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);
        $nombreDeCommentaire = $nombreDeCommentaires[0]["nombreDeCommentaire"];
        $nombreDeCommentaire -= 1;
    
        $sql = "UPDATE messages
                SET nombreDeCommentaire = :nombreDeCommentaire
                WHERE signatureMessage = :postId";
        $statement = $dbh->prepare($sql);
        $statement->bindParam(":nombreDeCommentaire", $nombreDeCommentaire, PDO::PARAM_STR);
        $statement->bindParam(":postId", $messageCommente, PDO::PARAM_STR);
        $statement->execute();
    
        $sql = "SELECT nombreDeCommentaire FROM messages WHERE signatureMessage = :postId";
        $statement = $dbh->prepare($sql);
        $statement->bindParam("postId", $postId, PDO::PARAM_STR);
        $statement->execute();
        $nombreDeCommentaires = $statement->fetchAll(PDO::FETCH_ASSOC);
        $nombreDeCommentaire = $nombreDeCommentaires[0]["nombreDeCommentaire"];
    }

    // Suppression des commentaires liés au message
    $sqlDeleteComments = "DELETE FROM commente WHERE messageCommente = :postId";
    $statementDeleteComments = $dbh->prepare($sqlDeleteComments);
    $statementDeleteComments->bindParam(':postId', $postId, PDO::PARAM_STR);
    $statementDeleteComments->execute();

    // Suppression du message
    $sqlDeleteMessage = "DELETE FROM messages WHERE signatureMessage = :postId";
    $statementDeleteMessage = $dbh->prepare($sqlDeleteMessage);
    $statementDeleteMessage->bindParam(':postId', $postId, PDO::PARAM_STR);
    $statementDeleteMessage->execute();
} catch (Exception $e) {
    die("". $e->getMessage());
}
?>