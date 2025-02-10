import pygame
import json
import random

class Sprite:
    pass

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

    def main_menu(self):
        pass


    def add_pokemon_to_file(self, new_pokemon):
        if new_pokemon not in self.pokemon_list:
            self.pokemon_list.append(new_pokemon)
            with open("data/pokemon.json", "w") as file:
                json.dump(self.pokemon_list, file, indent=4)


class Pokemon:
    def __init__(self, name, level, hit_points, type_, attack, defense):
        self.name = name
        self.level = level
        self.hit_points = hit_points
        self.type = type_
        self.attack = attack
        self.defense = defense
    def damage(self, damage):
        damage_taken = max(0, damage - self.defense)
        self.hit_points -=damage_taken
        if self.hit_points < 0:
            self.hit_points = 0
        print (f"{self.name} has {self.hit_points} remaining")

class Graphic:
    pass


class Type:
    pass


class Dresseur:
    pass

class Combat:
    pass

class Poke_index:
    pass
