import time
import random
from colorama import Fore

player_hp = 100
monster_hp = 100
variants = ["защита", "атака"]
characters = ["Игрок", "Монстр"]


def random_dmg_and_arm(min_damage, max_damage, min_armor, max_armor):
    return [random.randint(min_damage, max_damage), random.randint(min_armor, max_armor)]

def player_choice():
    while True:
        choice = input("\nЧто ты выберешь(Защита/Атака)?\n> ").lower()
        if choice in variants: break
        else: print("Такого варианта нет!")
    return choice

def monster_choice():
    return random.choice(variants)

def process_choice(player_choice, player_damage, player_armor, monster_choice, monster_damage, monster_armor):
    global player_hp, monster_hp
    if player_choice == "защита" and monster_choice == "защита":
        print("Два дурачка стоят и защищаются! Ахахахах!\n")
    elif player_choice == "защита" and monster_choice == "атака":
        print(f"Ты защищаешься (armor: {player_armor})")  # Защита + атака
        print(f"Монстр атакует! (damage: {monster_damage})\n")
        damage = player_armor - monster_damage
        damage = damage if damage < 0 else 0
        player_hp += damage
        time.sleep(1)
        print(f"Ты получил урон: {damage}\n")
    elif player_choice == "атака" and monster_choice == "защита":
        print(f"Ты атакуешь! (damage: {player_damage})")  # Атака + защита
        print(f"Монстр защищается! (armor: {monster_armor})\n")
        damage = monster_armor - player_damage
        damage = damage if damage < 0 else 0
        monster_hp += damage
        time.sleep(1)
        print(f"Монстр получил урон: {damage}\n")
    elif player_choice == "атака" and monster_choice == "атака":
        print(f"Ты атакуешь! (damage: {player_damage})")  # Атака + атака
        print(f"Монстр атакует! (damage: {monster_damage})\n")
        player_hp -= monster_damage
        time.sleep(1)
        print(f"Ты получил урон: {monster_damage}")
        monster_hp -= player_damage
        print(f"Монстр получил урон: {player_damage}\n")

def die(character):
    print(Fore.RED + f"{character} погиб!" + Fore.RESET)
    winner = "Монстр" if character == "Игрок" else "Игрок"
    print(Fore.YELLOW + f"{winner.upper()} WINS!!!" + Fore.RESET)

def display_information(player_hp, monster_hp):
    print(Fore.CYAN + "Твоё здоровье:", player_hp)
    print("Здоровье монстра:", monster_hp, "\n" + Fore.RESET)


print("Добро пожаловать в игру про драки с монстром!")
while True:
    player_damage, player_armor = random_dmg_and_arm(3, 20, 1, 10)
    monster_damage, monster_armor = random_dmg_and_arm(3, 20, 1, 10)

    display_information(player_hp, monster_hp)

    player_action = player_choice()

    time.sleep(1)
    print("Ты выбрал", player_action)
    time.sleep(1)
    monster_action = monster_choice(); print("Монстр выбрал", monster_action + "\n")
    time.sleep(1)

    process_choice(player_action, player_damage, player_armor, monster_action, monster_damage, monster_armor)

    time.sleep(1.5)

    if player_hp <= 0:
        die("Игрок")
        break
    if monster_hp <= 0:
        die("Монстр")
        break

print("Конец игры!")
