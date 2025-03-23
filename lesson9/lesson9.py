import time
import random
from colorama import Fore
import datetime
import json
import os
from entities import Player, Monster

turn = 0
variants = ["защита", "атака"]
characters = ["Игрок", "Монстр"]
SAVE_FILE = r"save.json"

player = Player(hp=100)
monster = Monster(hp=100)

def process_choice(player_choice, player_damage, player_armor, monster_choice, monster_damage, monster_armor):
    if player_choice == "защита" and monster_choice == "защита": # Защита + защита
        print("Два дурачка стоят и защищаются! Ахахахах!\n")
    elif player_choice == "защита" and monster_choice == "атака": # Защита + атака
        print(f"Ты защищаешься (защита: {player_armor})\nМонстр атакует! (урон: {monster_damage})\n")
        damage = monster_damage - player_armor
        damage = damage if damage > 0 else 0
        player.get_damage(damage)
        time.sleep(1)
        print(f"Ты получил урон: {damage}\n")
    elif player_choice == "атака" and monster_choice == "защита": # Атака + защита
        print(f"Ты атакуешь! (урон: {player_damage})\nМонстр защищается! (защита: {monster_armor})\n")
        damage = player_damage - monster_armor
        damage = damage if damage > 0 else 0
        monster.get_damage(damage)
        time.sleep(1)
        print(f"Монстр получил урон: {damage}\n")
    elif player_choice == "атака" and monster_choice == "атака": # Атака + атака
        print(f"Ты атакуешь! (урон: {player_damage})\nМонстр атакует! (урон: {monster_damage})\n")
        player.get_damage(monster_damage); monster.get_damage(player_damage)
        time.sleep(1)
        print(f"Ты получил урон: {monster_damage}\nМонстр получил урон: {player_damage}\n")
def save_game():
    with open(SAVE_FILE, "w") as save:
        json.dump({
        "time": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "move": turn,
        "player_hp": player_hp,
        "monster_hp": monster_hp
    }, save)
def load_game():
    try:
        with open(SAVE_FILE, 'r') as save:
            return json.load(save)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


os.system("cls" if os.name == "nt" else "clear")
print("Добро пожаловать в игру про драки с монстром!")
data = load_game()
while True:
    if data:
        user_input = input(f"{Fore.YELLOW}Обнаружен файл сохранения с {data.get('time')[0:10]}. Хотите продолжить игру? (да/нет)\n> {Fore.RESET}").lower()
        if user_input == "да":
            player_hp = data.get("player_hp")
            monster_hp = data.get("monster_hp")
            turn = data.get("move")
        elif user_input == "нет":
            if os.path.exists(SAVE_FILE): os.remove(SAVE_FILE)
        else:
            print(f"{Fore.RED}Такого варианта нет!{Fore.RESET}")
            continue
        os.system("cls" if os.name == "nt" else "clear")
        print("Добро пожаловать в игру про драки с монстром!")
    break


while True:
    turn += 1

    player_damage, player_armor = player.random_dmg_and_arm(3, 20, 1, 15)
    monster_damage, monster_armor = monster.random_dmg_and_arm(3, 20, 1, 15)

    player.display_health()
    monster.display_health()

    print(f"Ход: {turn}")
    player_choice = player.make_choice(variants)
    monster_choice = monster.make_choice(variants)

    time.sleep(1)
    print("Ты выбрал", player_choice)
    time.sleep(1)
    print("Монстр выбрал", monster_choice + "\n")
    time.sleep(1)

    process_choice(player_choice, player_damage, player_armor, monster_choice, monster_damage, monster_armor)

    time.sleep(1.5)

    if player.hp <= 0 or monster_hp <= 0:
        player.die() if player.hp <= 0 else monster.die()
        break

    save_game()
print(f"Игра закончилась на {turn} ходе!")
if os.path.exists(SAVE_FILE): os.remove(SAVE_FILE)