import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '12609'
TOKEN = 'TRAINER_TOKEN'
HEADER = {'Content_Type':'application/json', 'trainer_token': TOKEN}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == "Slonopitek"


   
