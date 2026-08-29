import requests

base_url = "http://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to get pokemon data {response.status_code}")


pokemon_name = "ditto"

pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:
    print(f"{pokemon_info['name']}")
    print(f"{pokemon_info['id']}")
