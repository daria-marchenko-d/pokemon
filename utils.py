import json
import pygame
import os
import random
import requests
from io import BytesIO

# --- Gestion JSON ---
def charger_json(fichier):
    """
    Charge un fichier JSON et retourne son contenu sous forme de liste.
    Retourne une liste vide en cas d'erreur.
    """
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def enregistrer_json(fichier, data):
    """
    Enregistre les données dans un fichier JSON.
    """
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# --- Fonctions d'affichage ---
def afficher_texte(fenetre, texte, position, taille=24, couleur=(255,255,255)):
    """
    Affiche un texte sur la fenêtre Pygame.
    """
    font = pygame.font.Font(None, taille)
    surface = font.render(texte, True, couleur)
    fenetre.blit(surface, position)

def dessiner_bouton(fenetre, texte, position, taille=(200,50), couleur=(0,128,255)):
    """
    Dessine un bouton interactif sur la fenêtre Pygame.
    """
    rect = pygame.Rect(position, taille)
    pygame.draw.rect(fenetre, couleur, rect)
    afficher_texte(fenetre, texte, (position[0]+10, position[1]+10), 30)
    return rect

# --- Table des types Pokémon ---
table_types = {
    "Normal": {"Roc": 0.5, "Spectre": 0, "Acier": 0.5},
    "Feu": {"Feu": 0.5, "Eau": 0.5, "Plante": 2, "Glace": 2, "Insecte": 2, "Acier": 2, "Roche": 0.5, "Dragon": 0.5},
    "Eau": {"Feu": 2, "Eau": 0.5, "Plante": 0.5, "Sol": 2, "Roche": 2, "Dragon": 0.5},
    "Plante": {"Feu": 0.5, "Eau": 2, "Plante": 0.5, "Poison": 0.5, "Vol": 0.5, "Insecte": 0.5, "Sol": 2, "Roche": 2, "Dragon": 0.5, "Acier": 0.5},
    "Électrik": {"Eau": 2, "Électrik": 0.5, "Plante": 0.5, "Sol": 0, "Vol": 2, "Dragon": 0.5},
    "Glace": {"Feu": 0.5, "Eau": 0.5, "Plante": 2, "Glace": 0.5, "Sol": 2, "Vol": 2, "Dragon": 2, "Acier": 0.5},
    "Combat": {"Normal": 2, "Glace": 2, "Roche": 2, "Spectre": 0, "Poison": 0.5, "Vol": 0.5, "Psy": 0.5, "Insecte": 0.5, "Ténèbres": 2, "Fée": 0.5},
    "Poison": {"Plante": 2, "Sol": 0.5, "Roche": 0.5, "Spectre": 0.5, "Acier": 0, "Fée": 2},
    "Sol": {"Feu": 2, "Électrik": 2, "Plante": 0.5, "Poison": 2, "Vol": 0, "Roche": 2, "Acier": 2},
    "Vol": {"Électrik": 0.5, "Combat": 2, "Plante": 2, "Sol": 0, "Roche": 0.5, "Acier": 0.5},
    "Psy": {"Combat": 2, "Poison": 2, "Acier": 0.5, "Psy": 0.5, "Ténèbres": 0},
    "Insecte": {"Feu": 0.5, "Combat": 0.5, "Plante": 2, "Poison": 0.5, "Vol": 0.5, "Psy": 2, "Spectre": 0.5, "Acier": 0.5, "Fée": 0.5},
    "Roche": {"Feu": 2, "Glace": 2, "Combat": 0.5, "Sol": 0.5, "Vol": 2, "Acier": 0.5},
    "Spectre": {"Normal": 0, "Psy": 2, "Spectre": 2, "Ténèbres": 0.5},
    "Dragon": {"Dragon": 2, "Acier": 0.5, "Fée": 0},
    "Ténèbres": {"Combat": 0.5, "Psy": 2, "Spectre": 2, "Ténèbres": 0.5, "Fée": 0.5},
    "Acier": {"Feu": 0.5, "Eau": 0.5, "Électrik": 0.5, "Glace": 2, "Roche": 2, "Acier": 0.5, "Fée": 2},
    "Fée": {"Combat": 2, "Poison": 0.5, "Acier": 0.5, "Dragon": 2, "Ténèbres": 2}
}

def calculer_dommages(attaquant, defenseur):
    """
    Calcule les dégâts en fonction de l'attaque, la défense et des types.
    """
    base = random.randint(10, 25)
    type_attaquant = attaquant["type"][0] if isinstance(attaquant["type"], list) else attaquant["type"]
    type_defenseur = defenseur["type"][0] if isinstance(defenseur["type"], list) else defenseur["type"]
    modificateur = table_types.get(type_attaquant, {}).get(type_defenseur, 1)
    dommages = int((attaquant["attaque"] * modificateur) - defenseur["defense"] + base)
    return max(0, dommages)

# --- Récupération des sprites Pokémon via l'API PokéAPI ---
def get_pokemon_sprite(nom, side="front"):
    """
    Récupère le sprite du Pokémon via l'API PokéAPI.
    """
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{nom.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()
        sprite_url = data["sprites"].get("front_default" if side == "front" else "back_default")

        if not sprite_url:
            return None

        sprite_response = requests.get(sprite_url)
        image_bytes = BytesIO(sprite_response.content)
        sprite = pygame.image.load(image_bytes).convert_alpha()
        sprite = pygame.transform.scale(sprite, (150, 150))

        return sprite
    except Exception:
        return None
