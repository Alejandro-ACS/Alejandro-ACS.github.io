<?php

$url = isset($_POST['inputTxt']) ? $_POST['inputTxt'] : '';

try {
    $conexion = new PDO('mysql:host=localhost;port=3306;dbname=eqts', 'root', '');
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);

    $pdo = $conexion->prepare('INSERT INTO equats(Text) VALUES(?)');
    $pdo->bindParam(1,$url);

    $pdo->execute() or die(print($pdo->errorInfo()));

    echo json_encode('true');

} catch (PDOException $error){
    echo $error->getMessage();
    die();
}