import pickle
from fastapi import FastAPI
from sklearn import *

codigo= FastAPI()
@codigo.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass: int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
    X = [Sex, Age, Lifeboat, Pclass]
    result = titanic.predict(X)

@codigo.get('/model')
def get():
    return {"survived": "bool",
	        "status": "int",	
	        "message": "string",	
            }
