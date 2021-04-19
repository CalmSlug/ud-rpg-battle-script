import random
from classes.magic import Spell
from classes.inventory import Item
from classes.game import Person
from colorama import init, Fore


init()


# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print()
print(Fore.BLACK + "Black" + Fore.RESET)
print(Fore.RED + "Red" + Fore.RESET)
print(Fore.GREEN + "Green" + Fore.RESET)
print(Fore.YELLOW + "Yellow" + Fore.RESET)
print(Fore.BLUE + "Blue" + Fore.RESET)
print(Fore.MAGENTA + "Magenta" + Fore.RESET)
print(Fore.CYAN + "Cyan" + Fore.RESET)
print(Fore.WHITE + "White" + Fore.RESET)
print()

# Create Magic
fire = Spell("Fire", "black", 100, 10)
thunder = Spell("Thunder", "black", 100, 10)
blizzard = Spell("Blizzard", "black", 100, 10)
quake = Spell("Quake", "black", 150, 15)
meteor = Spell("Meteor", "black", 200, 20)
cure = Spell("Cure", "white", 100, 10)
cura = Spell("Cura", "white", 200, 20)
curaga = Spell("Curaga", "white", 300, 30)

# Create Items
potion = Item("Potion", "potion", 50, 10, "Heals for 50 HP")
hipotion = Item("Hi-Potion", "potion", 500, 10, "Heals for 500 HP")
elixer = Item("Elixer", "elixer", 9999, 5, "Fully restores your HP and MP")
hielixer = Item("Hi-Elixer", "elixer", 9999, 5, "Fully restores your party's HP and MP")
grenade = Item("Grenade", "attack", 500, 2, "Deals 500 damage")
nuke = Item("Nuke", "attack", 2000, 3, "Deals 2000 damage")

player_magic = [fire, thunder, blizzard, quake, meteor, cure, cura]
player_items = [potion, hipotion, elixer, hielixer, grenade, nuke]
enemy_magic = [fire, meteor, curaga]
enemy_items = [potion, elixer, grenade]

# Create People
player1 = Person("Valos", 1000, 120, 200, 50, player_magic, player_items)
player2 = Person("Malas", 1000, 120, 200, 50, player_magic, player_items)
player3 = Person("Rotas", 1000, 120, 200, 50, player_magic, player_items)
enemy1 = Person("Baddy", 1000, 120, 200, 50, enemy_magic, enemy_items)
enemy2 = Person("Maddy", 1000, 120, 200, 50, enemy_magic, enemy_items)
enemy3 = Person("Kaddy", 1000, 120, 200, 50, enemy_magic, enemy_items)

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

print("RPG Battle Script")
print()
print("AN ENEMY ATTACKS!")
print("Type 'exit' if you get bored!")
print()

while True:
    print("=== === === === === === === === === === === === === === === ===")
    for player in players:
        player.get_stats()
    print()

    for enemy in enemies:
        enemy.get_enemy_stats()
    print()
    
    for player in players:
        player.choose_action()
        choice = input("Choose action: ")

        if choice == "exit":
            print()
            print("Bye!")
            break

        elif choice == "1":
            print()
            player.choose_target(enemies)
            target_choice = int(input("Choose target: ")) - 1
            dmg = player.generate_damage()
            enemies[target_choice].reduce_hp(dmg)
            print()
            print(player.name, "deals", dmg, "points of damage to", enemies[target_choice].name + ".")
            print()

            if enemies[target_choice].get_hp() == 0:
                print(enemies[target_choice].name, "has died.")
                del enemies[target_choice]

        elif choice == "2":
            print()
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            if magic_choice == -1:
                print()
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print()
                print(Fore.RED + "Not enough MP!" + Fore.RESET)
                print()
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "black":
                print()
                player.choose_target(enemies)
                target_choice = int(input("Choose target: ")) - 1
                enemies[target_choice].reduce_hp(magic_dmg)
                print()
                print(Fore.BLUE + spell.name, "deals", str(magic_dmg), "points of damage to", enemies[target_choice].name + "." + Fore.RESET)
                print()

                if enemies[target_choice].get_hp() == 0:
                    print(enemies[target_choice].name, "has died.")
                    del enemies[target_choice]

            elif spell.type == "white":
                player.restore_hp(magic_dmg)
                print()
                print(Fore.BLUE + spell.name, "heals for", str(magic_dmg), "HP." + Fore.RESET)
                print()

        elif choice == "3":
            print()
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                print()
                continue

            item = player.items[item_choice]

            if item.amount == 0:
                print()
                print(Fore.RED + "None left..." + Fore.RESET)
                print()
                continue

            item.remove(1)

            if item.type == "potion":
                player.restore_hp(item.dmg)
                print()
                print(Fore.GREEN + item.name, "heals for", str(item.dmg), "HP." + Fore.RESET)
                print()
            
            elif item.type == "elixer":

                if item.name == "Hi-Elixer":
                    for player in players:
                        player.hp = player.maxhp
                        player.mp = player.maxmp

                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp

                print()
                print(Fore.GREEN + item.name, "fully restores you!" + Fore.RESET)
                print()
            
            elif item.type == "attack":
                print()
                player.choose_target(enemies)
                target_choice = int(input("Choose target: ")) - 1
                enemies[target_choice].reduce_hp(item.dmg)
                print()
                print(Fore.GREEN + item.name, "deals", item.dmg, "points of damage to" + enemies[target_choice].name + "." + Fore.RESET)
                print()

                if enemies[target_choice].get_hp() == 0:
                    print(enemies[target_choice].name, "has died.")
                    del enemies[target_choice]

        else:
            print()
            print(Fore.RED + "Invalid command!!!" + Fore.RESET)
            print()
            continue

    defeated_enemies = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1    
    if defeated_enemies == 2:
        print(Fore.GREEN + "You win!" + Fore.RESET)
        break    

    for enemy in enemies:
        enemy_choice = random.choice([0, 1])
        
        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            enemy_target = random.choice(players)
            enemy_target.reduce_hp(enemy_dmg)
            print(enemy.name.replace(" ", ""), " deals", enemy_dmg, 
                  "points of damage to", enemy_target.name.replace(" ", "") + ".")

        if enemy_choice == 1:
            enemy_spell = random.choice(enemy.magic)
            magic_dmg = enemy_spell.generate_spell_damage()
            current_mp = enemy.get_mp()

            if enemy_spell.cost > current_mp:
                print()
                print(Fore.RED + enemy.name + ": Huh?! Not enough MP?!" + Fore.RESET)
                print()
            
            else:
                enemy.reduce_mp(enemy_spell.cost)

                if enemy_spell.type == "black":
                    enemy_target = random.choice(players)
                    enemy_target.reduce_hp(magic_dmg)
                    print(Fore.BLUE + enemy_spell.name, "by", enemy.name.replace(" ", ""), 
                          "deals", magic_dmg, "points of damage to", 
                          enemy_target.name.replace(" ", "") + "." + Fore.RESET)

                elif enemy_spell.type == "white" and enemy.get_hp() < 500:
                    enemy.restore_hp(magic_dmg)
                    print(Fore.BLUE + enemy_spell.name, "heals", magic_dmg, 
                          "HP to", enemy.name.replace(" ", "") + "." + Fore.RESET)
                
                else:
                    enemy.restore_mp(enemy_spell.cost)
                    print(Fore.BLUE + enemy.name + ": Heal? Nah!" + Fore.RESET)

    defeated_players = 0
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    if defeated_players == 3:
        print(Fore.RED + "Your enemy has defeated you!" + Fore.RESET)
        break
