from flask import Flask

app = Flask(__name__)

@app.route('/')
def basic ():
    return '<h2>Hello to all TSEC students</h2>'

if __name__ == '__main__':
    app.run (debug=True)
