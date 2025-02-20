import pygame
import sys
from graphic import Graphic 

class Menu:
    def __init__(self, game_screen, game, graphic):
      self.screen = game_screen
      self.game = game
      self.graphic = graphic
      self.WIDTH, self.HEIGHT = game_screen.get_size()
      
    def show_main_menu(self):
        print("Returning to main menu")
        self.running = True

        while self.running:
            self.graphic.draw_menu_background() 

            self.graphic.draw_button(240, "Start game", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.menu_game)
            self.graphic.draw_button(310, "Add pokemon", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.pokemon_menu)
            self.graphic.draw_button(380, "Pokedex", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_pokedex)
            self.graphic.draw_button(450, "Rules and Settings", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.rules_settings)
            self.graphic.draw_button(520, "Exit", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.quit_game)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def menu_game(self):
        print("menu_game called")  # Додали цей рядок для перевірки
        # Clothe current window
        # self.running = False
        # Open new window with new menu
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 

            self.graphic.draw_button(240, "New part", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.new_part)
            self.graphic.draw_button(310, "Current part", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.current_part)
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.return_to_main_menu)

            pygame.display.flip()
            # pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
        print("Exiting menu_game") 

    def new_part(self):
        # Clothe current window
        self.running = False
        # Open new window with new menu
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 

            self.graphic.draw_button(170, "Your name", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.user_name)
            self.graphic.draw_button(240, "Start", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.start)
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.return_to_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def current_part(self):
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 
            
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    
    def start(self):
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 
            
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def user_name(self):
    # Ask for the user's name via a Pygame graphical interface."""
        self.input_box = pygame.Rect(self.graphic.WIDTH // 2 - 100, self.graphic.HEIGHT // 2 - 20, 200, 60)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        color = self.color_inactive
        active = False
        text = ''
        done = False
        prompt_text = self.graphic.font.render("Please enter your name:", True, self.graphic.BLUE)
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

            self.graphic.draw_menu_background() 
            


            self.screen.blit(prompt_text, (self.graphic.WIDTH // 2 - prompt_text.get_width() // 2, self.graphic.HEIGHT // 2 - 80))
            txt_surface = self.graphic.font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            self.input_box.w = width
            self.input_box.x = self.WIDTH // 2 - self.input_box.w // 2
            self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            pygame.draw.rect(self.screen, color, self.input_box, 2)

            if message:
                message_surface = self.graphic.small_font.render(message, True, self.graphic.BLUE)
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
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 
            
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def show_pokedex(self):
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 
            
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def rules_settings(self):
        # Clothe current window
        self.running = False
        # Open new window with new menu
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 

            self.graphic.draw_button(170, "Rules", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.rules)
            self.graphic.draw_button(240, "Language", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.languages_menu)
            self.graphic.draw_button(310, "Help", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.help)
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def rules(self):
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 
            
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
        

    def languages_menu(self):
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 

            self.graphic.draw_button(170, "French", self.graphic.GRAY, self.graphic.HIGHLIGHT)
            self.graphic.draw_button(240, "English", self.graphic.GRAY, self.graphic.HIGHLIGHT)
            self.graphic.draw_button(310, "Ukrainian", self.graphic.GRAY, self.graphic.HIGHLIGHT)
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def help(self):
        self.running = True
        while self.running:
            self.graphic.draw_menu_background() 
            
            self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT, self.show_main_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def return_to_main_menu(self):
        print("Returning to main menu")  # Логування для перевірки
        self.running = False 

    def quit_game(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    game = None  # Якщо потрібно, заміни на клас гри
    graphic = Graphic(game)

    menu = Menu(screen, game, graphic)  # Передаємо `graphic`
    menu.show_main_menu()