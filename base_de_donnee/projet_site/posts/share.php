<?php
try {
    session_start();
    error_reporting(E_ALL);
    ini_set('display_errors', 1);
    $dbh = new PDO('mysql:host=localhost;port=50765;dbname=eouzan', 'azure', '6#vWHD_$');
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $postId = $_POST["post"];
    $sql = "SELECT nombreDePartage, signatureMessage
            FROM messages
            WHERE signatureMessage = :postId";

    $statement = $dbh->prepare($sql);
    $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
    $statement->execute();
    $messages = $statement->fetchAll(PDO::FETCH_ASSOC);
    $nombreDePartage = $messages[0]["nombreDePartage"];
    $signatureMessage = $messages[0]["signatureMessage"];

    $id = $_SESSION["utilisateur"] . $signatureMessage;

    if ($_POST["action"] === "create") {
        $nombreDePartage += 1;
        $sql = "UPDATE messages
                SET nombreDePartage = :nombreDePartage
                WHERE signatureMessage = :postId";
        $statement = $dbh->prepare($sql);
        $statement->bindParam(":nombreDePartage", $nombreDePartage, PDO::PARAM_INT);
        $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
        $statement->execute();
        $sql = "INSERT INTO partage (id, utilisateur, messagepartage) VALUES (:partageId, :username, :postId)";
        $statement = $dbh->prepare($sql);
        $statement->bindParam(":partageId", $id, PDO::PARAM_STR);
        $statement->bindParam(":username", $_SESSION["utilisateur"], PDO::PARAM_STR);
        $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
        $statement->execute();
    } else {
        $nombreDePartage -= 1;
        $sql = "UPDATE messages
                SET nombreDePartage = :nombreDePartage
                WHERE signatureMessage = :postId";
        $statement = $dbh->prepare($sql);
        $statement->bindParam(":nombreDePartage", $nombreDePartage, PDO::PARAM_INT);
        $statement->bindParam(":postId", $postId, PDO::PARAM_STR);
        $statement->execute();
        $sqlDeletePartage = "DELETE FROM partage WHERE id = :partageId";
        $statementDeletePartage = $dbh->prepare($sqlDeletePartage);
        $statementDeletePartage->bindParam(':partageId', $id, PDO::PARAM_STR);
        $statementDeletePartage->execute();
    }
} catch (Exception $e) {
    die("". $e->getMessage());
}
?>