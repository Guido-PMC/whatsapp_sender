from flask import Flask
from flask import request
from flask import jsonify
import json
import os

app = Flask(__name__)
zabbix_address = "1.1.1.1"
print("Zabbix Adress: "+zabbix_address)
cantidad_envios={}
diccionario={}
salida={}
@app.route('/', methods = ['POST'])
def wallet():
    if request.method == 'POST':
        data = request.json # a multidict containing POST data
        return (1)
if __name__ == '__main__':
   app.run(host= '0.0.0.0', port=5001)
