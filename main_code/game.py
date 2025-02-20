import pygame
import json
import random
import sys
import pygame
from menu import Menu 
from player import Player  
from combat import Combat
from graphic import Graphic  
from pokedex import Pokedex 

class Game:
    def __init__(self):
        pygame.init()

        # Initialize all necessary components
        self.graphic = Graphic(self)
        self.menu = Menu(self.graphic.screen, self, self.graphic) 

        player_name = self.menu.user_name()
        self.player = Player(player_name)

        self.combat = Combat(self)
        self.pokedex = Pokedex() 



        self.running = True
        self.pokemon_list = self.load_pokemon()
        self.selected_pokemon = None
        self.scroll_offset = 0  # Прокрутка списку
        self.selected_index = 0

    def run(self):
        while self.graphic.running:
            self.handle_events()
            self.update()
            self.draw()
            self.graphic.clock.tick(60)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            else:
                self.menu.handle_event(event)
                self.player.handle_event(event)
                self.combat.handle_event(event)
    
    def update(self):
        self.menu.update()
        self.player.update()
        self.combat.update()
        self.graphic.update()

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

    def choose_pokemon(self):
        """Меню вибору покемона зі скролінгом."""
        running = True

        while running:
            self.graphic.screen.fill((30, 30, 30))
            self.graphic.draw_text("Choose Your Pokemon", 40, self.graphic.center_x, 50)

            # Малюємо список покемонів
            start_y = 120
            for i, pokemon in enumerate(self.pokemon_list):
                img = pygame.image.load(pokemon["image"]).convert_alpha()
                img_rect = img.get_rect(center=(self.graphic.center_x, start_y + i * 100 + self.scroll_offset))
                
                if i == self.selected_index:
                    pygame.draw.rect(self.graphic.screen, (255, 255, 0), img_rect.inflate(10, 10), 3)

                self.graphic.screen.blit(img, img_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and self.selected_index < len(self.pokemon_list) - 1:
                        self.selected_index += 1
                        self.scroll_offset -= 100
                    if event.key == pygame.K_UP and self.selected_index > 0:
                        self.selected_index -= 1
                        self.scroll_offset += 100
                    if event.key == pygame.K_RETURN:
                        self.selected_pokemon = self.pokemon_list[self.selected_index]
                        running = False
                    if event.key == pygame.K_ESCAPE:
                        running = False
    


    def draw(self):
        self.menu.draw(self.graphic.screen)
        self.player.draw(self.graphic.screen)
        self.combat.draw(self.graphic.screen)
        self.graphic.draw(self.graphic.screen)
        pygame.display.flip()
        
    def quit(self):
        self.graphic.running = False
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()

        
