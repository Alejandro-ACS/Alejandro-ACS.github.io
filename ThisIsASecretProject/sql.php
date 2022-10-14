<?php

$url = isset($_POST['url']) ? $_POST['url'] : '';

try {
    $conexion = new PDO('mysql:host=localhost;port=3306;dbname=urls', 'root', '');
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);

    $pdo = $conexion->prepare('INSERT INTO enlaces(url) VALUES(?)');
    $pdo->bindParam(1,$url);

    $pdo->execute() or die(print($pdo->errorInfo()));

    echo json_encode('true');

} catch (PDOException $error){
    echo $error->getMessage();
    die();
}