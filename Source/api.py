from flask import Flask, render_template,request,url_for, jsonify
import os
import socket

app = Flask(__name__)

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Loading the model
from joblib import load 
with open("text_clf.joblib.z","rb") as f:
    text_clf = load(f)

# Define the route on method get
@app.route('/intent',methods=['GET'])
def api():

    try:

        query = request.json['query']

        intent = text_clf.predict(query)[0]
        proba = max(text_clf.predict_proba(query)[0])

        response = {
            "intent" : str(intent), 
            "proba" : str(proba)
        }

    except:

        response = {
            "intent" : "Error", 
            "proba" : '0'
        }
        return  jsonify(response), 400

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
