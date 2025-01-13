import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '12609'
TOKEN = '9dcbc54c1b7ea9a4b7919379a9075dc1'
HEADER = {'Content_Type':'application/json', 'trainer_token': TOKEN}
BODY_POKEMONS = {
    "name": "generate",
    "photo_id": -1
}
BODY_RENAME = {
    "pokemon_id": "192634",
    "name": "ПятьСемьСемьПять",
    "photo_id": 2
}
BODY_CATCH = {
    "pokemon_id": "192634"
}

def test_new_pokemon():
    response_new_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_POKEMONS)
    
    a = response_new_pokemon.text
    assert True

def test_rename_pokemon():
    response_rename_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_RENAME)
    
    a = response_rename_pokemon.text

    assert True

def test_catch_pokemon():
    response_catch_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_CATCH)
    
    a = response_catch_pokemon.text

    assert True
