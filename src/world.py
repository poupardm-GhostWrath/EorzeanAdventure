import json
from item import Item

class World():
    def __init__(self):
        self._name: str = "Eorzea"
        self._locations: dict[str, Location] = {}

    def get_name(self) -> str:
        return self._name
    
    def get_locations(self) -> dict:
        return self._locations

    def add_location(self, location: Location) -> None:
        self._locations[location.get_name()] = location

    def __repr__(self):
        return f"World name: {self._name} # of Locations: {len(self._locations)}"

    def create_world(self) -> None:
        # Open 'world.json' file and read the content
        try:
            with open('data/world.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Error: The 'world.json' file was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
        
        # Go through the data to populate world
        for location in data:
            tmp_location: Location = Location(location, 
                                            data[location]["desc"], 
                                            data[location]["exits"],
                                            data[location]["items"],
                                            data[location]["crystal"],
                                            data[location]["enemies"])
            self.add_location(tmp_location)

class Location():
    def __init__(self, 
                name: str, 
                desc: str, 
                exits: dict, 
                items: list[Item], 
                crystal: bool, 
                enemies: list[str]):
        self._name: str = name
        self._desc: str = desc
        self._exits: dict[str, str] = exits
        self._items: list[Item] = items
        self._crystal: bool = crystal
        self._enemies = enemies

    def __repr__(self):
        return f"Location name: {self._name}\nDescription: {self._desc}\nExits: {self._exits}\nItems: {self._items}\nCrystal: {self._crystal}\nEnemies: {self._enemies}"

    def get_name(self) -> str:
        return self._name
    
    def get_description(self) -> str:
        return self._desc

    def get_exits(self) -> dict:
        return self._exits

    def get_items(self) -> list[Item]:
        return self._items
    
    def get_crystal(self) -> bool:
        return self._crystal

    def get_enemies(self) -> list[Enemy]:
        return self._enemies

    def add_item(self, item: Item) -> None:
        self._items.append(item)

    def remove_item(self, item: str) -> Item:
        for i in range(len(self._items)):
            if self._items[i].get_name == item:
                return self._items.pop(i)
        return None

    def add_enemy(self, enemy) -> None:
        self._enemies.append(enemy)

    def remove_enemy(self, enemy: str) -> None:
        for i in range(len(self._enemies)):
            if self._enemies[i].get_name() == enemy:
                tmp: Enemy = self._enemies.pop(i)
