import requests
import datetime

URL="http://covid-openknowledge.herokuapp.com/covidOpenKnowledge/api/v1/noticias"

def post_noticias(data):
    payload={
        "estadoCuarentena": True,
        "fecha": datetime.datetime.utcnow(),
        "fuente": data['fuente'],
        "resumen": data['resumen'],
        "titulo": data['titulo']
    }
    r = requests.post(URL, data = payload)
    return r