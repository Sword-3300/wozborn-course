import time
import random
from colorama import Fore
import datetime
import json
import os

player_hp = 100
monster_hp = 100
turn = 0
variants = ["защита", "атака"]
characters = ["Игрок", "Монстр"]
SAVE_FILE = r"save.json"


def random_dmg_and_arm(min_damage, max_damage, min_armor, max_armor):
    return [random.randint(min_damage, max_damage), random.randint(min_armor, max_armor)]

def player_choice():
    while True:
        choice = input("Что ты выберешь(Защита/Атака)? (Q для выхода)\n> ").lower()
        if choice == "q":
            print("Выход из игры...")
            exit()
        if choice in variants: break
        else: print(f"{Fore.RED}Такого варианта нет!{Fore.RESET}")
    return choice

def monster_choice():
    return random.choice(variants)

def process_choice(player_choice, player_damage, player_armor, monster_choice, monster_damage, monster_armor):
    global player_hp, monster_hp
    if player_choice == "защита" and monster_choice == "защита": # Защита + защита
        print("Два дурачка стоят и защищаются! Ахахахах!\n")
    elif player_choice == "защита" and monster_choice == "атака": # Защита + атака
        print(f"Ты защищаешься (защита: {player_armor})\nМонстр атакует! (урон: {monster_damage})\n")
        damage = player_armor - monster_damage
        damage = damage if damage < 0 else 0
        player_hp += damage
        time.sleep(1)
        print(f"Ты получил урон: {abs(damage)}\n")
    elif player_choice == "атака" and monster_choice == "защита": # Атака + защита
        print(f"Ты атакуешь! (урон: {player_damage})\nМонстр защищается! (защита: {monster_armor})\n")
        damage = monster_armor - player_damage
        damage = damage if damage < 0 else 0
        monster_hp += damage
        time.sleep(1)
        print(f"Монстр получил урон: {abs(damage)}\n")
    elif player_choice == "атака" and monster_choice == "атака": # Атака + атака
        print(f"Ты атакуешь! (урон: {player_damage})\nМонстр атакует! (урон: {monster_damage})\n")
        player_hp -= monster_damage; monster_hp -= player_damage
        time.sleep(1)
        print(f"Ты получил урон: {monster_damage}\nМонстр получил урон: {player_damage}\n")

def die(character):
    print(Fore.RED + f"{character} погиб!" + Fore.RESET)
    winner = "Монстр" if character == "Игрок" else "Игрок"
    print(Fore.YELLOW + f"{winner.upper()} ПОБЕДИЛЛ!!!" + Fore.RESET)

def display_information(player_hp, monster_hp):
    print(Fore.CYAN + "Твоё здоровье:", player_hp)
    print("Здоровье монстра:", monster_hp, "\n\n" + Fore.RESET)

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

    player_damage, player_armor = random_dmg_and_arm(3, 20, 1, 15)
    monster_damage, monster_armor = random_dmg_and_arm(3, 20, 1, 15)

    display_information(player_hp, monster_hp)

    print(f"Ход: {turn}")
    player_action = player_choice()
    monster_action = monster_choice()

    time.sleep(1)
    print("Ты выбрал", player_action)
    time.sleep(1)
    print("Монстр выбрал", monster_action + "\n")
    time.sleep(1)

    process_choice(player_action, player_damage, player_armor, monster_action, monster_damage, monster_armor)

    time.sleep(1.5)

    if player_hp <= 0 or monster_hp <= 0:
        die("Игрок" if player_hp <= 0 else "Монстр")
        break

    save_game()

print(f"Игра закончилась на {turn} ходе!")