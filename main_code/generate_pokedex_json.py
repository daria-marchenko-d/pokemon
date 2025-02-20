import os
import json

def generate_pokemon_json(image_directory, output_json_file):
    # List all PNG files in the directory
    files = os.listdir(image_directory)
    png_files = [file for file in files if file.endswith('.png')]
    
    # Create a dictionary for Pokémon data
    pokemon_data = {
        "en": {
            "title": "Pokemon Battle",
            "pokemon": {
                "available": {
                    "bulbasaur": {
                        "name": "Bulbasaur",
                        "level": 5,
                        "hit_points": 50,
                        "type_": "unknown",
                        "attack": 50,
                        "defense": 50
                    },
                    "charmander": {
                        "name": "Charmander",
                        "level": 5,
                        "hit_points": 50,
                        "type_": "unknown",
                        "attack": 50,
                        "defense": 50
                    }
                },
                "unavailable": {
                    "squirtle": {
                        "name": "Squirtle",
                        "level": 5,
                        "hit_points": 50,
                        "type_": "unknown",
                        "attack": 50,
                        "defense": 50
                    },
                    "pikachu": {
                        "name": "Pikachu",
                        "level": 5,
                        "hit_points": 50,
                        "type_": "unknown",
                        "attack": 50,
                        "defense": 50
                    }
                }
            }
        }
    }
    
    # Populate the available and unavailable sections
    for i, file in enumerate(png_files):
        pokemon_key = os.path.splitext(file)[0]
        pokemon_entry = {
            "name": pokemon_key.capitalize(),
            "level": 5,
            "hit_points": 50,
            "type_": "unknown",
            "attack": 50,
            "defense": 50
        }
        
        if i % 2 == 0:
            pokemon_data["en"]["pokemon"]["available"][pokemon_key] = pokemon_entry
        else:
            pokemon_data["en"]["pokemon"]["unavailable"][pokemon_key] = pokemon_entry
    
    # Write the JSON data to the output file
    with open(output_json_file, "w") as f:
        json.dump(pokemon_data, f, indent=4)

if __name__ == "__main__":
    image_directory = "/Users/mameaminataconstancesane/Desktop/pokemon/main_code/pictures"
    output_json_file = "/Users/mameaminataconstancesane/Desktop/pokemon/main_code/data/generated_pokemon.json"
    
    generate_pokemon_json(image_directory, output_json_file)