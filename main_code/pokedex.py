

import json
import os

class Pokedex:
    """Клас для зберігання та керування інформацією про покемонів"""

    def __init__(self, filename="data/pokedex.json"):
        self.filename = filename
        self.pokemon_data = self.load_pokedex()

    def load_pokedex(self):
        """Завантаження покемонів із JSON-файлу"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    def save_pokedex(self):
        """Збереження оновленого списку покемонів у JSON"""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.pokemon_data, file, indent=4, ensure_ascii=False)

    def add_pokemon(self, name, level, p_type, attack, defense, life_point):
        """Додає нового покемона в Покедекс, якщо його ще немає"""
        if name not in self.pokemon_data:
            self.pokemon_data[name] = {
                "level": level,
                "type": p_type,
                "attack": attack,
                "defense": defense,
                "life_point": life_point
            }
            self.save_pokedex()
            print(f"✅ {name} додано в Покедекс!")
        else:
            print(f"⚠️ {name} вже є в Покедексі!")

    def get_pokemon(self, name):
        """Отримання інформації про покемона за ім'ям"""
        return self.pokemon_data.get(name, None)

    def is_pokemon_in_pokedex(self, name):
        """Перевіряє, чи є покемон у Покедексі"""
        return name in self.pokemon_data


# Тестування
if __name__ == "__main__":
    pokedex = Pokedex()

    # Додаємо покемонів
    pokedex.add_pokemon("Pikachu", 5, "electric", 10, 5, 35)
    pokedex.add_pokemon("Charmander", 5, "fire", 12, 4, 39)

    # Отримуємо інформацію
    print(pokedex.get_pokemon("Pikachu"))
    print(pokedex.get_pokemon("Bulbasaur"))  # Не існує

    # Перевіряємо наявність у Покедексі
    print("Pikachu в Покедексі?", pokedex.is_pokemon_in_pokedex("Pikachu"))  # True
    print("Bulbasaur в Покедексі?", pokedex.is_pokemon_in_pokedex("Bulbasaur"))  # False
