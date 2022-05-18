from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os
from datetime import datetime


class formulario:
    def __init__(self, servicio, rig_tipo_presupuesto, rig_tipo_dinero, rig_tipo_rentabilidad, rig_tipo_megahash, housing_placas, housing_rigs, exchange_operacion, exchange_monto, nombre, email, tel, mensaje):
        self.servicio = servicio
        self.rig_tipo_presupuesto = rig_tipo_presupuesto
        self.rig_tipo_dinero = rig_tipo_dinero
        self.rig_tipo_rentabilidad = rig_tipo_rentabilidad
        self.rig_tipo_megahash = rig_tipo_megahash
        self.housing_placas = housing_placas
        self.housing_rigs = housing_rigs
        self.exchange_operacion = exchange_operacion
        self.exchange_monto = exchange_monto
        self.nombre = nombre
        self.email = email
        self.tel = tel
        self.mensaje = mensaje


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

def whatsappize_number(number):
    if (number.startswith("549")): #NUMERO COMPLETO PARA WASAP
        return number
    elif number.startswith("54"):#NUMERO COMPLETO OTRA PROVINCIA
        return number
    elif number.startswith("11"): #NUMERO BASICO BS AS
        return ("549"+number)
    else: #NUMEROS BASICOS OTRAS PROVINCIAS
        return ("549"+number)



app = Flask(__name__)
@app.route('/test', methods = ['GET','POST'])
def test():
    if request.method == 'POST':
        data = request.json # a multidict containing POST data
        print("Imprimo la data \n\n")
        print(datetime.today().strftime('%d-%m %H:%M'))
        print(data)
        string_wsap = "https://web.whatsapp.com/send?phone=XXXXXXXXX&text=Hola%20como%20estas?%20Me%20comunico%20de%20Pilar%20Mining%20CO"
        string_wsap = string_wsap.replace('XXXXXXXXX', whatsappize_number(data["tel"]))
        new_json = {"fecha": datetime.today().strftime('%d-%m %H:%M'),"nombre": data["nombre"],"mail":data["email"], "celular":string_wsap, "servicio":data["servicio"],"detalle":data["rig-tipo-presupuesto"]+" "+data["rig-tipo-dinero"]+" "+data["rig-tipo-rentabilidad"]+" "+data["rig-tipo-megahash"]+" "+data["housing-placas"]+" "+data["housing-rigs"]+" "+data["exchange-operacion"]+" "+data["exchange-monto"]+" "+data["mensaje"] }
        row = list(new_json.values())
        append_row("Contactos WEB - PMC", "test", row)
        data = {'name': 'Guido'}
        return jsonify(data)
if __name__ == '__main__':
   app.run(host= '0.0.0.0', port=5001)
