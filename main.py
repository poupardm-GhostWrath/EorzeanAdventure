import sys
import os
module_dir = os.path.normpath('src')
sys.path.append(module_dir)

from character import Player, PlayerRace, create_player
from world import World, Location
from item import Item_Rarity, Item_Type, Consumable, Weapon

def parse_command(world: World, player: Player, cmd: str) -> None:
    parts = cmd.lower().strip().split()
    if not parts:
        return

    verb = parts[0]

    if verb in ("exit", "quit"):
        print("Thank you for playing. See you next time.")
        sys.exit()
    elif verb == "help":
        print("=== HELP MENU ===")
        help_menu: str = """
+-------------+-------------------+
| Action      | Command           |
+-------------+-------------------+
| Exit        | exit              |
|             | quit              |
+-------------+-------------------+
| Help        | help              |
+-------------+-------------------+
| Move        | move <direction>  |
|             | go <direction>    |
+-------------+-------------------+
| Look        | look              |
+-------------+-------------------+
| Inventory   | inventory         |
|             | inv               |
+-------------+-------------------+
| Take        | take              |
+-------------+-------------------+
"""
        print(help_menu)
    elif verb in ("go", "move"):
        if len(parts) < 2:
            print("Go where?\n")
        else:
            player.move(world, parts[1])
    elif verb == "look":
        player.look(world)
    elif verb == "take":
        if len(parts) < 2:
            print("Take what?\n")
        else:
            # player.take(parts[1])
            pass
    elif verb in ("inventory", "inv"):
        player.show_inventory()
    else:
        print("I don't understand that command.\n")
    
def main():
    # Creating world
    world: World = World()
    world.create_world()

    # Creating player
    player = create_player()

    # Intro
    print(f"\n=== Welcome to Eorzea {player.get_name()}! ===\n")
    print("Notice: Type 'exit' to end game.")
    print("Notice: Type 'help' for help info.")
    player.look(world)

    # Start Game Loop
    while True:
        cmd = input("> ")
        parse_command(world, player, cmd)




    


if __name__ == "__main__":
    main()
