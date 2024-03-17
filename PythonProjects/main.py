import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '1dfd82b8c2f6db1e5ce9fb9183a7f757'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body = {
    "name": "Бульбулятор",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}

body_rename = {
    "pokemon_id": "14252",
    "name": "Бульбугаврик",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}

body_pockeboll = {
    "pokemon_id": "14252"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print(response.text)


response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_rename)

print(response.text)


response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pockeboll)

print(response.text)