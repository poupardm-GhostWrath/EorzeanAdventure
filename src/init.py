import json
from world import World, Location

def create_world() -> World:

    # Open 'world.json' file and read the content
    try:
        with open('data/world.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: The 'world.json' file was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
    
    tmp_world: World = World()
    # Go through the data to populate world
    for location in data:
        tmp_location: Location = Location(location, 
                                        data[location]["desc"], 
                                        data[location]["exits"],
                                        data[location]["items"],
                                        data[location]["crystal"],
                                        data[location]["enemies"])
        tmp_world.add_location(tmp_location)
    return tmp_world