import sys
import os
module_dir = os.path.normpath('src')
sys.path.append(module_dir)

from character import Player, PlayerRace
from world import World, Location
from init import create_world
from item import Item, Item_Rarity, Item_Type

def main():
    world: World = create_world()
    player: Player = Player("Ghost", PlayerRace.LALAFELL, "Ul'dah")
    print(player)
    print(f"=== Welcome to Eorzea {player.get_name()}! ===")



    


if __name__ == "__main__":
    main()
