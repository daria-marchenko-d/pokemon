import pygame
import json
import random
import sys

class Pokemon:
    def __init__(self, name,level, hit_points, type_, attack, defense):
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

    def evolution(self):

        # Evolution of the pokemon
        self.level += 1
        self.attack_power += 2
        self.defense += 1
        self.life_point += 5
        print(f"{self.name} received the level {self.level}!")

    def attack(self, target):

    #    Attack the target
        damage = self.attack_power - target.defense
        target.life_point -= max(0, damage)  # Minimum damage is 0
        print(f"{self.name} attack {target.name} and caused {damage} damage!")

    def is_alive(self):
        return self.life_point > 0
    
    def __str__(self):
        return f"{self.name} is a {self.type_} type pokemon with {self.hit_points} hit points, {self.attack} attack and {self.defense} defense."
    
    def __repr__(self):
         return f"{self.name} is a {self.type_} type pokemon with {self.hit_points} hit points, {self.attack} attack and {self.defense} defense."
    

if __name__ == "__main__":
    pokemon = Pokemon("Pikachu", 1, 35, "Electric", 55, 40)
    print(pokemon)

    