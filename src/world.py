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
        return f"World name: {self.name} # of Locations: {len(self.locations)}"

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
        self._enemies: list[str] = enemies

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

    def get_enemies(self) -> list[str]:
        return self._enemies

    def add_item(self, item: Item) -> None:
        self._items.append(item)
        print(f"{item.get_name} was dropped on the floor")

    def remove_item(self, item: str) -> Item:
        for i in range(len(self._items)):
            if self._items[i].get_name == item:
                return self._items.pop(i)
        return None

    
