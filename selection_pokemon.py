import pygame
import random
import sys
from utils import charger_json, afficher_texte, dessiner_bouton
from combat import Combat

class SelectionPokemon:
    def __init__(self, screen, menu_principal_func):
        """
        Initialise la sélection de Pokémon avec la gestion des sprites et des données.
        """
        self.screen = screen
        self.menu_principal_func = menu_principal_func
        data = charger_json("data/pokemon.json")

        # Vérification du format des données
        if isinstance(data, list):
            self.pokemon_list = data
        else:
            self.pokemon_list = []  # En cas d'erreur de chargement

        self.clock = pygame.time.Clock()

    def run(self):
        """
        Affiche l'interface de sélection de Pokémon.
        """
        running = True
        index = 0

        while running:
            self.screen.fill((50, 50, 50))
            afficher_texte(self.screen, "Sélectionnez votre Pokémon", (220, 50), 36, (255, 255, 255))

            if not self.pokemon_list:
                afficher_texte(self.screen, "Aucun Pokémon disponible", (250, 250), 30, (255, 0, 0))
                pygame.display.flip()
                pygame.time.delay(2000)
                self.menu_principal_func()
                return

            current = self.pokemon_list[index]

            # Vérification que les clés existent pour éviter les erreurs
            nom = current.get("nom", "Inconnu")
            type_pokemon = ', '.join(current.get("type", ["Inconnu"]))
            pv = current.get("pv", 0)
            attaque = current.get("attaque", 0)
            defense = current.get("defense", 0)

            details = f"{nom} | Type: {type_pokemon} | PV: {pv} | ATK: {attaque} | DEF: {defense}"
            afficher_texte(self.screen, details, (100, 150), 28, (255, 255, 255))

            prev_btn = dessiner_bouton(self.screen, "<", (150, 300))
            next_btn = dessiner_bouton(self.screen, ">", (500, 300))
            select_btn = dessiner_bouton(self.screen, "Valider", (300, 400))
            back_btn = dessiner_bouton(self.screen, "Retour", (300, 480))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if prev_btn.collidepoint(event.pos):
                        index = (index - 1) % len(self.pokemon_list)
                    elif next_btn.collidepoint(event.pos):
                        index = (index + 1) % len(self.pokemon_list)
                    elif select_btn.collidepoint(event.pos):
                        pokemon_joueur = self.pokemon_list[index]
                        adversaire = random.choice(self.pokemon_list)
                        combat = Combat(self.screen, pokemon_joueur, adversaire)
                        combat.run()
                        return
                    elif back_btn.collidepoint(event.pos):
                        self.menu_principal_func()  # Retour au menu principal
                        return
            self.clock.tick(30)
