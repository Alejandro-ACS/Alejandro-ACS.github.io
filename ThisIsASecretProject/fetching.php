<?php
$conn = mysqli_connect("localhost", "root", "", "urls");
$sql = "SELECT * FROM `enlaces`;";
    
$result = $conn->query($sql);
?>