// Respuestas correctas
let correctas = [2,1,3,1,2];

let opcion_elegida = [];
let cantidad_correctas = 0;

function respuesta (numero_pregunta, seleccionada){
    opcion_elegida[numero_pregunta] = seleccionada.value;
    id = "p" + numero_pregunta;
    labels = document.getElementById(id).childNodes;
    labels[3].style.backgroundColor = "White";
    labels[5].style.backgroundColor = "White";
    labels[7].style.backgroundColor = "White";
    seleccionada.parentNode.style.backgroundColor = "#a06c3f";
}

function validarRespuestas(){
    cantidad_correctas = 0;
    for(i=0; i < correctas.length; i++){
        if(correctas[i] == opcion_elegida[i]){
            cantidad_correctas++;
        }
    }
    document.getElementById("resultado").innerHTML = cantidad_correctas;
}