const formulario = document.getElementById('userForm')

formulario.addEventListener('submit', function(evento){
    evento.preventDefault()

    const datosFormulario = new FormData(evento.target)
    
    fetch('http://127.0.0.1:8000/crear/', {
        method: 'POST',
        body: datosFormulario
    })

    .then(response =>{
        if(!response.ok) throw new Error('Error en la solicitud')
        console.log(response.status)
        return response.json()
    })

    .then(response => console.log(response))
    .catch(error => console.log(error))
})