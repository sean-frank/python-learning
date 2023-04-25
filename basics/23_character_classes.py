import random, requests, json


#would like to instead prompt the user of 5 different choices that they can choose from.
input = input('Please enter the name of the Pokemon you would like to use.')

number = random.randint(1, 1015)
random_pokemon = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}").json()['name'])
user_pokemon = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{input}").json()['name'])


class Blank_Pokemon:
    name = "none"
    hp = 0
    attack = 0
    defense = 0

#user pokemon class, might look into how to simplify this using a function to run the all 3 stats.
user = Blank_Pokemon()
user.name = user_pokemon
user.hp = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_pokemon}").json()['stats'][0]['base_stat'])
user.attack = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_pokemon}").json()['stats'][1]['base_stat'])
user.defense = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_pokemon}").json()['stats'][2]['base_stat'])

#enermy pokemon class, same thing as above applies. 
enemy = Blank_Pokemon()
enemy.name = random_pokemon
enemy.hp = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}").json()['stats'][0]['base_stat'])
enemy.attack = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}").json()['stats'][1]['base_stat'])
enemy.defense = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}").json()['stats'][2]['base_stat'])

print(f"Your Pokemon info: {user.name}, {user.hp}, {user.attack}, {user.defense}")
print(f"Enemy Pokemon info: {enemy.name}, {enemy.hp}, {enemy.attack}, {enemy.defense}")



