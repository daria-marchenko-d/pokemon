# after solving the go back problem, but not menu problem
import pygame
import sys
from graphic import Graphic 

class Menu:
    def __init__(self, game_screen, game, graphic):
        self.screen = game_screen
        self.game = game
        self.graphic = graphic
        self.WIDTH, self.HEIGHT = game_screen.get_size()
        self.running = True
        self.menu_state = "main"  # Просто зберігаємо поточний стан меню

    def show_main_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.graphic.draw_menu_background()

            # Кнопки головного меню
            if self.menu_state == "main":
                if self.graphic.draw_button(240, "Start game", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "game"
                if self.graphic.draw_button(310, "Add pokemon", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "pokemon"
                if self.graphic.draw_button(380, "Pokedex", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "pokedex"
                if self.graphic.draw_button(450, "Rules and Settings", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "rules_settings"
                if self.graphic.draw_button(520, "Exit", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.quit_game()

            # Кнопки меню гри
            elif self.menu_state == "game":
                if self.graphic.draw_button(240, "New part", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "new_part"
                if self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "main"

            # Кнопки нової частини
            elif self.menu_state == "new_part":
                if self.graphic.draw_button(170, "Your name", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.user_name()
                if self.graphic.draw_button(520, "Go back", self.graphic.GRAY, self.graphic.HIGHLIGHT):
                    self.menu_state = "game"

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

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

        return text

    def quit_game(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    game = None
    graphic = Graphic(game)
    menu = Menu(screen, game, graphic)
    
    while menu.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu.running = False
                pygame.quit()
                sys.exit()
                
        menu.show_main_menu()