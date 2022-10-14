<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <link rel="stylesheet" href="style2.css"></link>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.2/assets/css/docs.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
    <script id="MathJax-script" async
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <script src="https://code.jquery.com/jquery-latest.min.js"></script>
</head>
<body>
    <div id="formulas">

    </div>
    <script>
        var ints = []
        <?php

        $conexion = mysqli_connect('localhost', 'root', '', 'eqts');

        $sql = "SELECT * FROM equats";

        $result = mysqli_query($conexion,$sql);

        while($mostrar=mysqli_fetch_array($result)){

        ?>

        ints.push(<?php echo json_encode($mostrar); ?>);
        
        <?php
        }
        ?>
    </script>
    <script>
        var myDiv = document.getElementById("formulas");
        for(i=0; i<ints.length; i++){
            var mathText = document.createElement("a");
            var divCol = document.createElement("div");
            var divCol2 = document.createElement("div");
            mathText.innerHTML = "\\(\\color{rgb(220, 63, 89)} " + ints[i][1].split("=")[0] + "\\)";

            divCol.className = "collapse collapse-vertical";
            divCol.id = "collapse" + i;
            
            divCol2.className = "card card-body";
            divCol2.innerHTML = "\\(\\color{rgb(220, 63, 89)} " + ints[i][1] + " \\)";
            
            mathText.setAttribute("data-bs-toggle", "collapse");
            mathText.setAttribute("href", "#collapse" + i);
            mathText.setAttribute("aria-expanded", "false");

            if (i == ints.length-1) {
                mathText.style = "margin-bottom:1rem;";
                divCol2.style = "margin-bottom:2rem;";
            }

            myDiv.appendChild(mathText);
            divCol.appendChild(divCol2);
            myDiv.appendChild(divCol);
        }
    </script>
    <script>MathJax.typeset();</script>
</body>
</html>