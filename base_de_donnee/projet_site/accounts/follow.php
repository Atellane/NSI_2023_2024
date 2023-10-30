<?php
try {
    $dbh = new PDO('mysql:host=localhost;port=50765;dbname=eouzan', 'azure', '6#vWHD_$');
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    session_start();
    $username = $_SESSION["utilisateur"];
    $celuiQuiSAbonne = $_POST["abonne"];
    $abonnement = $_POST["abonnement"];
    echo "" . $celuiQuiSAbonne . " " . $abonnement . " " . $_SESSION["miaou"] . "";
        
    session_destroy();

} catch (PDOException $e) {
    die("Erreur !: " . $e->getMessage());
}
?>