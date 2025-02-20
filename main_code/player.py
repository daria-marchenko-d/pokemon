import pygame
import json
import random
import sys

from pokedex import Pokedex

class Player:
    def __init__(self, name):
# Player initialization
        self.name = name
        # The pokemon list
        self.team = [] 
        # Pokedex for checkong pokemons
        self.pokedex = Pokedex()

    def add_pokemon(self, pokemon_name):
        # Add a pokemon to the team if it is in the Pokedex
        pokemon = self.pokedex.find_pokemon(pokemon_name)
        if pokemon:
            # The limit is 6 pokemons in the team
            if len(self.team) < 6:  
                self.team.append(pokemon)
                print(f"{pokemon_name} is added to your team!")
            else:
                print("Your team is complete. First remove the pokemon.")
        else:
            print(f"{pokemon_name} is not found in pokedex.")

    def switch_pokemon(self, index):
# Changes the active Pokémon (moves it to the first place in the team)
        if 0 <= index < len(self.team):
            self.team.insert(0, self.team.pop(index))
            print(f"Now {self.team[0]['name']} is your active pokemon!")
        else:
            print("Wrong Pokemon choice!")

    def show_team(self):
#  Displays the player's team
        if self.team:
            print(f"Команда {self.name}:")
            for i, pokemon in enumerate(self.team):
                print(f"{i+1}. {pokemon['name']} - {pokemon['type']} (Lv: {pokemon['level']})")
        else:
            print("You don't have any Pokémon yet.!")

# Testing The Player class
if __name__ == "__main__":
    player = Player("Ash")

    # Add pokemon to the team
    player.add_pokemon("Pikachu")
    player.add_pokemon("Charmander")

    # Show the team
    player.show_team()

    # Switch the active pokemon
    player.switch_pokemon(1)
    player.show_team()
    player.switch_pokemon(0)