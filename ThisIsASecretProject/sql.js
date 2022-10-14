document.getElementById('formulario').addEventListener('submit', function(e){
    e.preventDefault();

    let formulario = new FormData(document.getElementById("formulario"));

    if(document.getElementById('url').value != ''){

        fetch("sql.php", {
            method:"POST",
            body:formulario
        })
        .then(res => res.json())
        .then(data => {
            if(data == 'true'){
                document.getElementById("url").value = "";
            }else {
                alert("Algo falló");
            }
        });
    }
});