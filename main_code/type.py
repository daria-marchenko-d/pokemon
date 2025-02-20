import pygame
import json
import random
import sys

class Type:
    # All possible types
    TYPES = [
        "normal", "fire", "water", "electric", "grass", "ice",
        "fighting", "poison", "ground", "flying", "psychic",
        "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"
    ]

    # Type effectiveness
    EFFECTIVENESS = {
        ("fire", "grass"): 2.0, ("fire", "water"): 0.5, ("fire", "fire"): 0.5,
        ("water", "fire"): 2.0, ("water", "grass"): 0.5, ("water", "water"): 0.5,
        ("grass", "water"): 2.0, ("grass", "fire"): 0.5, ("grass", "grass"): 0.5,
        ("electric", "water"): 2.0, ("electric", "ground"): 0.0, ("electric", "electric"): 0.5,
        ("rock", "fire"): 2.0, ("rock", "flying"): 2.0, ("rock", "bug"): 2.0,
        ("psychic", "fighting"): 2.0, ("psychic", "poison"): 2.0, ("psychic", "psychic"): 0.5,
        ("dark", "psychic"): 2.0, ("dark", "ghost"): 2.0, ("dark", "dark"): 0.5,
        ("steel", "rock"): 2.0, ("steel", "ice"): 2.0, ("steel", "steel"): 0.5,
    }

    @staticmethod
    def get_effectiveness(attacker_type, defender_type):
        # Return the effectiveness of an attack
        return Type.EFFECTIVENESS.get((attacker_type, defender_type), 1.0)
