document.getElementById('formData').addEventListener('submit', predictSpam)

function predictSpam (e) {
    e.preventDefault ()

    let text = document.getElementById('textarea_1').value

    fetch ('http://localhost:5000', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
            'firstname' : text
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerHTML = `<div>${data.output}</div>`
    })
}