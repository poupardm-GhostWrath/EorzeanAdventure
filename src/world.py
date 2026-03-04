class World():
    def __init__(self):
        self.name: str = "Eorzea"
        self.locations: dict[str, Location] = {}

    def add_location(self, location: Location) -> None:
        self.locations[location.name] = location

class Location():
    def __init__(self, 
                name: str, 
                desc: str, 
                exits: dict, 
                items: list[str], 
                crystal: bool, 
                enemies: list[str]):
        self.name: str = name
        self.desc: str = desc
        self.exits: dict[str, str] = exits
        self.items: list[str] = []
        self.crystal: bool = crystal
        self.enemies: list[str]
