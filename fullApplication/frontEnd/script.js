document.getElementById('formData').addEventListener('submit', predictSpam)

function predictSpam (e) {
    e.preventDefault()

    let text = document.getElementById('textarea_1').value

    fetch('http://localhost:5000', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
            'text' : text
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.response == 'Spam') {
            document.getElementById('output').innerHTML = `<div>The message is Spam</div>`
        }
        else {
            document.getElementById('output').innerHTML = `<div>The message is not a Spam</div>`
        }
    })
}