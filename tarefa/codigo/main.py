import pickle
import uvicorn
from fastapi import FastAPI
from sklearn import *

app= FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass: int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
    X = [Sex, Age, Lifeboat, Pclass]
    result = titanic.predict(X)

@app.get('/model')
def get(Sex:int, Age:float, Lifeboat:int, Pclass: int):
    y = titanic(Sex, Age, Lifeboat, Pclass)    
    return {"survived": y,
	        "status": "int",	
	        "message": "string",	
            }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)