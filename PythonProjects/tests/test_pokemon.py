import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ec329e1253203fb454c703a034504606'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4999'

def test_status_code():
    response_get_trainers = requests.get(url = f'{URL}/trainers')
    assert response_get_trainers.status_code == 200

def test_trainer_name():
    response_trainer_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_trainer_name.json()["data"][0]["trainer_name"] == 'ishenmue87'

@pytest.mark.parametrize('key, value', [('trainer_name', 'ishenmue87'), ('id', TRAINER_ID)])
def test_parametrize(key, value):
    response_trainer_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_trainer_name.json()["data"][0][key] == value


