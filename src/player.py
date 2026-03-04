from enum import Enum
from world import World, Location

class Race(Enum):
    LALAFELL = "Lalafell"
    HYUR = "Hyur"
    AURA = "Au Ra"
    ELEZEN = "Elezen"
    MIQOTE = "Miqo'te"
    HROTHGAR = "Hrothgar"
    VIERA = "Viera"

class Player:
    def __init__(self, name: str, race: Race, starting_town: str):
        self.name: str = name
        self.race: str = race
        self.level: int = 1
        self.exp: int = 0
        self.health: int = 100
        self.mana: int = 100
        self.location: str = starting_town
        self.inventory: list[str] = []

    def move(self, world: World, direction: str) -> None:
        curr_location: Location = world.locations[self.location]
        if direction in curr_location["exits"]:
            loc = world.locations[curr_location["exits"][direction]]
            self.location = loc.name
            print(f"You head {direction}.\n")
        else:
            print("You can't go that way.\n")

    def look(self, world: World) -> None:
        curr_location: Location = world.locations[self.location]
        print(curr_location.desc)
        if len(curr_location.items) > 0:
            print("You see:", "\n- ".join(curr_location.items))
        print("Exits:", "\n-","\n- ".join(curr_location.exits.keys()))
        