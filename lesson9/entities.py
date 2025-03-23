import random
from colorama import Fore

class Player:
    def __init__(self, hp):
        self.hp = hp

    def display_health(self):
        print(Fore.CYAN + "Твоё здоровье:", self.hp)

    def get_damage(self, damage):
        self.hp -= damage
        return self.hp

    def make_choice(self, variants):
        while True:
            choice = input(f"Что ты выберешь ({', '.join(variants)})? (Q для выхода)\n> ").lower()
            if choice == "q":
                print("Выход из игры...")
                exit()
            if choice in variants:
                break
            else:
                print(f"{Fore.RED}Такого варианта нет!{Fore.RESET}")
        return choice

    def random_dmg_and_arm(self, min_damage, max_damage, min_armor, max_armor):
        return random.randint(min_damage, max_damage), random.randint(min_armor, max_armor)

    def die(self):
        print(Fore.RED + f"{self} погиб!" + Fore.RESET)
        winner = "Монстр" if self == "Игрок" else "Игрок"
        print(Fore.YELLOW + f"{winner.upper()} ПОБЕДИЛЛ!!!" + Fore.RESET)

class Monster:
    def __init__(self, hp):
        self.hp = hp

    def display_health(self):
        print(Fore.CYAN + "Здоровье монстра:", self.hp)

    def get_damage(self, damage):
        self.hp -= damage
        return self.hp

    def make_choice(self, variants):
        return random.choice(variants)

    def random_dmg_and_arm(self, min_damage, max_damage, min_armor, max_armor):
        return random.randint(min_damage, max_damage), random.randint(min_armor, max_armor)

    def die(self):
        print(Fore.RED + f"{self} погиб!" + Fore.RESET)
        winner = "Монстр" if self == "Игрок" else "Игрок"
        print(Fore.YELLOW + f"{winner.upper()} ПОБЕДИЛЛ!!!" + Fore.RESET)