import warnings
warnings.filterwarnings("ignore")

from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
import joblib
from src.text_Classification_ML.pipeline.prediction import PredictionPipeline



app = Flask(__name__) # initializing a flask app


@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def predict():
    
    model = joblib.load(filename='artifacts/model_trainer/model.joblib')

   
    vectorizer = joblib.load(filename='artifacts/data_transformation/tfidf_vectorizer.pkl')

    
    review_text = request.form['review']

    
    review_vector = vectorizer.transform([review_text])

    
    prediction = model.predict(review_vector)

    # Defining the prediction
    if prediction == 1:
        result = "Negative"
    elif prediction == 2:
        result = "Neutral"
    else:
        result = "Positive"

    return render_template('index.html', result=result)



if __name__ == '__main__':
    app.run(debug=True, port=8000)


