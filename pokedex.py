import pygame
import sys
from utils import afficher_texte, dessiner_bouton, charger_json

class Pokedex:
    def __init__(self, fenetre, menu_principal_func):
        """
        Initialise l'affichage du Pokédex.
        """
        self.fenetre = fenetre
        self.menu_principal_func = menu_principal_func
        self.pokedex = charger_json("data/pokedex.json")  # Charger les Pokémon rencontrés

    def run(self):
        """
        Affiche le Pokédex avec les Pokémon rencontrés.
        """
        running = True
        while running:
            self.fenetre.fill((0, 0, 0))
            afficher_texte(self.fenetre, "Pokédex", (350, 50), 36)

            # Vérifie si le Pokédex est vide
            if not self.pokedex:
                afficher_texte(self.fenetre, "Aucun Pokémon enregistré.", (250, 250), 28, (255, 0, 0))
            else:
                y_offset = 120  # Position de départ de l'affichage des Pokémon
                for pokemon in self.pokedex:
                    nom = pokemon.get("nom", "Inconnu")
                    type_pokemon = ', '.join(pokemon.get("type", ["Inconnu"]))
                    afficher_texte(self.fenetre, f"{nom} - Type: {type_pokemon}", (250, y_offset), 24, (255, 255, 255))
                    y_offset += 40  # Décalage pour afficher les suivants

            # Bouton Retour
            bouton_retour = dessiner_bouton(self.fenetre, "Retour", (300, 500))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_retour.collidepoint(event.pos):
                        self.menu_principal_func()  # Retour au menu principal
                        return
