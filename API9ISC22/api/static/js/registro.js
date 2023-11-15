const formulario = document.getElementById('userForm')

formulario.addEventListener('submit', function(evento){
    evento.preventDefault()

    const datosFormulario = new FormData(evento.target)
    
    fetch('https://geobot.onrender.com/registro/', {
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