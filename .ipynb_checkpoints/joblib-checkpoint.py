import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
import joblib


df = pd.read_csv('Titanic.csv')
df = df.drop('Unnamed: 0',axis=1)
df['Sex'] = df['Sex'].replace({1:'Male',0:'Female'})
df['Embarked'] = df['Embarked'].replace({1:'Queensland',0:'Cherbourg',2:'Southampton'})

dfmodel = pd.read_csv('Titanic.csv')
dfmodel = dfmodel.drop(columns=['Unnamed: 0'])
xtr, xts, ytr, yts = train_test_split(dfmodel[['Age','Sex','Pclass','SibSp','Parch','Embarked','Fare']],df['Survived'],test_size=0.1)
model = RandomForestClassifier()
model.fit(xtr,ytr)
n_estimators = list(range(0,101))
criterion = ['gini','entropy']
param = {'n_estimators':n_estimators,'criterion':criterion}

model = RandomForestClassifier()
modelrs = RandomizedSearchCV(estimator=model, param_distributions=param, cv=5)
modelrs.fit(xtr,ytr)

est = modelrs.best_params_['n_estimators']
crit = modelrs.best_params_['criterion']

modelbaru = RandomForestClassifier(n_estimators=est,criterion=crit)
modelbaru.fit(xtr,ytr)

joblib.dump(model,'modelprediksijoblib')