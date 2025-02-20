# import pygame
# import json
# import random
# import sys

# class Sprite:
#     def __init__(self, image_path): 
#         self.image = pygame.image.load(image_path)
#         self.image = pygame.transform.scale(self.image, (50, 50))

#     def draw(self, screen, position):
#         screen.blit(self.image, position)

#     def get_rect(self):
#         return self.image.get_rect()
    
#     def get_width(self):
#         return self.image.get_width()
    
#     def get_height(self):
#         return self.image.get_height()
    
#     def get_size(self):
#         return self.image.get_size()
    
#     def get_center(self):
#         return self.image.get_rect().center
    
#     # def get centerx(self):
#     #     return self.image.get_rect().centerx

#     def get_centery(self):
#         return self.image.get_rect().centery
    
#     def get_top(self):
#         return self.image.get_rect().top
    
#     def get_bottom(self):
#         return self.image.get_rect().bottom
    
#     def get_left(self):
#         return self.image.get_rect().left
    
#     def get_right(self):
#         return self.image.get_rect().right
    
#     def get_topleft(self):
#         return self.image.get_rect().topleft
    
#     def get_topright(self):
#         return self.image.get_rect().topright
    
#     def get_bottomleft(self):
#         return self.image.get_rect().bottomleft
    
#     def get_bottomright(self):
#         return self.image.get_rect().bottomright
    
    
import pygame
from graphic import Graphic

class Sprite:
    def __init__(self, image, position):
# Sprite initialization

        # Pokemons sprites
        self.image = image
        # First position
        self.position = position 
        # Rectangular area of the sprite
        self.rect = self.image.get_rect(topleft = position)  

    def draw(self, screen):
        # Show the sprite on the screen
        screen.blit(self.image, self.rect.topleft)

    def move(self, new_position):
        # Move the sprite to the new position
        self.rect.topleft = new_position

    def animate_movement(self, screen, new_position, speed=5):
        # Animate the movement of the sprite to the new position
        x1, y1 = self.rect.topleft
        x2, y2 = new_position

        while (x1, y1) != (x2, y2):
            if x1 < x2:
                x1 += min(speed, x2 - x1)
            elif x1 > x2:
                x1 -= min(speed, x1 - x2)

            if y1 < y2:
                y1 += min(speed, y2 - y1)
            elif y1 > y2:
                y1 -= min(speed, y1 - y2)

            self.rect.topleft = (x1, y1)
            self.screen.blit(self.background, (0, 0))

            self.draw(screen)
            pygame.display.update()
            # Launching the event 
            pygame.time.delay(30) 

    
    
