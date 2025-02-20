import pygame
import random
import sys
from utils import afficher_texte, dessiner_bouton, calculer_dommages, get_pokemon_sprite, enregistrer_json, charger_json

class Combat:
    def __init__(self, screen, pokemon_joueur, adversaire):
        """
        Initialise le combat entre le Pokémon du joueur et un adversaire.
        """
        self.screen = screen
        self.pokemon_joueur = pokemon_joueur
        self.adversaire = adversaire
        self.clock = pygame.time.Clock()
        self.sauvegarde_fichier = "data/sauvegarde.json"

        # Charger les sprites
        self.sprite_joueur = get_pokemon_sprite(self.pokemon_joueur["nom"], "back")
        self.sprite_adversaire = get_pokemon_sprite(self.adversaire["nom"], "front")

    def run(self):
        """
        Boucle principale du combat Pokémon.
        """
        running = True
        while running:
            self.screen.fill((50, 50, 50))
            afficher_texte(self.screen, "Combat Pokémon !", (300, 50), 36, (255, 255, 255))

            # Affichage des Pokémon et de leurs PV
            if self.sprite_adversaire:
                self.screen.blit(self.sprite_adversaire, (500, 100))
            afficher_texte(self.screen, f"{self.adversaire['nom']} - PV: {self.adversaire['pv']}", (500, 250), 28, (255, 255, 255))

            if self.sprite_joueur:
                self.screen.blit(self.sprite_joueur, (100, 300))
            afficher_texte(self.screen, f"{self.pokemon_joueur['nom']} - PV: {self.pokemon_joueur['pv']}", (100, 450), 28, (255, 255, 255))

            # Boutons d'action
            attack_btn = dessiner_bouton(self.screen, "Attaquer", (100, 500))
            change_btn = dessiner_bouton(self.screen, "Changer", (300, 500))
            run_btn = dessiner_bouton(self.screen, "Abandonner", (500, 500))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if attack_btn.collidepoint(event.pos):
                        self.attaquer()
                    elif change_btn.collidepoint(event.pos):
                        print("Changement de Pokémon pas encore implémenté.")
                    elif run_btn.collidepoint(event.pos):
                        self.sauvegarder_progression()
                        return

            self.clock.tick(30)

    def attaquer(self):
        """
        Gère l'attaque du Pokémon du joueur sur l'adversaire.
        """
        degats = calculer_dommages(self.pokemon_joueur, self.adversaire)
        print(f"{self.pokemon_joueur['nom']} attaque {self.adversaire['nom']} et inflige {degats} dégâts !")
        self.adversaire["pv"] -= degats

        # Vérifier si l'adversaire est K.O.
        if self.adversaire["pv"] <= 0:
            print(f"{self.adversaire['nom']} est K.O. !")
            self.fin_du_combat()
            return

        # L'adversaire attaque en retour
        self.attaque_adversaire()

    def attaque_adversaire(self):
        """
        Gère l'attaque de l'adversaire contre le joueur.
        """
        degats = calculer_dommages(self.adversaire, self.pokemon_joueur)
        print(f"{self.adversaire['nom']} attaque {self.pokemon_joueur['nom']} et inflige {degats} dégâts !")
        self.pokemon_joueur["pv"] -= degats

        # Vérifier si le Pokémon du joueur est K.O.
        if self.pokemon_joueur["pv"] <= 0:
            print(f"{self.pokemon_joueur['nom']} est K.O. !")
            self.fin_du_combat()
            return

    def fin_du_combat(self):
        """
        Affiche le menu de fin de combat et propose de continuer ou de sauvegarder.
        """
        running = True
        while running:
            self.screen.fill((50, 50, 50))
            afficher_texte(self.screen, "Combat terminé !", (300, 100), 36, (255, 255, 255))

            continuer_btn = dessiner_bouton(self.screen, "Continuer", (200, 300))
            sauvegarder_btn = dessiner_bouton(self.screen, "Sauvegarder & Quitter", (400, 300))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if continuer_btn.collidepoint(event.pos):
                        self.nouveau_combat()
                        return
                    elif sauvegarder_btn.collidepoint(event.pos):
                        self.sauvegarder_progression()
                        pygame.quit()
                        sys.exit()

            self.clock.tick(30)

    def nouveau_combat(self):
        """
        Démarre un nouveau combat contre un adversaire aléatoire.
        """
        print("Un nouvel adversaire apparaît !")
        nouveaux_pokemons = charger_json("data/pokemon.json")
        nouvel_adversaire = random.choice(nouveaux_pokemons)
        self.adversaire = nouvel_adversaire
        self.sprite_adversaire = get_pokemon_sprite(self.adversaire["nom"], "front")
        self.pokemon_joueur["pv"] = 50  # Remettre des PV pour le prochain combat
        self.run()

    def sauvegarder_progression(self):
        """
        Sauvegarde l'état du Pokémon du joueur dans un fichier JSON.
        """
        sauvegarde = {
            "joueur": self.pokemon_joueur
        }
        enregistrer_json(self.sauvegarde_fichier, sauvegarde)
        print("Progression sauvegardée !")
