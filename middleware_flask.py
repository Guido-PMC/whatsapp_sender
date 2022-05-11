from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

if "TEST" in os.environ['ENVIRONMENT']:
    credenciales = 'pilarminingco-c11e8da70b2f.json'
if "MACBOOK" in os.environ['ENVIRONMENT']:
    credenciales = '/home/PMC/AutomatismosPMC/pilarminingco-c11e8da70b2f.json'
if "PORTAINER" in os.environ['ENVIRONMENT']:
    credenciales = '/creds/pilarminingco-c11e8da70b2f.json'

def append_row(sheet,worksheet,new_row):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credenciales, scope)
    client = gspread.authorize(creds)
    work_sheet = client.open(sheet)
    sheet_instance = work_sheet.worksheet(worksheet)
    sheet_instance.append_row(new_row, value_input_option="USER_ENTERED")
    return True
app = Flask(__name__)
@app.route('/test', methods = ['GET','POST'])
def test():
    if request.method == 'POST':
        data = request.json # a multidict containing POST data
        print(data)
        row = list(filter(lambda i:i!="", data.values()))
        append_row("Contactos WEB - PMC", "Hoja 1", row)
        data = {'name': 'Guido'}
        return jsonify(data)
if __name__ == '__main__':
   app.run(host= '0.0.0.0', port=5001)
