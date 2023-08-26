from flask import Flask, request, jsonify

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def genericFunction ():

    if request.method == 'POST':
        firstname = request.json['firstname']
        return jsonify ({
            'output' : firstname
        })

    return jsonify ({
        'firstname' : 'raunak'
    })

if __name__ == '__main__':
    app.run (debug=True)