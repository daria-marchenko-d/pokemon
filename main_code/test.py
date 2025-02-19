# import pygame
# import json
# import random

# # Клас для представлення Покемона
# class Pokemon:
#     def __init__(self, name, ptype, hp, attack, defense):
#         self.name = name
#         self.ptype = ptype
#         self.hp = hp
#         self.attack = attack
#         self.defense = defense

#     def take_damage(self, damage):
#         self.hp -= max(0, damage - self.defense)
#         return self.hp > 0

# # Клас для типів покемонів та ефективності атак
# class Type:
#     effectiveness = {
#         "Feu": {"Eau": 0.5, "Plante": 2.0, "Feu": 1.0},
#         "Eau": {"Feu": 2.0, "Plante": 0.5, "Eau": 1.0},
#         "Plante": {"Eau": 2.0, "Feu": 0.5, "Plante": 1.0}
#     }

#     @staticmethod
#     def get_effectiveness(attacker_type, defender_type):
#         return Type.effectiveness.get(attacker_type, {}).get(defender_type, 1.0)

# # Клас для бою між покемонами
# class Combat:
#     def __init__(self, pokemon1, pokemon2):
#         self.pokemon1 = pokemon1
#         self.pokemon2 = pokemon2

#     def attack(self, attacker, defender):
#         effectiveness = Type.get_effectiveness(attacker.ptype, defender.ptype)
#         damage = attacker.attack * effectiveness
#         alive = defender.take_damage(damage)
#         return alive

#     def start_battle(self):
#         while self.pokemon1.hp > 0 and self.pokemon2.hp > 0:
#             if not self.attack(self.pokemon1, self.pokemon2):
#                 return f"{self.pokemon1.name} wins!"
#             if not self.attack(self.pokemon2, self.pokemon1):
#                 return f"{self.pokemon2.name} wins!"

# # Клас для збереження покемонів у Pokédex
# class PokeIndex:
#     def __init__(self):
#         self.filename = "pokedex.json"
#         self.pokedex = self.load_pokedex()

#     def load_pokedex(self):
#         try:
#             with open(self.filename, "r") as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             return {}

#     def save_pokemon(self, pokemon):
#         if pokemon.name not in self.pokedex:
#             self.pokedex[pokemon.name] = {
#                 "type": pokemon.ptype,
#                 "hp": pokemon.hp,
#                 "attack": pokemon.attack,
#                 "defense": pokemon.defense
#             }
#             with open(self.filename, "w") as file:
#                 json.dump(self.pokedex, file, indent=4)

# # Клас для дресирувальника
# class Dresseur:
#     def __init__(self, name):
#         self.name = name
#         self.pokemons = []

#     def add_pokemon(self, pokemon):
#         if len(self.pokemons) < 6:
#             self.pokemons.append(pokemon)

# # Головний клас гри
# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((800, 600))
#         pygame.display.set_caption("Pokemon Battle")
#         self.running = True
#         self.pokedex = PokeIndex()
#         self.dresseur = Dresseur("Player")
#         self.load_pokemon_data()
#         self.menu()

#     def load_pokemon_data(self):
#         try:
#             with open("pokemon.json", "r") as file:
#                 self.pokemon_data = json.load(file)
#         except FileNotFoundError:
#             self.pokemon_data = []

#     def menu(self):
#         while True:
#             print("1. Lancer une partie")
#             print("2. Ajouter un Pokémon")
#             print("3. Accéder au Pokédex")
#             print("4. Quitter")
#             choix = input("Choisissez une option: ")
            
#             if choix == "1":
#                 self.start_game()
#             elif choix == "2":
#                 self.add_pokemon()
#             elif choix == "3":
#                 self.view_pokedex()
#             elif choix == "4":
#                 break
#             else:
#                 print("Option invalide.")

#     def start_game(self):
#         print("Démarrage du jeu...")
#         self.game_loop()

#     def add_pokemon(self):
#         name = input("Nom du Pokémon: ")
#         ptype = input("Type du Pokémon: ")
#         hp = int(input("HP: "))
#         attack = int(input("Attaque: "))
#         defense = int(input("Défense: "))
#         new_pokemon = Pokemon(name, ptype, hp, attack, defense)
#         self.pokedex.save_pokemon(new_pokemon)
#         print(f"{name} a été ajouté au Pokédex!")

#     def view_pokedex(self):
#         print("Pokédex:")
#         for name, data in self.pokedex.pokedex.items():
#             print(f"{name}: {data}")

#     def game_loop(self):
#         while self.running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
#             self.screen.fill((0, 0, 0))  # Чорний фон
#             pygame.display.flip()
#         pygame.quit()

# if __name__ == "__main__":
#     game = Game()

import sys
import pygame as pg


pg.init()

class Window:

    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        self.rect = self.screen.get_rect()
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 25)
        self.menu_open = True
        self.colors = {"red": (255, 0, 0),
                       "green": (0, 255, 0),
                       "blue": (0, 0, 255),
                       "white": (255, 255, 255),
                       "black": (0, 0, 0),
                       "brown": (153, 76, 0),
                       "grey": (100, 100, 100)}

    def setup(self):
        self.screen.fill(self.colors["black"])
        pg.display.set_caption("Menu Test!")

    def text(self, message, text_color, x_pos, y_pos):
        text = self.font.render(message, True, (self.colors[text_color]))
        text_rect = text.get_rect(center=(x_pos, y_pos))
        self.screen.blit(text, text_rect)

    def exit(self):
        self.screen.fill(self.colors["black"])
        text = self.font.render("Thank you for playing. Goodbye!", True,
                                (self.colors["white"]))
        text_rect = text.get_rect(center=(self.rect.w/2, self.rect.h/2))
        self.screen.blit(text, text_rect)
        pg.display.update()
        pg.time.wait(1000)
        pg.quit()
        sys.exit()


class Button(pg.sprite.Sprite):

    def __init__(self, pos, text, window):
        super().__init__()  # Call __init__ of the parent class.
        # Render the text.
        self.text_surf = window.font.render(text, True, window.colors["black"])
        self.image = pg.Surface((self.text_surf.get_width()+40,
                                 self.text_surf.get_height()+20))
        self.image.fill(window.colors["white"])
        # Now blit the text onto the self.image.
        self.image.blit(self.text_surf, (20, 10))
        self.rect = self.image.get_rect(topleft=pos)


def main():
    window = Window()
    window.setup()
    clock = pg.time.Clock()
    # gui is a sprite group which will contain the button sprites.
    gui = pg.sprite.Group()
    # Instantiate some buttons.
    quit_button = Button(
        pos=(window.rect.w/2 - 100, window.rect.h/1.5 - 25),
        text="QUIT",
        window=window,
        )
    hello_button = Button(
        pos=(window.rect.w/8, window.rect.h/2),
        text="hello",
        window=window,
        )
    # Add the buttons to the gui group.
    gui.add(quit_button, hello_button)

    while window.menu_open == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                window.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # Handle button events.
                if quit_button.rect.collidepoint(event.pos):
                    window.exit()
                elif hello_button.rect.collidepoint(event.pos):
                    print("hello")

        gui.update()  # Call update methods of contained sprites.
        gui.draw(window.screen)  # Draw all sprites.
        pg.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
