import requests
from urllib.request import urlopen
from PIL import Image
from matplotlib import pyplot
#import matplotlib.pyplot as plt


def menu():
    print("Welcome to the Pokédex, the indispensable tool for every Pokémon Trainer on their journey through the vast and wondrous world of Pokémon! Developed by Professor Oak, the Pokédex is not just a digital encyclopedia but your faithful guide to discovering and cataloging every Pokémon species you encounter.\n\nAs you embark on your adventure, the Pokédex will be your trusted companion, providing detailed information about each Pokémon's habitat, abilities, evolutionary stages, and even tips on effective strategies for capturing them. It's more than just a database; it's a window into the rich diversity of Pokémon species that inhabit forests, caves, oceans, and even the skies above.\n\nWhether you're exploring the dense forests of Viridian City or navigating the treacherous waters of Cerulean Cape, the Pokédex is your key to understanding and connecting with the Pokémon you encounter. Each entry is a testament to the unique characteristics and behaviors of these extraordinary creatures, from the fiery Charizard to the mysterious Mewtwo.\n\nWith each new discovery and entry in your Pokédex, you'll deepen your knowledge of the Pokémon world and forge stronger bonds with your Pokémon partners. So, embark on your journey, capture your dreams, and let the Pokédex illuminate the path ahead as you strive to become a Pokémon Master!")

menu()


def imprimir_nombres():
    url = 'https://pokeapi.co/api/v2/pokemon'
    response = requests.get(url)
    if response.status_code == 200:
        nombres = response.json()
        for nombres in nombres['results']:
            print(nombres['name'])
    else:
        print(f"Error :  {response.status_code}")

imprimir_nombres()


def name_pokemon():
    id_name = input("Enter de the or id of your pokemon")
    url = f'https://pokeapi.co/api/v2/pokemon/{id_name}'
    response = requests.get(url)
    if response.status_code == 200:
        name = response.json()
        pokemon_name = name['species']['name']
        print(pokemon_name)
    else:
        print("no exsite ese pokemon")

name_pokemon()

def imprimir_abilidades():
    id_name = input("Enter the id or name of the pokemon you want to search:  ")
    url = f'https://pokeapi.co/api/v2/pokemon/{id_name}'
    response = requests.get(url)
    if response.status_code == 200:
        habilidades = response.json()
        print("these are its abilities\n")
        for index,habilities in enumerate(habilidades['abilities'], start=1):
            print(f'{index}.-',habilities['ability']['name'])
    else:
        print(f"Error : {response.status_code}")

imprimir_abilidades()



def imprimir_movimientos():
    id_name = input("Enter the id or name of the pokemon you want to search:  ")
    url = f'https://pokeapi.co/api/v2/pokemon/{id_name}'
    response = requests.get(url)
    if response.status_code == 200:
        moves = response.json()
        print("these are its abilities\n")
        for index,movimientos in enumerate(moves['moves'], start=1):
            print(f'{index}.', movimientos['move']['name'])
    else:
        print(f"Error : {response.status_code}\nNo se encuentra el pokemon {id}")

imprimir_movimientos()



def image_show():
    id_name = input("Enter the id or name of your pokemon! :  ")
    url = f"https://pokeapi.co/api/v2/pokemon/{id_name}"
    response = requests.get(url)
    if response.status_code == 200:
        image_pokemon = response.json()
        image_url = image_pokemon['sprites']['other']['showdown']['front_shiny']
        image = Image.open(urlopen(image_url))
        pyplot.imshow(image)
        pyplot.show()
    else:
        print(f"{"Error" : response.status_code}")

image_show()