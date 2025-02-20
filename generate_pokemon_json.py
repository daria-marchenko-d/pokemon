import requests
import json

# URL de base de l'API PokéAPI
base_url = "https://pokeapi.co/api/v2/pokemon/"

# Liste pour stocker les données des Pokémon
pokemon_data = []

# Fonction pour récupérer les données d'un Pokémon par son ID
def get_pokemon_data(pokemon_id):
    response = requests.get(f"{base_url}{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "nom": data["name"].capitalize(),
            "type": [t["type"]["name"].capitalize() for t in data["types"]],
            "pv": data["stats"][0]["base_stat"],
            "attaque": data["stats"][1]["base_stat"],
            "defense": data["stats"][2]["base_stat"],
            "vitesse": data["stats"][5]["base_stat"],
            "special": data["stats"][3]["base_stat"],  # Dans la 1ère génération, c'était "special"
            "sprites": {
                "face": data["sprites"]["front_default"],
                "dos": data["sprites"]["back_default"]
            },
            "attaques": [move["move"]["name"] for move in data["moves"][:4]]  # Limité aux 4 premières attaques
        }
    else:
        print(f"Erreur lors de la récupération des données pour le Pokémon ID {pokemon_id}")
        return None

# Boucle pour récupérer les données des 151 premiers Pokémon
for i in range(1, 152):
    pokemon = get_pokemon_data(i)
    if pokemon:
        pokemon_data.append(pokemon)

# Écriture des données dans un fichier JSON
with open("pokemon.json", "w", encoding="utf-8") as f:
    json.dump(pokemon_data, f, indent=4, ensure_ascii=False)

print("Fichier 'pokemon.json' généré avec succès.")
