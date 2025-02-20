import pygame
import sys
import random  # 🔹 Ajout de l'import pour gérer le choix aléatoire du type
from selection_pokemon import SelectionPokemon
from pokedex import Pokedex
from sauvegarde import load_game
from utils import dessiner_bouton, afficher_texte, charger_json, enregistrer_json, attaques_par_type

LARGEUR, HAUTEUR = 800, 600

def menu_principal():
    """
    Affiche le menu principal du jeu Pokémon.
    """
    pygame.init()
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Menu Pokémon")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        fenetre.fill((0, 0, 0))
        afficher_texte(fenetre, "Pokemon RPG", (280, 50), 48, (255,255,255))
        
        # Boutons du menu
        new_game_btn = dessiner_bouton(fenetre, "Nouvelle Partie", (300, 150))
        pokedex_btn = dessiner_bouton(fenetre, "Pokédex", (300, 230))
        load_game_btn = dessiner_bouton(fenetre, "Charger Partie", (300, 310))
        add_pokemon_btn = dessiner_bouton(fenetre, "Ajouter un Pokémon", (300, 390))
        quit_btn = dessiner_bouton(fenetre, "Quitter", (300, 470))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if new_game_btn.collidepoint(x, y):
                    SelectionPokemon(fenetre, menu_principal).run()
                elif pokedex_btn.collidepoint(x, y):
                    Pokedex(fenetre, menu_principal).run()
                elif load_game_btn.collidepoint(x, y):
                    load_game(fenetre)
                    menu_principal()
                elif add_pokemon_btn.collidepoint(x, y):
                    ajouter_pokemon_interface(fenetre, menu_principal)
                elif quit_btn.collidepoint(x, y):
                    running = False
        clock.tick(30)
    sys.exit()

def ajouter_pokemon_interface(fenetre, menu_principal_func):
    """
    Interface graphique pour ajouter un Pokémon avec sprites et attaques.
    """
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(250, 200, 300, 40)
    couleur_active = (255, 255, 255)
    couleur_inactive = (200, 200, 200)
    couleur = couleur_inactive
    actif = False
    texte = ""

    running = True
    while running:
        fenetre.fill((0, 0, 0))
        afficher_texte(fenetre, "Entrez le nom du Pokémon :", (250, 150), 30, (255,255,255))

        pygame.draw.rect(fenetre, couleur, input_box, 2)
        txt_surface = font.render(texte, True, (255,255,255))
        fenetre.blit(txt_surface, (input_box.x + 10, input_box.y + 5))

        bouton_retour = dessiner_bouton(fenetre, "Retour", (300, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    actif = True
                else:
                    actif = False
                couleur = couleur_active if actif else couleur_inactive
                if bouton_retour.collidepoint(event.pos):
                    menu_principal_func()
                    return
            elif event.type == pygame.KEYDOWN:
                if actif:
                    if event.key == pygame.K_RETURN:
                        if texte:
                            pokemons = charger_json("data/pokemon.json")
                            if texte.lower() not in [p["nom"].lower() for p in pokemons]:
                                type_pokemon = random.choice(list(attaques_par_type.keys()))  # 🔹 Choix aléatoire d'un type
                                nouveau_pokemon = {
                                    "nom": texte.capitalize(),
                                    "type": [type_pokemon],
                                    "pv": random.randint(40, 100),
                                    "attaque": random.randint(10, 30),
                                    "defense": random.randint(5, 20),
                                    "attaques": attaques_par_type[type_pokemon][:2],  # 🔹 Sélection de 2 attaques
                                    "sprites": {
                                        "face": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{texte.lower()}.png",
                                        "dos": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/{texte.lower()}.png"
                                    }
                                }
                                pokemons.append(nouveau_pokemon)
                                enregistrer_json("data/pokemon.json", pokemons)
                            menu_principal_func()
                            return
                    elif event.key == pygame.K_BACKSPACE:
                        texte = texte[:-1]
                    else:
                        texte += event.unicode

if __name__ == "__main__":
    menu_principal()
