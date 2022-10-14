<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            background: #1b1b1b;
        }
    </style>
</head>
<body>
    <script>
        var urls = []
        <?php

        $conexion = mysqli_connect('localhost', 'root', '', 'eqts');

        $sql = "SELECT * FROM equats";

        $result = mysqli_query($conexion,$sql);

        while($mostrar=mysqli_fetch_array($result)){

        ?>

        urls.push(<?php echo json_encode($mostrar); ?>);
        
        <?php
        }
        ?>
    </script>
    <script>
        function tableCreate() {
        //body reference 
        var body = document.getElementsByTagName("body")[0];

        // create elements <table> and a <tbody>
        var tbl = document.createElement("table");
        var tblBody = document.createElement("tbody");

        // cells creation
        var a = 0;
        for (var j = 0; j < Math.ceil((urls.length)/4); j++) {
            // table row creation
            var row = document.createElement("tr");

            if ((j+1)*4 <= urls.length){
                a = 4;
            } else{
                a = 4-((j+1)*4-urls.length);
            }

            for (var i = 0; i < a; i++) {
            // create element <td> and text node 
            //Make text node the contents of <td> element
            // put <td> at end of the table row
            var cell = document.createElement("td");
            var cellText = document.createElement('iframe');
            cellText.src = urls[j*4+i]['url'];
            cellText.setAttribute("allowfullscreen", true)

            cell.appendChild(cellText);
            row.appendChild(cell);
            }

            //row added to end of table body
            tblBody.appendChild(row);
        }

        // append the <tbody> inside the <table>
        tbl.appendChild(tblBody);
        // put <table> in the <body>
        body.appendChild(tbl);
        // tbl border attribute to 
        tbl.setAttribute("width", "100%");
        }
        tableCreate();
    </script>
</body>
</html>