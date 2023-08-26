from pickle5 import pickle

with open ('./savedModels/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load (handle)

from tensorflow.python.keras.models import load_model
model = load_model ('./savedModels/model.h5')

from tensorflow.python.keras.preprocessing.sequence import pad_sequences

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route ('/', methods = ['POST'])
def basic ():
    text = request.json['text']
    X_test = tokenizer.texts_to_sequences([text])
    padded_text = pad_sequences (X_test, padding='post', maxlen=50)
    y_pred = model.predict (padded_text)
    if y_pred < 0.75:
        response = 'No_Spam'
    else:
        response = 'Spam'
    return jsonify({
        'response' : response
    })

if __name__ == '__main__':
    app.run (debug=True)