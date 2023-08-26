from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def basic ():
    if request.method == 'POST':
        text = request.form['firstname']
        return render_template ('index.html', name=text)
    return render_template ('index.html')

if __name__ == '__main__':
    app.run(debug=True)