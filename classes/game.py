import random
from colorama.ansi import Fore


class Person:
    def __init__(self, name, hp, mp, atk, armor, magic, items):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.maxhp = hp
        self.maxmp = mp
        self.atk = atk
        self.armor = armor
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        atkl = self.atk - 25
        atkh = self.atk + 25
        return random.randrange(atkl, atkh)

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def reduce_hp(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def reduce_mp(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0

    def restore_hp(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def restore_mp(self, cost):
        self.mp += cost
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def choose_action(self):
        i = 1
        print(self.name)
        print("ACTIONS")
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("TARGET")
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ":", enemy.name)
                i += 1

    def choose_magic(self):
        i = 1
        print(Fore.BLUE + "MAGIC" + Fore.RESET)
        print("    0: Go back")
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print(Fore.GREEN + "ITEMS" + Fore.RESET)
        print("    0: Go back")
        for item in self.items:
            print("    " + str(i) + ":", item.name, "x" + str(item.amount), "(" + str(item.desc) + ")")
            i += 1

    def get_stats(self):
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        while len(hp_string) < 9:
            hp_string = " " + hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        while len(mp_string) < 7:
            mp_string = " " + mp_string

        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 20
        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1
        while len(hp_bar) < 20:
            hp_bar += " "

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 10
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        print("            HP     ____________________       MP    __________")
        print(self.name + "   " + 
              hp_string + " |" + Fore.RED + hp_bar + Fore.RESET + "|   " + 
              mp_string + " |" + Fore.BLUE + mp_bar + Fore.RESET + "|")
        
    def get_enemy_stats(self):
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        while len(hp_string) < 9:
            hp_string = " " + hp_string

        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 40
        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1
        while len(hp_bar) < 40:
            hp_bar += " "

        print("            HP     ________________________________________")
        print(self.name + "   " + 
              hp_string + " |" + Fore.RED + hp_bar + Fore.RESET + "|")
