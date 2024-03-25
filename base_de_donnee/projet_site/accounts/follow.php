<?php
try {
    $dbh = new PDO('mysql:host=localhost;port=50929;dbname=eouzan', 'azure', '6#vWHD_$');
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    session_start();
    $username = $_SESSION["utilisateur"];
    $abonnement = $_POST["abonnement"];
    $id = $username . $abonnement;
    
    if ($_POST["action"] == "create") {
        $sql = "INSERT INTO sAbonneA (id, abonne, abonnement) VALUES (:id, :username, :abonnement)";
        $statement = $dbh->prepare($sql);
        $statement->bindParam(":id", $id, PDO::PARAM_STR);
        $statement->bindParam(":username", $username, PDO::PARAM_STR);
        $statement->bindParam(":abonnement", $abonnement, PDO::PARAM_STR);
        $statement->execute();
    } else {
        $sql = "DELETE FROM sAbonneA WHERE id = :id";
        $statement = $dbh->prepare($sql);
        $statement->bindParam(":id", $id, PDO::PARAM_STR);
        $statement->execute();
    }
} catch (PDOException $e) {
    die("Erreur !: " . $e->getMessage());
}
?>