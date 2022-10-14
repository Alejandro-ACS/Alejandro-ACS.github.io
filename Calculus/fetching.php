<?php
$conn = mysqli_connect("localhost", "root", "", "eqts");
$sql = "SELECT * FROM `equats`;";
    
$result = $conn->query($sql);
?>