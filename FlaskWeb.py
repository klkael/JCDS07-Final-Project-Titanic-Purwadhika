import pandas as pd
import numpy as np
from flask import Flask, render_template, request, send_from_directory
import requests
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template("predict.html")

@app.route('/result', methods=['POST','GET'])
def result():
    kota = ['cherbourg','queenstown','southampton']
    sexx = ['male','female']
    inputuser = request.form.to_dict()
    age = inputuser['Age']
    # sex = inputuser['Sex']
    if inputuser['Sex'].lower() == 'male' :
        sex = 1
    else:
        sex = 0
    if inputuser['Sex'].lower() not in sexx:
        return render_template('errorsex.html')
    sibsp = inputuser['SibSp']
    pclass = inputuser['Pclass']
    parch = inputuser['Parch']
    # embarked = inputuser['Embarked']
    if inputuser['Embarked'].lower() == 'cherbourg':
        embarked = 0
    elif inputuser['Embarked'].lower() == 'queenstown':
        embarked = 1
    else:
        embarked = 2
    if inputuser['Embarked'].lower() not in kota:
        return render_template('errorkota.html')
    fare = inputuser['Fare']
    prediksi = model.predict([[age,sex,pclass,sibsp,parch,embarked,fare]])
    if prediksi == 1:
        predik = "Look's Like You're Manage To Go To Emergency Ship so You're Safe !"
    else:
        predik = "Oh No ! You Can't Reach The Emergency Ship For a Reason, Guess You Will Sink Together With Titanic Ship"
    return render_template("result.html",age=age,sex=sex,sibsp=sibsp,parch=parch,embarked=embarked,fare=fare,pred=predik)

@app.route('/visual')
def visual():
    return render_template('visual.html')

if __name__ == '__main__':
    model = joblib.load('modelprediksijoblib')

    app.run(debug=True,port=6060)

