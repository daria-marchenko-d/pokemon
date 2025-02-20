import os
import json
import pygame

class Pokedex:
    pass

def generate_pokemon_json(image_directory, output_json_file):
    # List all PNG files in the directory
    files = os.listdir(image_directory)
    png_files = [file for file in files if file.endswith('.png')]
    
    # Create a dictionary for Pokémon data
    pokemon_data = {
        "en": {
            "title": "Pokemon Battle",
            "pokemon": {
                "available": {},
                "unavailable": {}
            }
        }
    }
    
    # Populate the available and unavailable sections
    for i, file in enumerate(png_files):
        pokemon_key = os.path.splitext(file)[0]
        pokemon_entry = {
            "name": pokemon_key.capitalize(),
            "level": 5,
            "hit_points": 50,
            "type_": "unknown",
            "attack": 50,
            "defense": 50
        }
        
        if i % 2 == 0:
            pokemon_data["en"]["pokemon"]["available"][pokemon_key] = pokemon_entry
        else:
            pokemon_data["en"]["pokemon"]["unavailable"][pokemon_key] = pokemon_entry
    
    # Write the JSON data to the output file
    with open(output_json_file, "w") as f:
        json.dump(pokemon_data, f, indent=4)

def draw_rounded_rect(surface, color, rect, corner_radius):
    """ Draw a rectangle with rounded corners.
    We use anti-aliased circles to make the corners smooth.
    """
    if corner_radius > min(rect[2], rect[3]) // 2:
        corner_radius = min(rect[2], rect[3]) // 2

    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

def display_images(image_directory, data_file, background_image_path):
    pygame.init()
    pygame.mixer.init()  # Initialize the mixer module
    screen = pygame.display.set_mode((800, 600))  # Decrease window size
    pygame.display.set_caption("Pokedex")
    clock = pygame.time.Clock()
    
    # Load and resize background image
    background_image = pygame.image.load(background_image_path)
    background_image = pygame.transform.scale(background_image, (800, 600))
    
    # Load Pokémon data from JSON file
    with open(data_file) as f:
        pokemon_data = json.load(f)['en']['pokemon']
    
    pokemon_keys = list(pokemon_data['available'].keys()) + list(pokemon_data['unavailable'].keys())
    current_index = 0
    
    # Load the Comic Sans MS font with a smaller size
    font = pygame.font.SysFont("Comic Sans MS", 24)
    
    # Load and play background music
    pygame.mixer.music.load("main_code/sounds/menu.mp3")  # Change this to your sound file path
    pygame.mixer.music.play(-1)  # Play the music in a loop
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_index = (current_index + 1) % len(pokemon_keys)
                elif event.key == pygame.K_LEFT:
                    current_index = (current_index - 1) % len(pokemon_keys)
        
        screen.fill((255, 255, 255))
        
        # Display background image
        screen.blit(background_image, (0, 0))
        
        # Get the Pokémon key and data
        pokemon_key = pokemon_keys[current_index]
        if pokemon_key in pokemon_data['available']:
            pokemon = pokemon_data['available'][pokemon_key]
            availability_text = "Available"
            availability_color = (0, 255, 0)  # Green
        else:
            pokemon = pokemon_data['unavailable'][pokemon_key]
            availability_text = "Unavailable"
            availability_color = (255, 0, 0)  # Red
        
        # Load and display the Pokémon image
        image_path = os.path.join(image_directory, f"{pokemon_key}.png")
        try:
            pokemon_image = pygame.image.load(image_path)
            # Resize the Pokémon image (maintain size at 325x325)
            pokemon_image = pygame.transform.scale(pokemon_image, (325, 325))  # Maintain size
            # Center the Pokémon image and shift it to the left and up
            image_rect = pokemon_image.get_rect(center=(screen.get_width() // 2 - 100, screen.get_height() // 2 - 15))
            screen.blit(pokemon_image, image_rect.topleft)
        except pygame.error:
            print(f"Image not found at {image_path}")
        
        # Display Pokémon information
        info_text = f"Name: {pokemon['name']}\nLevel: {pokemon['level']}\nHP: {pokemon['hit_points']}\nType: {pokemon['type_']}\nAttack: {pokemon['attack']}\nDefense: {pokemon['defense']}"
        y_offset = 120  # Move descriptions slightly down
        for line in info_text.split('\n'):
            text_surface = font.render(line, True, (0, 0, 0))
            # Position the text further to the right
            text_x = screen.get_width() - text_surface.get_width() - 100
            screen.blit(text_surface, (text_x, y_offset))
            y_offset += 40  # Adjust line spacing
        
        # Display availability text with rounded rectangle
        availability_surface = font.render(availability_text, True, (0, 0, 0))
        availability_rect = availability_surface.get_rect(topleft=(text_x, y_offset + 10))
        draw_rounded_rect(screen, availability_color, availability_rect.inflate(20, 20), 10)
        screen.blit(availability_surface, availability_rect)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    print("Pygame quit")

if __name__ == "__main__":
    image_directory = "main_code/pokemon_sprites"
    output_json_file = "main_code/data/generated_pokemon.json"
    background_image_path = "main_code/pokedex-background/pokedex.jpg"  # Change this to your background image path
    
    # Generate the JSON file
    generate_pokemon_json(image_directory, output_json_file)
    
    # Display the images and information
    display_images(image_directory, output_json_file, background_image_path)