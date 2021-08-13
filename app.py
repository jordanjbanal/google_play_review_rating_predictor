import numpy as np
from flask import Flask, request, render_template
import joblib


app = Flask(__name__)
model = joblib.load(open('assets/model.pkl', 'rb'))
cv = joblib.load(open('assets/cv.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        text = request.form['Review']
        data = [text]
        vectorizer = cv.transform(data).toarray()
        prediction = model.predict(vectorizer)
        return render_template('index.html', prediction_text=f'The estimated rating for this review is {int(prediction)} stars.')


if __name__ == "__main__":
    app.run(debug=True)
