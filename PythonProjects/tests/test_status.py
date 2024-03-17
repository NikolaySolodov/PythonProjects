import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '1dfd82b8c2f6db1e5ce9fb9183a7f757'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {"trainer_id": 1970})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params= {"trainer_id": 1970})
    assert response.json()['data'][0]["trainer_name"]== "Николай"