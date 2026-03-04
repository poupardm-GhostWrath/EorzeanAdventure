from enum import Enum
from world import World, Location
from item import Item, Item_Type, Item_Rarity

class PlayerRace(Enum):
    LALAFELL = "Lalafell"
    HYUR = "Hyur"
    AURA = "Au Ra"
    ELEZEN = "Elezen"
    MIQOTE = "Miqo'te"
    HROTHGAR = "Hrothgar"
    VIERA = "Viera"

class EnemyRace(Enum):
    BEAST = "Beast"
    UNDEAD = "Undead"
    FIEND = "Fiend"
    DRAGON = "Dragon"
    HUMANOID = "Humanoid"
    MACHINE = "Machine"
    PLANT = "Plant"

class Character:
    def __init__(self, name: str):
        self._name: str = name
        self._health: int = 100

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def take_damage(self, damage: int) -> int:
        self._health -= damage
        return self._health

class Player(Character):
    def __init__(self, name: str, race: PlayerRace, starting_town: str):
        super().__init__(name)
        self._race: PlayerRace = race
        self._level: int = 1
        self._exp: int = 0
        self._mana: int = 100
        self._weapon: Item = None
        self._location: str = starting_town
        self._inventory: list[Item] = []

    def __repr__(self):
        return f"Name: {self._name} Race: {self._race.value} Level: {self._level}"

    def get_race(self) -> PlayerRace:
        return self._race

    def get_level(self) -> int:
        return self._level
    
    def get_exp(self) -> int:
        return self._exp
    
    def get_mana(self) -> int:
        return self._mana

    def get_weapon(self) -> Item:
        return self._weapon

    def get_location(self) -> str:
        return self._location

    def get_inventory(self) -> list[Item]:
        return self._inventory

    def gain_exp(self, exp: int) -> None:
        print(f"{self._name} has gained {exp} exp.")
        self._exp += exp
        if self._exp >= 1000:
            self._level += self.level_up()
            print(f"Congratulation! {self._name} is now level {self._level}!")

    def level_up(self):
        if self._exp < 1000:
            return 0
        self._exp -= 1000
        self._health += 50 # Gain 50 health points
        self._mana += 50 # Gain 50 mana points
        return 1 + self.level_up()
        
    def move(self, world: World, direction: str) -> None:
        curr_location: Location = world.locations[self._location]
        if direction in curr_location["exits"]:
            loc = world.locations[curr_location["exits"][direction]]
            self._location = loc.name
            print(f"You head {direction}.\n")
        else:
            print("You can't go that way.\n")

    def look(self, world: World) -> None:
        curr_location: Location = world.get_locations()[self._location]
        print(curr_location.get_description())
        if len(curr_location.get_items()) > 0:
            print("You see:", "\n- ".join(curr_location.get_items()))
        print("Exits:", "\n-","\n- ".join(curr_location.get_exits().keys()))

    def add_to_inventory(self, item: Item) -> None:
        self._inventory.append(item)

    def remove_from_inventory(self, item: Item) -> None:
        self._inventory.remove(item)

    def unequip_weapon(self) -> None:
        if self._weapon is None:
            return
        self.add_to_inventory(self._weapon)
        self._weapon = None

    def equip_weapon(self, weapon: Item) -> None:
        if self._weapon is not None:
            self.add_to_inventory(self._weapon)
            self._weapon = None
        self._weapon = weapon
        self.remove_from_inventory(weapon)