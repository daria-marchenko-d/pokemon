import pygame
import json
import random
import sys

class Sprite:
    def __init__(self, image_path): 
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def draw(self, screen, position):
        screen.blit(self.image, position)

    def get_rect(self):
        return self.image.get_rect()
    
    def get_width(self):
        return self.image.get_width()
    
    def get_height(self):
        return self.image.get_height()
    
    def get_size(self):
        return self.image.get_size()
    
    def get_center(self):
        return self.image.get_rect().center
    
    # def get centerx(self):
    #     return self.image.get_rect().centerx

    def get_centery(self):
        return self.image.get_rect().centery
    
    def get_top(self):
        return self.image.get_rect().top
    
    def get_bottom(self):
        return self.image.get_rect().bottom
    
    def get_left(self):
        return self.image.get_rect().left
    
    def get_right(self):
        return self.image.get_rect().right
    
    def get_topleft(self):
        return self.image.get_rect().topleft
    
    def get_topright(self):
        return self.image.get_rect().topright
    
    def get_bottomleft(self):
        return self.image.get_rect().bottomleft
    
    def get_bottomright(self):
        return self.image.get_rect().bottomright
    
    

    
    
