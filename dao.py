import requests
from datetime import datetime

HOST = "https://dadosabertos.camara.leg.br"


def get_all_partys_current():
    today = str(datetime.now().date())
    url = HOST+"/api/v2/partidos?dataInicio="+today
    response = requests.get(url).json()
    return response
