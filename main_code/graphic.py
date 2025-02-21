import pygame
import os
import json

class Graphic:
    def __init__(self, screen, width=1280, height=720):
        self.WIDTH = width 
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen = screen

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
        self.default_font = pygame.font.SysFont("Harrington", 50)
        self.default_small_font = pygame.font.SysFont("Harrington", 30)
        
        # Ukrainian fonts
        self.ua_font = pygame.font.SysFont("Segoe UI", 50)
        self.ua_small_font = pygame.font.SysFont("Segoe UI", 30)

        self.running = True

        # Load languages
        self.languages = self.load_languages("main_code/data/pokemon.json")
        self.current_language = "english"
        self.texts = {}  # Add the texts for the current language

        self.pokemon_sprites = self.load_pokemon_sprites("main_code/pictures/pokemon_sprites")

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

    def load_languages(self, path):
# Load the languages from the file
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
        print(f"The file {path} is not found!")
        return {}

    def set_language(self, language):
        # Change the current language
        if language in self.languages:
            self.current_language = language
            print(f"Language changed to {language}")
            return self.languages[language]
        else:
            print(f"The language '{language}' Is not found!")
            return self.languages["english"]

    def get_text(self, key):
        # Get the text from the current language
        # return self.languages.get(self.current_language, {}).get(key, key)
        current_lang_texts = self.languages.get(self.current_language, self.languages["english"])
        return current_lang_texts.get(key, key)
    
    def set_texts(self, texts):
        # Update the texts for the current language
        self.texts = texts
        print(f"The text is update to {self.current_language}")

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
    
    def display_pokemon(self, pokemon_name, position):
        if pokemon_name in self.pokemon_sprites:
            self.screen.blit(self.pokemon_sprites[pokemon_name], position)
        else:
            print(f"Sprite for {pokemon_name} is not found!")
    
    def draw_button(self, y, key, default_color, hover_color):
        # Chose the font
        font = self.ua_font if self.current_language == "ukrainian" else self.default_font
        
        try:
            # Translation from json file
            if isinstance(key, str):  
                text = self.texts.get(key, key)  # Take the text from the dictionary
            else:
                text = str(key) 
                
            text_surface = font.render(text, True, self.BLACK)
            text_rect = text_surface.get_rect(center=(self.WIDTH // 2, y + 25))
            width = text_rect.width + 40
            height = 50
            x = (self.WIDTH - width) // 2
            button_rect = pygame.Rect(x, y, width, height)

            mouse = pygame.mouse.get_pos()
            is_hovered = button_rect.collidepoint(mouse)

            if is_hovered:
                pygame.draw.rect(self.screen, hover_color, button_rect)
                if pygame.mouse.get_pressed()[0]:
                    pygame.time.wait(150)  
                    pygame.event.clear()  
                    return True
            else:
                pygame.draw.rect(self.screen, default_color, button_rect)

            self.screen.blit(text_surface, text_rect)
        except Exception as e:
            print(f"Error drawing button: {e}")
        return False

# Pygame initialization
pygame.init()

# Font initialization
pygame.font.init()

#  mixer initialization
pygame.mixer.init()

graphic = Graphic(screen=pygame.display.set_mode((1280, 720)))

# if __name__ == "__main__":
    # pygame.init()
    # screen = pygame.display.set_mode((1280, 720))
    # # Send the screen to the Graphic constructor
    # graphic = Graphic() 
    
    # # Test the draw_button method
    # running = True
    # while running:
    #     graphic.draw_menu_background()
    #     # graphic.draw_button(100, "Test Button", graphic.GRAY, graphic.HIGHLIGHT, lambda: print("Button Pressed"))
    #     pygame.display.flip()
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    # pygame.quit()