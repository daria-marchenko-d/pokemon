# before fixed the problems with go back and menu start game
import pygame
import os

class Graphic:
    def __init__(self, game, width=1280, height=720):
        self.WIDTH = width 
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.game = game

        pygame.display.set_caption("Pokémon Game")
        self.clock = pygame.time.Clock()

        # Colors
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 200, 50)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.HIGHLIGHT = (100, 149, 237)
        self.BLUE = (0, 0, 255)

        self.FPS = 30

        # Game background 
        self.background = pygame.image.load("main_code/pictures/menu-background.jpg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        # battle background
        self.battle_background = pygame.image.load("main_code/pictures/battle_background.png")
        self.battle_background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        # If there is no file, or load: 
        # self.battle_background = None  

        # Music
        self.music = pygame.mixer.music.load("main_code/sounds/menu.mp3")
        pygame.mixer.music.play(-1)

        # Fonts
        self.font = pygame.font.SysFont("Harrington", 50)
        self.small_font = pygame.font.SysFont("Harrington", 30)

        self.running = True

        self.pokemon_sprites = self.load_pokemon_sprites("main_code/pictures/pokemon_sprites")

    def draw_menu_background(self):

        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill((200, 200, 255))  

    def draw_battle_background(self):

        if self.battle_background:            
            self.screen.blit(self.battle_background, (0, 0))
        else:
            self.screen.fill((150, 150, 255))  
    
    def load_image(self, path):
        if os.path.exists(path):
            return pygame.image.load(path)
        else:
            print(f"The file {path} is not found!")
            return None

    def load_pokemon_sprites(self, folder_path):
        sprites = {}
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith((".png", ".jpg")):
                    name = filename.split(".")[0]
                    sprites[name] = pygame.image.load(os.path.join(folder_path, filename))
        else:
            print(f"The folder {folder_path} is not found!")
        return sprites  

    def display_pokemon(self, pokemon_name, position):
        if pokemon_name in self.pokemon_sprites:
            self.screen.blit(self.pokemon_sprites[pokemon_name], position)
        else:
            print(f"Sprite for {pokemon_name} is not found!")
    
    def draw_button(self, y, text, default_color, hover_color, action=None):
        button_y = y
        button_text = text
        text_surface = self.font.render(button_text, True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, button_y + 25))
        width = text_rect.width + 40  
        height = 50
        x = (self.WIDTH - width) // 2

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + width and button_y < mouse[1] < button_y + height:
            pygame.draw.rect(self.screen, hover_color, (x, button_y, width, height))
            if click[0] == 1 and action is not None:
                # pygame.time.delay(150)
                action()
                return True
        else:
            pygame.draw.rect(self.screen, default_color, (x, button_y, width, height))

        self.screen.blit(text_surface, text_rect)
        return None  # Якщо кнопка не натиснута, повертаємо None

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    # Send the screen to the Graphic constructor
    graphic = Graphic() 
    
    # Test the draw_button method
    running = True
    while running:
        graphic.draw_menu_background()
        # graphic.draw_button(100, "Test Button", graphic.GRAY, graphic.HIGHLIGHT, lambda: print("Button Pressed"))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()