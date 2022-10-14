const textarea = document.querySelector('textarea');
const disp = document.getElementById('disp');
const trig_enabled = document.getElementById("trig_enabled");

var efmr;

function writeTextArea(string, n, trig=false) {
    var curPos = textarea.selectionStart;
    var endPos = curPos + string.length;
    textarea.value = textarea.value.slice(0, curPos) + string + textarea.value.slice(curPos);
    textarea.focus();
    textarea.selectionEnd = endPos - n;
    update();
    if (trig == true && trig_enabled.checked) {
        writeTextArea('\\left (  \\right ) ', 10)
    }
}

function update() {
    disp.innerHTML = "\\(" + textarea.value + "\\)";
    MathJax.typeset();
}

function send(){
    document.getElementById("inputTxt").value = textarea.value;

    let formulario = new FormData(document.getElementById("formulario"))
    if(textarea.value != ''){

        fetch("sql.php", {
            method:"POST",
            body:formulario
        })
        .then(res => res.json())
        .then(data => {
            if(data == 'true'){
                textarea.value = "";
            }else {
                alert("Algo falló");
            }
        });
    }
}