import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c8515e763c8eff53f5c4f7e737615da9'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1",
    "password_re": "Iloveqa1"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}
body_new = {
    "pokemon_id": "530585",
    "name": "New Name",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "530585"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirmation', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json)

response_new = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new)
print(response_new.json)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.json)


