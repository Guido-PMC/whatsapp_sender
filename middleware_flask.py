from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import json
import os

app = Flask(__name__)
@app.route('/test', methods = ['GET','POST'])
def test():
    if request.method == 'POST':
        data = request.json # a multidict containing POST data
        print(data)
        data = {'name': 'Guido'}
        return jsonify(data)
if __name__ == '__main__':
   app.run(host= '0.0.0.0', port=5001)
