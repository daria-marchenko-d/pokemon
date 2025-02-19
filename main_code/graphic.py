import pygame
import json
import random
import sys

class Graphic:
    def __init__(self, game, width=1280, height=720):
        self.game = game
        self.WIDTH = width 
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pokémon Game")

        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 200, 50)
        self.clock = pygame.time.Clock()

        self.FPS = 30
        
        self.screen.fill(self.WHITE) 

        self.font = pygame.font.Font("Harrington", 50)
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

class Map:
    pass