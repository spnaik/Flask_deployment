import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    fruit_dict = {1:'apple',2:'mandarin',3:'orange',4:'lemon'}
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction[0]
    return render_template('index.html', prediction_text='The fruit is predicted to be {}'.format(fruit_dict[output]))


if __name__ == "__main__":
    app.run(debug=True)