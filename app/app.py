from flask import Flask
from time import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'time': time()}
