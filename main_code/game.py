import pygame
import json
import random
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.graphic = Graphic(self)
        self.pokemon_list = self.load_pokemon()

    def load_pokemon(self):
        try:
            with open("data/pokemon.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []


    def add_pokemon_to_file(self, new_pokemon):
        if new_pokemon not in self.pokemon_list:
            self.pokemon_list.append(new_pokemon)
            with open("data/pokemon.json", "w") as file:
                json.dump(self.pokemon_list, file, indent=4)
game = Game()   