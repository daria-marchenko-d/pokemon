import pygame
import json
import random
import sys

import random
from type import Type

class Combat:
    def __init__(self, player, opponent):
        """Ініціалізація бою між гравцем і опонентом"""
        self.player = player
        self.opponent = opponent
        self.type_ = Type()

    def calculate_damage(self, attacker, defender):
        """Розрахунок шкоди з урахуванням типу атаки"""
        base_damage = max(1, attacker['attack'] - defender['defense'])
        type_multiplier = self.type_affinity.get_multiplier(attacker['type'], defender['type'])
        return int(base_damage * type_multiplier)

    def fight(self):
        """Початок бою"""
        player_pokemon = self.player.team[0]
        opponent_pokemon = self.opponent.team[0]

        print(f"{self.player.name} випускає {player_pokemon['name']}!")
        print(f"{self.opponent.name} випускає {opponent_pokemon['name']}!")

        while player_pokemon['life_point'] > 0 and opponent_pokemon['life_point'] > 0:
            # Гравець атакує
            damage = self.calculate_damage(player_pokemon, opponent_pokemon)
            opponent_pokemon['life_point'] -= damage
            print(f"{player_pokemon['name']} атакує {opponent_pokemon['name']} та завдає {damage} шкоди!")

            if opponent_pokemon['life_point'] <= 0:
                print(f"{opponent_pokemon['name']} переможений!")
                self.award_xp(player_pokemon)
                return "player"

            # Опонент атакує
            damage = self.calculate_damage(opponent_pokemon, player_pokemon)
            player_pokemon['life_point'] -= damage
            print(f"{opponent_pokemon['name']} атакує {player_pokemon['name']} та завдає {damage} шкоди!")

            if player_pokemon['life_point'] <= 0:
                print(f"{player_pokemon['name']} переможений!")
                return "opponent"

    def award_xp(self, pokemon):
        """Нагорода досвідом після перемоги"""
        pokemon['level'] += 1
        pokemon['attack'] += 2
        pokemon['defense'] += 1
        pokemon['life_point'] += 5
        print(f"{pokemon['name']} підняв рівень до {pokemon['level']}!")

    def attempt_escape(self):
        """Спроба втечі з бою"""
        escape_chance = random.random()
        if escape_chance > 0.5:
            print("Втеча вдалася!")
            return True
        else:
            print("Втеча не вдалася!")
            return False

# Тестування
if __name__ == "__main__":
    from player import Player

    player = Player("Ash")
    opponent = Player("Gary")

    player.add_pokemon("Pikachu")
    opponent.add_pokemon("Charmander")

    battle = Combat(player, opponent)
    battle.fight()
