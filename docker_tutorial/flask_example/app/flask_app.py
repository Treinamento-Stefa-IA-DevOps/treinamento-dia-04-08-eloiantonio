 flask_example
    +- app
        +- __init__.py
        +- flask_app.py
        +- Dockerfile
    +- docker-compose.yml

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

