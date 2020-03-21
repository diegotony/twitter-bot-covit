import requests
import datetime
import json


URL = "http://covid-openknowledge.herokuapp.com/covidOpenKnowledge/api/v1/noticias"


def post_noticias(data):
    payload = {
        # "estadoCuarentena": "true",
        # "fecha": str(datetime.datetime.utcnow()),
        "fuente": str(data['fuente']),
        "resumen": str(data['resumen']),
        "titulo": str(data['titulo'])
    }
    data = json.dumps(payload)
    r = requests.post(URL, data=data, headers={
                      'Content-Type': 'application/json', "charset": "UTF-8"},)
    return r.json()
