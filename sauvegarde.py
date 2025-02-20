import json

SAVE_FILE = "data/save.json"

def save_game(data):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_game(screen):
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Ici, vous pouvez ajouter une interface graphique pour afficher la sauvegarde
            print("Partie chargée :", data)
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
