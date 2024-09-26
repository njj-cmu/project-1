from typing import List
from typing import Callable

MENUS = {
    "main": {
        0: "MAIN MENU",
        1: "Music Library",
        2: "Play",
        3: "Search",
        4: "Artists",
        5: "Exit"
    } ,
    "library": {
        0: "MUSIC LIBRARY",
        1: "Show All Music",
        2: "Select Album",
        3: "Select Artist",
        4: "Tracks",
        5: "Go Back"
    }, 
    "tracks": {

    }
}

def showMenu(key: str, inline: int = 1):
    """
        Shows the menu of a selected menu key.

        :param key: Key of the menu to be shown. Must exist in the MENUS dictionary.
        :param inline: Determines how many options should be printed on the same line. Defaults to 1, meaning
            only 1 option will be printed per line.
    """
    assert insideCollection(key, MENUS.keys()), "Menu key not found."
    assert inline > 0, "Invalid inline value. It must be greater than 1."

    i = 0

    print(f"<---- {MENUS[key][0]} ---->")

    for option in MENUS[key]:
        
        # Skip first option
        if option == 0:
            continue

        out = "[{}]".format(option)
        if i == inline and i != 1:
            out = "\n[{}]".format(option)
        
        print("{} {}".format(out, MENUS[key][option]), end = "\t" if inline > 1 else "\n")
        
        i = 1 if i == inline else (i + 1)

def prompt(phrase: str, rules: List[Callable] = None, typecast: Callable = str) -> any:
    """
    Prompts the user for some input. 
    :param phrase: Prompt to the user.
    :param rules: Limitations of the input from the user.
    :
    """
    
    while True:
        input = typecast(phrase + ": ")

        for rule in rules:
            # Check if rule evaluates properly for the input.
            if not rule(input):
                raise ValueError("Incorrect value given", name = "input")
            

def withinNumericRange(input: int | float, low: int | float, high: int | float) -> bool:
    """
        Checks if a numeric value is within the specified range.

        :param input: Input to be checked.
        :param low: Lower bound range.
        :param high: Upper bound range.

        :return: True if number is within range. False otherwise.
    """
    return low <= input <= high

def insideCollection(input: any, collection: list | tuple | set | dict ) -> bool:
    """
        Checks if value is located inside a collection of objects. 

        :param input: Value to be checked inside collection.
        :param collection: Collection of values. Does not work with array list.
        :return: True if value is located inside a collection of values. False otherwise.
    """
    assert isinstance(collection, (list, tuple, set, dict, type({}.keys()), type({}.values()) )), "Invalid collection type given."
    try:
        # if isinstance(collection, (list, tuple)):
        #     return collection.index(input) != -1
        # elif isinstance(collection, set):
        #     s = set(input)

        #     # If the length of intersection is equal to 0, that means that the input value is not
        #     # present on the set
        #     return len(s.intersection(collection)) > 0
        # elif isinstance(collection, dict):
        #     # In dictionary, there are two ways a value could be present.
        #     # Either it exists as a key, or it exists as a value.
        #     res = input in collection.keys()
            
        #     # If it doesn't exist as a key
        #     if not res:
        #         res = input in collection.values()
            
        #     # Check if it exists as a key or a value...
        #     if res:
        #         return True
        # elif isinstance(type({}.keys))
        return input in collection
    except:
        return False
    

print("main" in MENUS.keys())
showMenu("main")