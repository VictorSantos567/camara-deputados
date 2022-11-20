import requests

HOST = "https://dadosabertos.camara.leg.br"

def get_partidos():
    url = HOST+"/api/v2/partidos"
    response = requests.get(url).json()
    return response
