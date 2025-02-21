import pygame
import json
import random
import sys

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
    def __init__(self, game):
        self.game = game
        self.width, self.height = 1280, 720  # Розмір вікна
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pokémon Game")

        self.font = pygame.font.Font(None, 36)
        self.running = True

    def show_main_menu(self):
        # main_menu of the game
        while self.running:
            self.screen.fill((50, 150, 200)) 

            title_text = self.font.render("Pokémon Game", True, (255, 255, 255))
            self.screen.blit(title_text, (self.width // 2 - 100, 50))

            # Buttom "Start Game"
            start_button = pygame.Rect(self.width // 2 - 100, 200, 200, 50)
            pygame.draw.rect(self.screen, (0, 255, 0), start_button)
            start_text = self.font.render("Start Game", True, (0, 0, 0))
            self.screen.blit(start_text, (self.width // 2 - 60, 215))

            # Buttom "Exit"
            exit_button = pygame.Rect(self.width // 2 - 100, 300, 200, 50)
            pygame.draw.rect(self.screen, (255, 0, 0), exit_button)
            exit_text = self.font.render("Exit", True, (0, 0, 0))
            self.screen.blit(exit_text, (self.width // 2 - 40, 315))

            pygame.display.flip()

            # Cicle for event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        self.game.start_game()  # Start game
                    elif exit_button.collidepoint(event.pos):
                        self.running = False
                        pygame.quit()
                        sys.exit()


class Type:
    pass


class Dresseur:
    pass

class Combat:
    pass

class Poke_index:
    pass
