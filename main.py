import sys
import os
module_dir = os.path.normpath('src')
sys.path.append(module_dir)

from player import Player, Race
from world import World, Location
from init import create_world

def main():
    world: World = create_world()
    player: Player = Player("Ghost", Race.LALAFELL, "Ul'dah")
    print(f"=== Welcome to Eorzea {player.name}! ===")
    player.look(world)
    


if __name__ == "__main__":
    main()
