<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    try {
        session_start();

        $_SESSION["miaou"] = "en effet";

        echo "tout ok";
    } catch (Exception $e) {
        echo "". $e->getMessage() ."";
    }
    ?>
</body>
</html>