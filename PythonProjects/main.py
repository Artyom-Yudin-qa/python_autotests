import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ec329e1253203fb454c703a034504606'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_creation = {
    "name": "Lastik",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_change_name = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": pokemon_id
}
response_name_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_name_change.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)