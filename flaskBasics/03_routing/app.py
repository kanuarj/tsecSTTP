from flask import Flask

app = Flask(__name__)

@app.route('/raunakjoshi')
def tsec ():
    return 'Hello World'

@app.route('/name/<name>')
def basic (name):
    return f'Hello, {name}'

if __name__ == '__main__':
    app.run (debug=True)