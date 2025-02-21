import pygame
import sys
from graphic import Graphic 
import json
import os

class Menu:
    def __init__(self, game_screen, game, graphic):
        self.screen = game_screen
        self.game = game
        self.graphic = graphic
        self.WIDTH, self.HEIGHT = game_screen.get_size()
        self.running = True
        self.menu_state = "main"  # Save the current menu state
        self.menu_stack = ["main"]  # Add a stack to save the menu states

        # Languages
        self.languages = self.load_languages()
        self.current_language = "english"  # Current
        self.texts = self.languages[self.current_language]["menu"]
        self.graphic.texts = self.texts  # Send the texts to the graphic
        self.graphic.current_language = self.current_language  # Send the current language to the graphic

    def push_menu(self, new_state):
        self.menu_stack.append(self.menu_state)
        self.menu_state = new_state

    def pop_menu(self):
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()
            self.menu_state = self.menu_stack[-1]
            print(f"Returning to {self.menu_state}") # Return to the previous state
        else:
            print("Cannot go back further!")

    def load_languages(self):
        # Load the languages from the file
        with open("main_code/data/pokemon.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def change_language(self, lang_code):
        if lang_code in self.languages:
            self.current_language = lang_code
            self.texts = self.languages[lang_code]["menu"]
            self.graphic.current_language = lang_code
            self.graphic.texts = self.texts  
            print(f"The language was changed {lang_code}")

    def show_main_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.graphic.draw_menu_background()

            # Unified button for all menus
            if self.menu_state != "main":
                if self.graphic.draw_button(520, "go_back", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = self.menu_stack.pop()  # Return to the previous state
                    pygame.event.clear()  # Clear the event queue
                    continue  # Continue to the next iteration

            # Main menu buttons
            if self.menu_state == "main":
                if self.graphic.draw_button(240, "start_game", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("game")
                if self.graphic.draw_button(310, "add_pokemon", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("pokemon")
                if self.graphic.draw_button(380, "Pokedex", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("pokedex")
                if self.graphic.draw_button(450, "Rules and Settings", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("rules_settings")
                if self.graphic.draw_button(520, "Exit", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.quit_game()

            # The buttons of the game menu
            elif self.menu_state == "game":
                if self.graphic.draw_button(200, "New part", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("new_part")
                if self.graphic.draw_button(300, "Current part", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("current_part")

            # New part menu
            elif self.menu_state == "new_part":
                if self.graphic.draw_button(170, "Your name", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.user_name()
                if self.graphic.draw_button(240, "Start", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "start"

            # Current part menu
            elif self.menu_state == "current_part":
                pass

            # Menu Add pokemon
            elif self.menu_state == "pokemon":
                if self.graphic.draw_button(200, "Create Pokemon", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    pass  # Add functionality to create a pokemon
                if self.graphic.draw_button(300, "Import Pokemon", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    pass  # Add functionality to import a pokemon
                if self.graphic.draw_button(520, "go_back", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "main"
                    continue

            # Menu Pokedex
            elif self.menu_state == "pokedex":
                # Change the state to the main menu
                if self.graphic.draw_button(200, "View All Pokemon", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    pass  # add functionality to view all pokemon
                if self.graphic.draw_button(300, "Search Pokemon", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    pass  # add functionality to search pokemon
                if self.graphic.draw_button(520, "go_back", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "main"
                    continue

            # Settings and rules menu
            elif self.menu_state == "rules_settings":
                if self.graphic.draw_button(170, "Rules", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("rules")
                if self.graphic.draw_button(240, "Language", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("languages")
                if self.graphic.draw_button(310, "Help", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.push_menu("help")

            # Rules menu
            elif self.menu_state == "rules":
                pass

            # Language menu
            elif self.menu_state == "languages":
                if self.graphic.draw_button(170, "French", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.change_language("french")
                if self.graphic.draw_button(240, "English", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.change_language("english")
                if self.graphic.draw_button(310, "Ukrainian", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.change_language("ukrainian")

            # Help menu
            elif self.menu_state == "help":
                pass

            pygame.display.flip()
            pygame.time.Clock().tick(60)

    def user_name(self):
        self.input_box = pygame.Rect(self.graphic.WIDTH // 2 - 100, self.graphic.HEIGHT // 2 - 20, 200, 60)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        color = self.color_inactive
        active = False
        text = ''
        done = False
        
        # Use the font based on the current language
        if self.current_language == "ukrainian":
            font_to_use = self.graphic.ua_font
            small_font_to_use = self.graphic.ua_small_font
        else:
            font_to_use = self.graphic.default_font
            small_font_to_use = self.graphic.default_small_font

        prompt_text = font_to_use.render(self.texts.get("enter_name", "Please enter your name:"), True, self.graphic.BLUE)
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
            txt_surface = font_to_use.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            self.input_box.w = width
            self.input_box.x = self.WIDTH // 2 - self.input_box.w // 2
            self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            pygame.draw.rect(self.screen, color, self.input_box, 2)

            if message:
                message_surface = small_font_to_use.render(message, True, self.graphic.BLUE)
                self.screen.blit(message_surface, (self.WIDTH // 2 - message_surface.get_width() // 2, self.HEIGHT // 2 + 50))

            pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

        return text

    def push_menu(self, new_state):
        self.menu_stack.append(self.menu_state)
        self.menu_state = new_state

    def pop_menu(self):
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()
            self.menu_state = self.menu_stack[-1] # Return to the previous state
        elif len(self.menu_stack) == 1:
            self.menu_state = self.menu_stack[0]
        else:
            # self.menu_state = "main" 
            print("Stack is empty, cannot pop.")

    def quit_game(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    game = None
    graphic = Graphic(screen=screen, width=1280, height=720)
    menu = Menu(screen, game, graphic)
    
    while menu.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu.running = False
                pygame.quit()
                sys.exit()
                
        menu.show_main_menu()