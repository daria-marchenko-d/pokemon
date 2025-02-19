# import pygame
# import sys
# import os

# pygame.init()

# WIDTH = 1280
# HEIGHT = 720
# pygame.display.set_caption("Pokemon Battle")
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# rect = screen.get_rect()



# FPS = 30
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 25)
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)
# YELLOW = (255, 200, 50)

# screen.fill(WHITE)

# def main_menu():
#     running = True
#     texts = ["Start Game", "Options", "Exit", "Settings", "Help", "Credits"]

#     while running:
#         screen.fill(WHITE)

#          # Mouse coordinates
#         mouse_x, mouse_y = pygame.mouse.get_pos()

#         # Center text
#         text_rects = []
#         for i, text in enumerate(texts):
#             rendered_text = font.render(text, True, YELLOW)
#             text_rect = rendered_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 40))
#             screen.blit(rendered_text, text_rect)
#             text_rects.append((text_rect, i))

#         pygame.display.update()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 for text_rect, index in text_rects:
#                     if text_rect.collidepoint(event.pos):
#                         print(f"Main menu option {[index]} selected.")
#                         if index == 0:
#                                 pass 
#                         elif index == 1:
#                                 pass
#                         elif index == 2:
#                             pass
#                         elif index == 3:
#                             pass
#                         elif index == 4:
#                             pass
#                         elif index == 5:
#                             pass
#         clock.tick(FPS)
# main_menu()


import pygame
import sys

class Screen:
    def __init__(self, width=1280, height=720):
        pygame.init()
        
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pokemon Battle")
        
        self.font = pygame.font.SysFont("Harrington", 50)
        self.clock = pygame.time.Clock()
        
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 200, 50)
        
        self.FPS = 30
        
        self.screen.fill(self.WHITE)  # Set initial background color

    def draw_menu(self, texts):
        # Display the main menu options on the screen
        self.screen.fill(self.WHITE)  # Clear the screen with white

        # Mouse coordinates
        mouse_x, mouse_y = pygame.mouse.get_pos()

        text_rects = []
        for i, text in enumerate(texts):
            rendered_text = self.font.render(text, True, self.YELLOW)
            text_rect = rendered_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 4 + i * 80))
            self.screen.blit(rendered_text, text_rect)
            text_rects.append((text_rect, i))

        pygame.display.update()

        return text_rects

    def handle_events(self, text_rects):
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for text_rect, index in text_rects:
                    if text_rect.collidepoint(event.pos):
                        print(f"Main menu option {index} selected.")
                        return index  # Return the selected index

        return None

    def run(self):
        running = True
        texts = ["Start Game", " Choose pokemon", "Rules", "Statistic", "Languages", "Exit"]
        
        while running:
            text_rects = self.draw_menu(texts)
            selected_option = self.handle_events(text_rects)

            if selected_option is not None:
                # Implement actions based on selected option
                if selected_option == 0:
                    pass  # Action for Start Game
                elif selected_option == 1:
                    pass  # Action for Options
                elif selected_option == 2:
                    pass  # Action for Exit
                elif selected_option == 3:
                    pass  # Action for Settings
                elif selected_option == 4:
                    pass  # Action for Help
                elif selected_option == 5:
                    pass  # Action for Credits

            self.clock.tick(self.FPS)
    

if __name__ == "__main__":
    game_screen = Screen()  # Create an instance of the Screen class
    game_screen.run()  # Run the main menu
