from flask import Flask
from flask import request
from flask import jsonify
import json
import os

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def wallet():
    if request.method == 'POST':
        data = request.json # a multidict containing POST data
        print(data)
        return str(data)
if __name__ == '__main__':
   app.run(host= '0.0.0.0', port=2000)
