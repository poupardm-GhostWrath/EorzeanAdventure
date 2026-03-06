import sys
import os
module_dir = os.path.normpath('src')
sys.path.append(module_dir)

from character import Player, PlayerRace
from world import World, Location
from item import Item_Rarity, Item_Type, Consumable, Weapon

def main():
    world: World = World()
    world.create_world()
    print(f"Please enter your player name...")
    cmd = input("Player Name > ")
    tmp_player = [cmd]
    print(f"Please choose your Race...")
    tmp_race = [member.value for member in PlayerRace]
    for i in range(len(tmp_race)):
        print(f"{i + 1}: {tmp_race[i]}")
    right_option = False
    while not right_option:
        cmd = input("Race > ")
        right_option = True
        match (cmd):
            case "1":
                tmp_player.append(PlayerRace.LALAFELL)
                break
            case "2":
                tmp_player.append(PlayerRace.HYUR)
                break
            case "3":
                tmp_player.append(PlayerRace.AURA)
                break
            case "4":
                tmp_player.append(PlayerRace.ELEZEN)
                break
            case "5":
                tmp_player.append(PlayerRace.MIQOTE)
                break
            case "6":
                tmp_player.append(PlayerRace.HROTHGAR)
                break
            case "7":
                tmp_player.append(PlayerRace.VIERA)
                break
            case _:
                print("Invalid Option. Try Again...")
                right_option = False

    print(f"Please choose your starting location...")
    print(f"1. Ul'dah\n2. Gridania\n3. Limsa Lominsa")
    right_option = False
    while not right_option:
        cmd = input("Starting Location > ")
        right_option = True
        match (cmd):
            case "1":
                tmp_player.append("Ul'dah")
                break
            case "2":
                tmp_player.append("Gridania")
                break
            case "3":
                tmp_player.append("Limsa Lominsa")
                break
            case _:
                print("Invalid Option. Try Again...")
                right_option = False

    player = Player(tmp_player[0], tmp_player[1], tmp_player[2])
    print(f"\n=== Welcome to Eorzea {player.get_name()}! ===\n")
    player.look(world)





    


if __name__ == "__main__":
    main()
