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
        self.clock = pygame.time.Clock()

        # Colors
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 200, 50)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.HIGHLIGHT = (100, 149, 237)
        self.BLUE = (0,0,255)

        self.FPS = 30
        self.background = pygame.image.load("main_code/pictures/menu-background.jpg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.music = pygame.mixer.music.load("main_code/sounds/menu.mp3")
        pygame.mixer.music.play(-1)

        self.font = pygame.font.SysFont("Harrington", 50)
        self.small_font = pygame.font.SysFont("Harrington", 30)

        self.running = True


    def draw_button(self, y, text, default_color, hover_color, action=None):
        self.y = y
        self.text = text 
        self.default_color = default_color
        self.hover_color = hover_color
        self.action = action

        text_surface = self.font.render(self.text, True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, self.y + 25))
        width = text_rect.width + 40  
        height = 50
        x = (self.WIDTH - width) // 2

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + width and self.y < mouse[1] < self.y + height:
            pygame.draw.rect(self.screen, self.hover_color, (x, self.y, width, height))
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            pygame.draw.rect(self.screen, self.default_color, (x, self.y, width, height))

        self.screen.blit(text_surface, text_rect)


    def show_main_menu(self):
        self.running = True
        while self.running:
            self.screen.blit(self.background, (0, 0))

            self.draw_button(170, "Your name", self.GRAY, self.HIGHLIGHT, self.user_name)
            self.draw_button(230, "Start game", self.GRAY, self.HIGHLIGHT, self.menu_game)
            self.draw_button(290, "Choose pokemon", self.GRAY, self.HIGHLIGHT, self.pokemon_menu)
            self.draw_button(350, "Rules", self.GRAY, self.HIGHLIGHT, self.rules)
            self.draw_button(410, "Statistic", self.GRAY, self.HIGHLIGHT, self.statistic)
            self.draw_button(470, "Languages", self.GRAY, self.HIGHLIGHT, self.languages_menu)
            self.draw_button(530, "Exit", self.GRAY, self.HIGHLIGHT, self.quit_game)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def menu_game(self):
        pass

    def user_name(self):
    # Ask for the user's name via a Pygame graphical interface."""
        self.input_box = pygame.Rect(self.WIDTH // 2 - 100, self.HEIGHT // 2 - 20, 200, 60)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        color = self.color_inactive
        active = False
        text = ''
        done = False
        prompt_text = self.font.render("Please enter your name:", True, self.BLUE)
        message = ""

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = self.color_active if active else self.color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            message = f"Hello, {text}. Time to choose your pokemon!"
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.blit(self.background, (0, 0))
            


            self.screen.blit(prompt_text, (self.WIDTH // 2 - prompt_text.get_width() // 2, self.HEIGHT // 2 - 80))
            txt_surface = self.font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            self.input_box.w = width
            self.input_box.x = self.WIDTH // 2 - self.input_box.w // 2
            self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            pygame.draw.rect(self.screen, color, self.input_box, 2)

            if message:
                message_surface = self.small_font.render(message, True, self.BLUE)
                self.screen.blit(message_surface, (self.WIDTH // 2 - message_surface.get_width() // 2, self.HEIGHT // 2 + 50))

            pygame.display.flip()

        # Wait for the user to press a key to continue
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

        return text

    def pokemon_menu(self):
        pass
    
    def rules(self):
        pass

    def statistic(self):
        pass

    def languages_menu(self):
        pass

    def quit_game(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    
    if not pygame.get_init():
        print("❌")
    
    game = None  
    graphic = Graphic(game)
    graphic.show_main_menu()