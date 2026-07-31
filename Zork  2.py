import time
import random
import sys

def Zork_2():
    start_time = time.time()
    MAX_WEIGHT = 20 
    row = 5 #5
    col = 0 #0
    PlayerPos = [row, col]
    PlayerInventory = []
    PlayerHealth = 100
    lost = 0
    stepCount = 0 
    prisoner_dialogue_done = False
    prisoner_dialogue_done2 = False
    VisitedRooms = set()
    william_multi = 1
    william_weapon = None
    
    Maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],#0     #4 entrances to the maze
        [1, 0, 0, 0, 1, 1, 1, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],#1     #0 - Corridor
        [1, 9, 1, 0, 0, 0, 1, 3, 3, 1, 0, 1, 1, 0, 1, 1, 0, 1, 5, 1],#2     #1 - Wall 
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 3, 1, 3, 3, 1, 1, 0, 0, 0, 1],#3     #3 - Room
        [1, 0, 0, 3, 1, 0, 1, 0, 0, 1, 1, 1, 3, 3, 1, 1, 0, 1, 1, 1],#4     #9 - Door
        [0, 0, 1, 1, 1, 0, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],#5     #5 - Enemy
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 9, 1, 0, 1],#6     #6 - Final destination / exit
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],#7     #7 - Shopkeeper (twins)
        [1, 5, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],#8     #8 - Riddler
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 3, 5, 9, 0, 1, 3, 3, 1, 0, 0, 0],#9
        [1, 8, 1, 1, 0, 1, 1, 0, 1, 6, 3, 1, 1, 1, 3, 3, 1, 0, 1, 1],#10
        [1, 0, 1, 1, 0, 1, 3, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],#11
        [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],#12
        [1, 1, 0, 1, 5, 1, 1, 1, 0, 0, 5, 0, 0, 1, 1, 1, 0, 1, 0, 1],#13
        [1, 7, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],#14
        [1, 1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],#15
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],#16
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 9, 1, 3, 1, 3, 1],#17
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1, 1],#18
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] #19
    ] #  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19

    RoomDescriptions = {
        #Entrances
        (0, 10): "You are at the north entrance of the maze, there is a wall to the west and east of you with a path going south",
        (19, 4): "You are at the south entrance of the maze, there is a wall to the west and east of you with a path going north",
        (9, 19): "You are at the east entrance of the maze, there is a wall to the north and south of you with a path going west",
        (5, 0): "You are at the west entrance of the maze, there is a wall to the north and south of you with a path going east",

        (1, 1): "There is a wall to the north and west of you with a path going east and you see a door to your south",
        (1, 2): "There is a wall to the north and south of you with a path going east and west",
        (1, 3): "There is a wall to the north and east of you with a path going south and west",
        (1, 7): "There is a wall to the north and west of you with a path going south and east",
        (1, 8): "There is a wall to the north and east of you with a path going south and west",
        (1, 10): "There is s wall to your west but a long corridor to your east and you glimpse a candle light to your south and the exit of the maze to your north",
        (1, 11): "There is a wall to the north and south of you with a path going east and west",
        (1, 12): "There is a wall to the north and south of you with a path going east and west",
        (1, 13): "There is a wall to the north of you with a path going east, and west and you can see a room to your south",
        (1, 14): "There is a wall to the north and south of you with a path going east and west",
        (1, 15): "There is a wall to the north and south of you with a path going east and west",
        (1, 16): "There is a wall to the north and east of you with a long corridor going west and a path going south",
        (1, 18): "You are at a dead end with a path only going south",
        (2, 1): "There is a wall to the west and east of you with a path going north and south",
        (2, 3): "There is a wall to the south and west of you with a path going north and east",
        (2, 4): "There is a wall to the north and south of you with a path going east and west",
        (2, 5): "There is a wall to the north and east of you with a path going west and you can see a never ending corridor going south",
        (2, 6): "There is a wall to the north and south of you with a path going east and west",
        (2, 7): "There is a wall to the south of you with a path going north, east, and west",
        (2, 8): "There is a wall to the east of you with a path going north, south, and west",
        (2, 10): "There is a wall to the west and east of you with a path going north and south",
        (2, 13): "There is a wall to the west and east of you with a path going north and south",
        (2, 16): "There is a wall to the west and east of you with a path going north and south",
        (2, 18): "There is a wall to the west and east of you covered in the rats blood with a path going north and south",
        (3, 1): "There is a wall to the west and east of you with a path going south and a you see a door to you north",
        (3, 5): "There is a wall to the west and east of you with a path going north and south",
        (3, 8): "There is a wall to the west and east of you with a path going north and south",
        (3, 10): "There is a wall to the south, west, and east of you with a path going north",
        (3, 12): "There is a wall to the north and west of you with a path going south and east",
        (3, 13): "There is a wall to the east of you with a path going north, south, and west",
        (3, 16): "There is a wall to the west of you with a path going north, south, and east",
        (3, 17): "There is a wall to the north and south of you with a path going east and west",
        (3, 18): "There is a wall to the south and east of you with a path west and you can see a rat to your north",
        (4, 1): "There is a wall to the west of you with a path going north, south, and east",
        (4, 2): "There is a wall to the north and south of you with a path going east and west",
        (4, 3): "You are in a dark room with a table in the far corner with wall all around you apart from a path going west",
        (4, 5): "There is a wall to the west and east of you with a path going north and south",
        (4, 7): "There is a wall to the north and west of you with a path going south and east",
        (4, 8): "There is a wall to the south and east of you with a path going north and west",
        (4, 12): "There is a wall to the west of you with a path going north, south, and east",
        (4, 13): "There is a wall to the south and east of you with a path going north and west",
        (4, 16): "There is a wall to the west and east of you with a path going north and south",
        (5, 1): "There is a wall to the south and east of you with a path going north and west",
        (5, 5): "There is a wall to the west and east of you with a path going north and south",
        (5, 7): "There is a wall to the west and east of you with a path going north and south",
        (5, 12): "There is a wall to the west and east of you with a path going north and south",
        (5, 16): "There is a wall to the west of you with a path going north and east while being met with a door to you north",
        (5, 17): "There is a wall to the north and south of you with a path going east and west",
        (5, 18): "There is a wall to the north and east of you with a path going south and west",
        (6, 3): "There is a wall to the north, west, and east of you with a path going south",
        (6, 5): "There is a wall to the west and east of you with a path going north and south",
        (6, 7): "There is a wall to the west and east of you with a path going north and south",
        (6, 10): "There is a wall to the north and west of you with a path going south and east",
        (6, 11): "There is a wall to the north and south of you with a path going east and west",
        (6, 13): "There is a wall to the north and south of you with a path going east and west",
        (6, 14): "There is a wall to the north and east of you with a path going south and west",
        (6, 16): "There is a wall to the west and east of you with a path going north and south",
        (6, 18): "There is a wall to the west and east of you with a path going north and south",
        (7, 1): "There is a wall to the north and west of you with a path going south and east",
        (7, 2): "There is a wall to the north and south of you with a path going east and west",
        (7, 3): "There is a wall to the south and east of you with a path going north and west",
        (7, 5): "There is a wall to the west of you with a path going north, south, and east",
        (7, 6): "There is a wall to the north and south of you with a path going east and west",
        (7, 7): "You are at an intersection with paths going in all 4 directions, choose wisely",
        (7, 8): "There is a wall to the north and south of you with a path going east and west",
        (7, 9): "There is a wall to the north and south of you with a path going east and west",
        (7, 10): "There is a wall to the south and east of you with a path going north and west",
        (7, 12): "There is a wall to the west and east of you with a path going north and south",
        (7, 14): "There is a wall to the south and west of you with a path going north and east",
        (7, 15): "There is a wall to the north and south of you with a path going east and west",
        (7, 16): "There is a wall to the south and east of you with a path west and you are met with a door to your north",
        (7, 18): "There is a wall to the south, west, and east of you with a path going north",
        (8, 1): "There is a wall to the west and east of you with a path going north and south",
        (8, 5): "There is a wall to the west and east of you with a path going north and south",
        (8, 7): "There is a wall to the west and east of you with a path going north and south",
        (8, 12): "There is a wall to the west and east of you with a path going north and south",
        (9, 1): "There is a wall to the west and east of you with a path going north and south",
        (9, 3): "There is a wall to the north, south, and west of you with a path going east",
        (9, 4): "There is a wall to the north of you with a path going south, east, and west",
        (9, 5): "There is a wall to the east of you with a path going north, south, and west",
        (9, 7): "There is a wall to the west and east of you with a path going north and south",
        (9, 9): "There is a wall to the north and west of you with a path going south and east",
        (9, 10): "There is a wall to the north of you with a path going south, east, and west",
        (9, 11): "There is a wall to the north and south of you with a path going east and west",
        (9, 12): "There is a wall to the south and east of you with a path going north and west",
        (9, 14): "There is a wall to the north and west of you with a path going south and east",
        (9, 15): "There is a wall to the north and east of you with a path going south and west",
        (9, 17): "There is a wall to the north and west of you with a path going south and east",
        (9, 18): "There is a wall to the north and south of you with a path going east and west",
        (10, 1): "There is a wall to the west and east of you with a path going north and south",
        (10, 4): "There is a wall to the west of you with a path going north, south, and east",
        (10, 6): "There is a wall to the north of you with a path going south, east, and west",
        (10, 7): "There is a wall to the east of you with a path going north, south, and west",
        (10, 9): "You are at the very centre of the maze and you see a ladder leading to the surface",
        (10, 10): "There is a wall to the south and east of you with a path going north and west",
        (10, 14): "There is a wall to the west of you with a path going north, south, and east",
        (10, 15): "There is a wall to the south of you with a path going north, east, and west",
        (10, 16): "There is a wall to the north and south of you with a path going east and west",
        (10, 17): "There is a wall to the east of you with a path going north, south, and west",
        (11, 1): "There is a wall to the west and east of you with a path going south and mysterous man to your south.",
        (11, 4): "There is a wall to the west of you with a path going north, south, and east",
        (11, 5): "There is a wall to the south of you with a path going north, east, and west",
        (11, 6): "There is a wall to the south of you with a path going north, east, and west",
        (11, 7): "There is a wall to the east of you with a path going north, south, and west",
        (11, 14): "There is a wall to the west and east of you with a path going north and south",
        (11, 17): "There is a wall to the west and east of you with a path going north and south",
        (12, 1): "There is a wall to the south and west of you with a path going north and east",
        (12, 2): "There is a wall to the north and east of you with a path going south and west",
        (12, 4): "There is a wall to the west and east of you with a path going north and south",
        (12, 7): "There is a wall to the south and west of you with a path going north and east",
        (12, 8): "There is a wall to the north and east of you with a path going south and west",
        (12, 12): "There is a wall to the north and west of you with a path going south and east",
        (12, 13): "There is a wall to the north and south of you with a path going east and west",
        (12, 14): "There is a wall to the south and east of you with a path going north and west",
        (12, 16): "There is a wall to the north and west of you with a path going south and east",
        (12, 17): "There is a wall to the south of you with a path going north, east, and west",
        (12, 18): "There is a wall to the north and east of you with a path going south and west",
        (13, 2): "There is a wall to the west and east of you with a path going north and south",
        (13, 4): "There is a wall to the west and east of you with a path going north and south",
        (13, 8): "There is a wall to the south and west of you with a path going north and east",
        (13, 9): "There is a wall to the north and south of you with a path going east and west",
        (13, 10): "There is a wall to the north and south of you with a path going east and west",
        (13, 11): "There is a wall to the north and south of you with a path going east and west",
        (13, 12): "There is a wall to the south and east of you with a path going north and west",
        (13, 16): "There is a wall to the west and east of you with a path going north and south",
        (13, 18): "There is a wall to the west and east of you with a path going north and south",
        (14, 1): "There is a wall to the north, south, and west of you with a path going east",
        (14, 2): "There is a wall to the east of you with a path going north and south. You can see a cheerful merchant to your west.",
        (14, 4): "There is a wall to the west and east of you with a path going north and south",
        (14, 14): "There is a wall to the north, south, and west of you with a path going east",
        (14, 15): "There is a wall to the north and south of you with a path going east and west",
        (14, 16): "There is a wall to the south and east of you with a path going north and west",
        (14, 18): "There is a wall to the west and east of you with a path going north and south",
        (15, 2): "There is a wall to the west and east of you with a path going north and south",
        (15, 4): "There is a wall to the west and east of you with a path going north and south",
        (15, 6): "There is a wall to the north, west, and east of you with a path going south",
        (15, 8): "There is a wall to the north, west, and east of you with a path going south",
        (15, 10): "There is a wall to the north, south, and west of you with a path going east",
        (15, 11): "There is a wall to the north and south of you with a path going east and west",
        (15, 12): "There is a wall to the north and east of you with a path going south and west",
        (15, 18): "There is a wall to the west and east of you with a path going north and south",
        (16, 1): "There is a wall to the north and west of you with a path going south and east",
        (16, 2): "There is a wall to the south and east of you with a path going north and west",
        (16, 4): "There is a wall to the west of you with a path going north, south, and east",
        (16, 5): "There is a wall to the north and south of you with a path going east and west",
        (16, 6): "There is a wall to the east of you with a path going north, south, and west",
        (16, 8): "There is a wall to the west and east of you with a path going north and south",
        (16, 12): "There is a wall to the west of you with a path going north, south, and east",
        (16, 13): "There is a wall to the north and south of you with a path going east and west",
        (16, 14): "There is a wall to the north of you with a path going east, and west. You can see an old imprisoned man to your south.",
        (16, 15): "There is a wall to the north and south of you with a path going east and west",
        (16, 16): "There is a wall to the north of you with a path going south, east, and west",
        (16, 17): "There is a wall to the north and south of you with a path going east and west",
        (16, 18): "There is a wall to the east of you with a path going north, south, and west",
        (17, 1): "There is a wall to the west and east of you with a path going north and south",
        (17, 4): "There is a wall to the west and east of you with a path going north and south",
        (17, 6): "There is a wall to the west and east of you with a path going north and south",
        (17, 8): "There is a wall to the west and east of you with a path going north and south",
        (17, 11): "There is a wall to the north and west of you with a path going south and east",
        (17, 12): "There is a wall to the south and east of you with a path going north and west",
        (17, 14): "There is a wall to the west and east of you with a path going north and south",
        (17, 16): "There is a wall to the south, west, and east of you with a path going north",
        (17, 18): "There is a wall to the south, west, and east of you with a path going north",
        (18, 1): "There is a wall to the south and west of you with a path going north and east",
        (18, 2): "There is a wall to the north and south of you with a path going east and west",
        (18, 3): "There is a wall to the north and south of you with a path going east and west",
        (18, 4): "There is a wall to the east of you with a path going north, south, and west",
        (18, 6): "There is a wall to the south, west, and east of you with a path going north",
        (18, 8): "There is a wall to the south and west of you with a path going north and east",
        (18, 9): "There is a wall to the north and south of you with a path going east and west",
        (18, 10): "There is a wall to the north and south of you with a path going east and west",
        (18, 11): "There is a wall to the south and east of you with a path going north and west",
        (18, 14): "There is a wall to the south, west, and east of you with a path going north",
    }

    RoomItems = {
        (17, 4): ["rock"],
        (1, 14): ["rock"],
        (4, 5): ["rock"], 
        (4, 1): ["bread"], #bread lol
        (14, 14): ["bread"],
        (11, 6): ["bread"],
        (17, 1): ["coin"],
        (3, 10): ["coin"],
        (18, 6): ["gruel"],
        (3, 12): ["gruel"],
        (10, 15): ["gruel"],
        (1, 18): ["cheese"],
        (1, 8): ["bread","cheese"],
        (9, 14): ["bread","bandage"],

        (5, 0): ["letter"],  # West entrance
        (15, 10): ["note"], #note that says time 
        (17, 18): ["torn journal"],
        
        (3, 1): ["sign"],
        (9, 12): ["final sign"],
        (2, 1): ["danger sign"],
        (18, 4): ["crossroad sign"],
        (12, 17): ["prison sign"],
        #keys
        (4, 3): ["brass key"],   # top left door door_1 
        (6, 3): ["gold key","bandage"],   # for the final boss door_2
        (7, 18): ["copper key"],   # to open the door that splits the paths door_3
        (15, 8): ["iron key","coin"],   # To let the man escape door_4
    }

    Traps = {
        (11, 3): {
            "name": "dart",
            "damage": 5,
            "description": "A dart shoots from the wall! ",
            "one_time": True,
            "triggered": False
        },
        (3, 15): {
            "name": "pit trap",
            "damage": 25,
            "description": "The floor gives way beneath you and you fall into a pit",
            "one_time": True,
            "triggered": False
        },
        (16, 10): {
            "name": "spike trap",
            "damage": 30,
            "description": "Sharp spikes spring up from the floor",
            "one_time": True,
            "triggered": False
        },
        (1, 2): {
            "name": "bear trap",
            "damage": 0,
            "description": "You stepped on a bear trap but it was old and rusty so you managed to lift your leg out of harms way",
            "one_time": True, 
            "triggered": False
        },
        (17, 6): {
            "name": "pebble launcher",
            "damage": 3,
            "description": "Some fool thought it was a great idea to launch pebbles at passers by",
            "one_time": True, 
            "triggered": False
        }
    }

    def check_for_trap(row, col):
        nonlocal PlayerHealth
        
        pos = (row, col)
        
        if pos in Traps:
            trap = Traps[pos]
            
            if trap.get("one_time") and trap.get("triggered"):
                return False
            
            trap["triggered"] = True
            PlayerHealth -= trap["damage"]
            
            print(f"\n{trap['description']}")
            print(f"You took {trap['damage']} damage")
            print(f"Health remaining: {PlayerHealth} health")
            
            if PlayerHealth <= 0:
                print("\nThe trap was fatal...")
                PlayerHealth = 0
            
            return True
        
        return False

    shop = {
        (14, 1): { 
            "name": "Merchant",
            "greeting": "Ah, a customer! Welcome to trade?",
            "inventory": {
                "gruel": 1,
                "cheese": 2,
                "bread": 3,
                "bandage": 5,
            },
            "buy_prices": {
                "gruel": 1,
                "cheese": 2,
                "bread": 3,
                "bandage": 5,
            }
        }
    }

    def typewriter(text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char in ":!":
                time.sleep(2)
            else:
                time.sleep(delay)
        print()

    def get_adjacent_shops(row, col):
        shops_found = []
        if (row, col) in shop:
            shops_found.append(("next", row, col))
        if row > 0 and (row-1, col) in shop:
            shops_found.append(("north", row-1, col))
        if row < len(Maze)-1 and (row+1, col) in shop:
            shops_found.append(("south", row+1, col))
        if col < len(Maze[0])-1 and (row, col+1) in shop:
            shops_found.append(("east", row, col+1))
        if col > 0 and (row, col-1) in shop:
            shops_found.append(("west", row, col-1))
        return shops_found

    def handle_shop_interaction(shop, shop_row, shop_col):
        nonlocal PlayerHealth
        
        print(f"\n{shop['name']}: \"{shop['greeting']}\"")
        
        while True:
            print(f"\n{'='*50}")
            print(f"Your coins: {PlayerInventory.count('coin')}")
            print(f"Your health: {PlayerHealth}")
            print(f"\n1. Buy items")
            print(f"2. Sell items")
            print(f"3. Leave shop")
            
            choice = input("\nWhat would you like to do? ").lower().strip()
            
            if choice in ["1", "buy"]:
                handle_buying(shop)
            elif choice in ["2", "sell"]:
                handle_selling(shop)
            elif choice in ["3", "leave", "exit"]:
                print(f"\n{shop['name']}: \"Safe travels!\"")
                break
            else:
                print("Invalid choice!")

    def handle_buying(shop):

        print(f"\n--- Items for Sale ---")

        #dont ask me how this works but it does
        items_list = list(shop["inventory"].items())
        for i, (item, price) in enumerate(items_list, 1):
            item_desc = Items[item]["description"].split("|")[0].strip()
            print(f"{i}. {item} - {price} coins - {item_desc}")
        print(f"{len(items_list) + 1}. Cancel")
        
        try:
            choice = int(input("\nWhat would you like to buy? (number): "))
            if 1 <= choice <= len(items_list):
                item, price = items_list[choice - 1]
                
                coin_count = PlayerInventory.count("coin")
                if coin_count >= price:
                    for _ in range(price):
                        PlayerInventory.remove("coin")
                    
                    PlayerInventory.append(item)
                    print(f"\nYou bought {item} for {price} coins!")
                    
                else:
                    print(f"\nNot enough coins! You need {price} coins, but you have {coin_count}.")
            elif choice == len(items_list) + 1:
                print("Maybe next time!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a number!")

    def handle_selling(shop):
        if not PlayerInventory:
            print("\nYou have nothing to sell!")
            return
        
        sellable_items = []
        for item in set(PlayerInventory):
            if item in shop["buy_prices"]:
                count = PlayerInventory.count(item)
                price = shop["buy_prices"][item]
                sellable_items.append((item, count, price))
        
        if not sellable_items:
            print("\nThe shopkeeper isn't interested in your items!")
            return
        
        print("\n--- Items to Sell ---")
        for i, (item, count, price) in enumerate(sellable_items, 1):
            print(f"{i}. {item} (x{count}) - {price} coins each")
        print(f"{len(sellable_items) + 1}. Cancel")
        
        try:
            choice = int(input("\nWhat would you like to sell? (number): "))
            if 1 <= choice <= len(sellable_items):
                item, count, price = sellable_items[choice - 1]
                
                if count > 1:
                    amount = input(f"How many {item}s? (1-{count}): ")
                    try:
                        amount = int(amount)
                        if amount < 1 or amount > count:
                            print("Invalid amount!")
                            return
                    except ValueError:
                        print("Please enter a number!")
                        return
                else:
                    amount = 1
                
                for _ in range(amount):
                    PlayerInventory.remove(item)
                
                for _ in range(price * amount):
                    PlayerInventory.append("coin")
                
                print(f"\nSold {amount}x {item} for {price * amount} coins!")
                
            elif choice == len(sellable_items) + 1:
                print("Maybe next time!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a number!")

    enemies = {
        (9, 10): { #done
            "name": "Minotaur",
            "description": "A fitting enemy for the labyrinth",
            "dead": False,
            "requirement": "You need >= 90 and a mace",
            "loot": [],
        },
        (8, 1): {
            "name": "Troll", #done
            "description": "A troll with a mace in a maze",
            "dead": False,
            "requirement": "You need >= 70 and a sword",
            "loot": ["mace","coin","coin","coin","coin","coin"],
        },
        (5, 7): { #done
            "name": "Brute",
            "description": "A large (but rather dumb looking) beast holding a gleaming sword",
            "dead": False,
            "requirement": "You need >= 60 and a spear",
            "loot": ["sword","coin","coin","coin","coin"],
        },
        (13, 10): { #done
            "name": "Goblin",
            "description": "Human looking green man with a custom made spear",
            "dead": False,
            "requirement": "You need >= 50 and a rusty dagger",
            "loot": ["spear","coin","coin","coin"],
        },
        (13, 4): { # done
            "name": "Skeleton",
            "description": "A bony creature made of bones holding a beating up dagger",
            "dead": False,
            "requirement": "You need >= 50 and a rock",
            "loot": ["rusty dagger","coin","coin"],
        },
        (2, 18): { #done
            "name": "Giant Rat",
            "description": "A large pest the size of a panther",
            "dead": False,
            "requirement": "You need >= 40 and a rock",
            "loot": ["coin"],
        }
    }

    def get_room_description(row, col):
        pos = (row, col)
        
        if pos in RoomDescriptions:
            return RoomDescriptions[pos]

        return "A nondescript part of the maze."

    Doors = {
        (2, 1): {"locked": True, "key_needed": "door_1", "description": "A worn down door"}, #door in the top left (west entrance) key coords [4,3]
        (9, 11): {"locked": True, "key_needed": "door_2", "description": "A gold-reinforced door"}, #final door to enter the booss fight [6,3]
        (6, 16): {"locked": True, "key_needed": "door_3", "description": "A heavy wooden door"}, #door in the top right that splits the path [1,18]
        (17, 14): {"locked": True, "key_needed": "door_4", "description": "A iron prison cell that is holding a man captive"}, #door to open to help the man escape key coords [15,8]
    }

    Items = {
        "letter": {
            "description": "A crumpled letter with writing on it",
            "text": """
                                    WELCOME TO ZORK 2
    
        ZORK 2 is a game of adventure, danger, and low cunning.  In it you will explore some of the most amazing territory ever seen by mortal man.  Hardened adventurers have run screaming from the terrors contained within!
    
        In ZORK 2 the intrepid explorer (you) is stuck on the outside of a labyrinth deep in the bowels of the earth, searching for vast treasures long hidden from prying eyes, treasures guarded by fearsome monsters and diabolical traps!

        To win, you must find the centre of the maze and escape through a ladder to reach the surfaceof the modern world.

        ZORK 2 was created in my room by me (Aron).  It was inspired by the adventure game ZORK.
    
        Information may be available using the HELP (shows how to play the game) and INFO (shows the list of commands in the game) commands.
    
        (c) Copyright by Me?. Email | verify.exe101@gmail.com | if there are any bugs (probably a lot)
                        All rights reserved.
    """,
            "grabbable": True,
            "readable": True,
            "weight": 2
        },
        "note": {
            "description": "A wrangled old note",
            "text": "time",
            "grabbable": True,
            "readable": True,
            "weight": 1
        },
        "torn journal": {
            "description": "A partially destroyed journal",
            "text": """
            Day 47: The others are gone. I'm the last one left.
            I think they left me here to die... they havent came with 
            food for the past 3 days, I am being made to die a slow death...
            - Marcus
            """,
            "grabbable": True,
            "readable": True,
        },
        "sign": {
            "description": "A old wooden sign",
            "text": "You need a brass key for this door",
            "grabbable": False,
            "readable": True,
            "weight": 0
        },
        "crossroad sign": {
            "description": "A old wooden sign",
            "text": """
    =====================================
                ADVERTISMENT
    =====================================
        SHOP TOWARDS WEST OF THIS SIGN        
    """,
            "grabbable": False,
            "readable": True,
            "weight": 0
        },
        "prison sign": {
            "description": "A metal sign with letters etched into it",
            "text": """
    =====================================
                BEWARE
    =====================================
        PRISONS EAST TO THIS SIGN        
    """,
            "grabbable": False,
            "readable": True,
            "weight": 0
        },
        "danger sign": {
            "description": "A warning sign",
            "text": """
    ===============================
                DANGER
                TRAPS
    ===============================""",
            "grabbable": False,
            "readable": True,
            "weight": 0
        },
        "final sign": {
            "description": "The final sign",
            "text": "Gold key needed for this door",
            "grabbable": False,
            "readable": True,
            "weight": 0
        },
        #Keys
        "brass key": {
            "description": "A worn down brass key",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 3,
            "opens": "door_1"  # Opens the door in the top left 
        },
        "gold key": {
            "description": "A shiny golden key, looks important",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 3,
            "opens": "door_2"  # Opens tha door that leads to the boss fight
        },
        "copper key": {
            "description": "A cold copper key",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 3,
            "opens": "door_3"  # Opens the door in the top right that splits the path
        },
        "iron key": {
            "description": "A rusty iron key",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 3,
            "opens": "door_4"  # Opens the door for the man to escape
        },
        #Weapons
        "mace": { #strongest, needed to kill the minotaur
            "description": "A mean looking mace with spikes coming out of it",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 10
        },
        "sword": { #2nd strongest, needed to kill the troll
            "description": "A gleaming sword",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 8
        },
        "spear": { #3rd strongest, needed to kill the brute
            "description": "A hardwood pole with a iron spike on the end",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 7
        },
        "rusty dagger": { #4th strongest, needed to kill the goblin
            "description": "A dodgy looking dagger",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 5
        },
        "rock": { #5th strongest, needed to kill the giant rat and skeleton
            "description": "A sharp rock that looks like it could do some damage",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 3,
        },
        #Others 
        "bread": {
            "description": "Some tasty but stale bread | Restores 30 health",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 3
        },
        "bandage": {
            "description": "A nice length of bandage to heal bones and wounds | Restores 50 health",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 5
        },
        "cheese": {
            "description": "Slightly mouldy cheese | Restores 20 health",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 3
        },
        "gruel": {
            "description": "A small nasty looking bowl of gruel | Restores 10 health",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 2
        },
        "coin": {
            "description": "A golden currency used to trade",
            "text": None,
            "grabbable": True,
            "readable": False,
            "weight": 1
        }
    }

    def get_inventory_weight():
        total_weight = 0
        for item in PlayerInventory:
            if "weight" in Items[item]:
                total_weight += Items[item]["weight"]
        return total_weight

    NPCs = {
        (10, 1): {
            "name": "Riddler",
            "type": "riddler",
            "description": "a mysterious figure in a green suit covered in question marks",
            "riddle":"""
        I am ever present; nothing escapes my my view. My nature
        never changes, but by it, I change all. Even the strongest 
        warrior falls when I pass him by. What am I?""",
            "answer": "time",
            "solved": False,
            "dialogue_before": "Answer my riddle and you may pass...",
            "dialogue_after": "Impressive! You may pass."
        },
        (14, 1): {
            "name": "Merchant",
            "type": "shop",
            "description": "a friendly merchant with a nice smile",
        },
        (17, 14): {
            "name": "Prisoner",
            "type": "prisoner",
            "description": "a old man covered in rags",
            "free": False
        },
    }

    def prisoner_dots_cycling():
        frames = [".  ", ".. ", "..."]
        for i in range(9):
            print(f"\rPrisoner: {frames[i % 3]}", end="", flush=True)
            time.sleep(0.4)
        sys.stdout.write("\033[F")  
        sys.stdout.write("\033[K")  
        sys.stdout.write("\033[1B")
        sys.stdout.flush()

    def player_dot_cycling():
        frames = [".  ", ".. ", "..."]
        for i in range(9):
            print(f"\rYou: {frames[i % 3]}", end="", flush=True)
            time.sleep(0.4)
        sys.stdout.write("\033[F")  
        sys.stdout.write("\033[K")  
        sys.stdout.write("\033[1B")
        sys.stdout.flush()

    def prisoner_dialogue():
        typewriter("\nPrisoner: help me...")
        print("\n1 - What happened to you?")
        print("2 - Who are you?")

        PlayerInput = int(input("\n>"))
        while PlayerInput not in [1,2]:
            print("Choose a number")
            PlayerInput = int(input("\n>"))

        if PlayerInput == 1:
            print()
            prisoner_dots_cycling()
            frames = [".  ", ".. ", "..."]
            for i in range(9):
                print(f"\rPrisoner: I dont know {frames[i % 3]}", end="", flush=True)
                time.sleep(0.4)
            sys.stdout.write("\033[F")  
            sys.stdout.write("\033[K")  
            sys.stdout.write("\033[1B")
            sys.stdout.flush()
            typewriter("Prisoner: I was doing something until i think i was knocked out and trapped here")
            print("\n1 - Who are you?")
            PlayerInput = int(input("\n>"))
            while PlayerInput != 1:
                PlayerInput = int(input("\n>"))
            print()
            prisoner_dots_cycling()
            print("Prisoner: My name is William, whats yours?")
            PlayerName = input("\n>")
            print()
            prisoner_dots_cycling()
            sys.stdout.write("\033[K")  
            sys.stdout.flush()
            print("Prisoner: Right, nice to meet you" ,PlayerName, ",will you help me get out of here?")
            print("\n1 - Yes")
            print("2 - No i have to go, im sorry")
            PlayerInput = int(input("\n>"))
            while PlayerInput not in [1,2]:
                print("Choose a number")
                PlayerInput = int(input("\n>"))

            if PlayerInput == 1:
                print("\nPrisoner: God bless you",PlayerName)
                print("\nPrison: I belive that the time i was captured, the poeple who put me here went west from here")
                print("\nPrisoner: Im sure the key is in that direction")
                print("\n1 - What type of key?")
                PlayerInput = int(input("\n>"))
                while PlayerInput != 1:
                    print("Choose a number")
                    PlayerInput = int(input("\n>"))

                time.sleep(2)            
                print("\nWilliam: I believe it was an iron key, i remember the shine it gave")
                time.sleep(2)
                print("\n1 - Ill be back soon ,sit tight")
                PlayerInput = int(input("\n>"))
                while PlayerInput != 1:
                    print("Choose a number")
                    PlayerInput = int(input("\n>"))
                time.sleep(2)
                print("\nWilliam: Thank you and stay safe",PlayerName)

            elif PlayerInput == 2:
                print("I understand, i hope you find your way out",PlayerName)
        
        elif PlayerInput == 2:
            print()
            prisoner_dots_cycling()
            print("Prisoner: My name is William, whats yours?")
            PlayerName = input("\n>")
            print()
            prisoner_dots_cycling()
            sys.stdout.write("\033[K")  
            sys.stdout.flush()
            print("Prisoner: Right, nice to meet you" ,PlayerName, ",will you help me get out of here?")
            print("\n1 - Yes")
            print("2 - No i have to go, im sorry")
            PlayerInput = int(input("\n>"))
            while PlayerInput not in [1,2]:
                print("Choose a number")
                PlayerInput = int(input("\n>"))

            if PlayerInput == 1:
                print("\nPrisoner: God bless you",PlayerName)
                time.sleep(3)
                print("\nPrison: I belive that the time i was captured, the poeple who put me here went west from here")
                time.sleep(4)
                print("\nPrisoner: Im sure the key is in that direction")
                time.sleep(3)
                print("\n1 - What type of key?")
                PlayerInput = int(input("\n>"))
                while PlayerInput != 1:
                    print("Choose a number")
                    PlayerInput = int(input("\n>"))

                time.sleep(2)            
                print("\nWilliam: I believe it was an iron key, i remember the shine it gave")
                time.sleep(2)
                print("\n1 - Ill be back soon ,sit tight")
                PlayerInput = int(input("\n>"))
                while PlayerInput != 1:
                    print("Choose a number")
                    PlayerInput = int(input("\n>"))
                time.sleep(2)
                print("\nWilliam: Thank you and stay safe",PlayerName)
            elif PlayerInput == 2:
                print("I understand, i hope you find your way out",PlayerName)

    def prisoner_dialogue2():
        print()
        prisoner_dots_cycling()
        typewriter("Prisoner: Well, ill be damned!")
        typewriter("\nWilliam: You found it!")
        typewriter("\nWilliam: I will be forever grateful friend!")
        typewriter("\nWilliam: I will join you on this journey")
        print()
        prisoner_dots_cycling()
        typewriter("William: Till death do us part...")
        print("\nWilliam will now aid you in battle as a gratitude of your kindness!")
        print("You can give him weapons using the 'give' command to make him stronger in battle")
        print("You can take the weapon back by using the 'take' command")

    def handle_npc_interaction(npc, npc_row, npc_col):
        if npc["type"] == "riddler":
            if not npc["solved"]:
                print(f"\n{npc['name']} asks: \"{npc['riddle']}\"")
                answer = input("\nYour answer: ").lower().strip()
                if answer == npc["answer"]:
                    npc["solved"] = True
                    print(f"\n{npc['name']}: \"{npc['dialogue_after']}\"")
                    Maze[npc_row][npc_col] = 0 
                else:
                    print(f"\n{npc['name']}: Wrong! Try again when youre wiser.")
            else:
                print("Riddler: Hello there")

    def handle_enemy_interaction(enemy, enemy_row, enemy_col):
        nonlocal row, col
        nonlocal PlayerHealth
        nonlocal PlayerPos
        nonlocal VisitedRooms
        
        if enemy["dead"]:
            print(f"There is a slayed {enemy['name']} on the ground")
            return PlayerHealth, PlayerPos
        
        print(f"\n{'='*50}")
        typewriter(f"\nYou engage the {enemy['name']} in combat!\n")
        print(f"{'='*50}")
        time.sleep(0.5)
        
        player_damage = 5
        weapon_used = "fists"
        
        if "mace" in PlayerInventory:
            player_damage = random.randint(20, 30)
            weapon_used = "mace"
        elif "sword" in PlayerInventory:
            player_damage = random.randint(15, 25)
            weapon_used = "sword"
        elif "spear" in PlayerInventory:
            player_damage = random.randint(12, 20)
            weapon_used = "spear"
        elif "rusty dagger" in PlayerInventory:
            player_damage = random.randint(8, 15)
            weapon_used = "rusty dagger"
        elif "rock" in PlayerInventory:
            player_damage = random.randint(5, 10)
            weapon_used = "rock"
        
        enemy_stats = {
            "Minotaur": {"health": 80, "damage": (20, 35), "weapon_needed": "mace"},
            "Troll": {"health": 60, "damage": (12, 25), "weapon_needed": "sword"},
            "Brute": {"health": 50, "damage": (10, 20), "weapon_needed": "spear"},
            "Goblin": {"health": 35, "damage": (8, 15), "weapon_needed": "rusty dagger"},
            "Skeleton": {"health": 30, "damage": (5, 12), "weapon_needed": "rock"},
            "Giant Rat": {"health": 20, "damage": (3, 8), "weapon_needed": "rock"},
        }
        
        stats = enemy_stats.get(enemy["name"], {"health": 25, "damage": (5, 15), "weapon_needed": "rock"})
        enemy_health = stats["health"]
        enemy_min_damage, enemy_max_damage = stats["damage"]
        
        william_bonus = 0
        if prisoner_dialogue_done2:
            william_bonus = random.randint(3, 8)
            william_bonus = william_bonus * william_multi
            print("William fights alongside you!")
            time.sleep(0.5)
        
        print(f"\n{enemy['name']} Health: {enemy_health}")
        print(f"Your Health: {PlayerHealth}")
        print(f"Your Weapon: {weapon_used} (Damage: {player_damage})")
        if prisoner_dialogue_done2 == True:
            print(f"William's Bonus: +{william_bonus} damage")
        
        turn = 1
        while enemy_health > 0 and PlayerHealth > 0:
            print(f"\n--- Turn {turn} ---")
            time.sleep(0.5)
            
            total_damage = player_damage + william_bonus
            enemy_health -= total_damage
            
            print(f"Your {weapon_used} deals {total_damage} damage!")
            
            if enemy_health <= 0:
                enemy_health = 0
                print(f"\nThe {enemy['name']} has been defeated!")
                time.sleep(2)
                break
            
            print(f"{enemy['name']} Health: {enemy_health}")
            time.sleep(2)
            
            enemy_damage = random.randint(enemy_min_damage, enemy_max_damage)
            
            print(f"The {enemy['name']} attacks you for {enemy_damage} damage!")

            PlayerHealth -= enemy_damage

            print(f"Your Health: {PlayerHealth}")
            
            if PlayerHealth <= 20 and PlayerHealth > 0:
                print("Your health is low!")

            elif PlayerHealth <= 50 and PlayerHealth > 20:
                print("You're taking heavy damage!")
            
            if PlayerHealth <= 0:
                PlayerHealth = 0
                print(f"\nThe {enemy['name']} has defeated you!")
                print("Your vision fades to black...")
                time.sleep(3)
                return PlayerHealth, PlayerPos
            
            time.sleep(0.5)
            turn += 1
            
            if turn % 3 == 0 and enemy_health > 0 and PlayerHealth > 0:
                print(f"\n{'='*50}")
                print("\nWhat do you want to do?")
                print("1. Continue fighting")
                print("2. Use healing item")
                print("3. Try to flee")
                
                PlayerInput = input("\n>").strip()
                
                if PlayerInput == "2":
                    healing_items = [item for item in PlayerInventory if item in ["bread", "bandage", "cheese", "gruel"]]
                    if healing_items:
                        print("\nHealing items:")
                        for i, item in enumerate(healing_items, 1):
                            heal_amount = {"bread": 30, "bandage": 50, "cheese": 20, "gruel": 10}[item]
                            print(f"{i}. {item}")
                        print(f"{i + 1}. Cancel")
                        
                        try:
                            PlayerInput = int(input("\n>"))

                            if 1 <= PlayerInput <= len(healing_items):
                                item = healing_items[PlayerInput - 1]
                                heal_amount = {"bread": 30, "bandage": 50, "cheese": 20, "gruel": 10}[item]
                                PlayerHealth = min(100, PlayerHealth + heal_amount)
                                PlayerInventory.remove(item)
                                print(f"\nYou use {item} and restore {heal_amount} health!")
                                print(f"Health: {PlayerHealth}")

                            elif PlayerInput == i + 1:
                                print("You decide to save your items.")
                            else:
                                print("Invalid choice!")
                        except ValueError:
                            print("Please enter a number!")
                    else:
                        print("You have no healing items!")
                
                elif PlayerInput == "3":
                        print(f"\nYou successfully flee from the {enemy['name']}!")
                        time.sleep(2)
                        return PlayerHealth, PlayerPos
        
        if enemy_health <= 0:
            print(f"\n{'='*50}")
            typewriter(f"Victory! The {enemy['name']} has been slain!")
            print(f"{'='*50}")
            
            enemy["dead"] = True
            enemy["name"] = f"Dead {enemy['name']}"
            Maze[enemy_row][enemy_col] = 0
            
            if enemy["loot"]:
                pos = (enemy_row, enemy_col)
                if pos not in RoomItems:
                    RoomItems[pos] = []
                RoomItems[pos].extend(enemy["loot"])
                print(f"The {enemy['name']} dropped: {', '.join(enemy['loot'])}")
            
            row = enemy_row
            col = enemy_col
            PlayerPos = [row, col]
            
            time.sleep(3)
        
        return PlayerHealth, PlayerPos

    def get_adjacent_npcs(row, col):
        npcs_found = []
        if (row, col) in NPCs:
            npcs_found.append(("next", row, col))
        if row > 0 and (row-1, col) in NPCs:
            npcs_found.append(("north", row-1, col))
        if row < len(Maze)-1 and (row+1, col) in NPCs:
            npcs_found.append(("south", row+1, col))
        if col < len(Maze[0])-1 and (row, col+1) in NPCs:
            npcs_found.append(("east", row, col+1))
        if col > 0 and (row, col-1) in NPCs:
            npcs_found.append(("west", row, col-1))
        return npcs_found

    def get_adjacent_enemies(row, col):
        enemies_found = []
        if (row, col) in enemies:
            enemies_found.append(("next", row, col))
        if row > 0 and (row-1, col) in enemies:
            enemies_found.append(("north", row-1, col))
        if row < len(Maze)-1 and (row+1, col) in enemies:
            enemies_found.append(("south", row+1, col))
        if col < len(Maze[0])-1 and (row, col+1) in enemies:
            enemies_found.append(("east", row, col+1))
        if col > 0 and (row, col-1) in enemies:
            enemies_found.append(("west", row, col-1))
        return enemies_found

    def get_adjacent_doors(row, col):
        adjacent = []
        if row > 0 and Maze[row - 1][col] == 9:
            adjacent.append(("north", row - 1, col))
        if row < len(Maze) - 1 and Maze[row + 1][col] == 9:
            adjacent.append(("south", row + 1, col))
        if col < len(Maze[0]) - 1 and Maze[row][col + 1] == 9:
            adjacent.append(("east", row, col + 1))
        if col > 0 and Maze[row][col - 1] == 9:
            adjacent.append(("west", row, col - 1))
        return adjacent

    print("""\n
    West side of the maze
    There is a lonely letter left on the ground""")
    #----------------------------------------------------------------------------------------------------------------------------------
    while True:
        stepCount += 1
        if PlayerHealth == 0:
            print("You have lost all of your health and died! Game Over!")
            lost += 1
            break

        if PlayerPos == [10,9]:
            print("Would you like to climb out of the maze or explore some more?")
            PlayerInput = input("\n>").lower().strip()
            if PlayerInput == "climb":   
                break
            else:
                print("Have fun and make sure to not die!")

        PlayerInput = input("\n>").lower().strip()

        if PlayerInput == "side":
            if PlayerPos == [0,10] or PlayerPos == [19,4] or PlayerPos == [9,19] or PlayerPos == [5,0]:
                print("Which side?")
                PlayerInput = input("\n>").lower().strip()

                if PlayerInput == "north" or PlayerInput == "n":
                    row = 0
                    col = 10
                    PlayerPos = [row,col]
                    VisitedRooms.add((row, col))
                    print("""North Side of the maze

    You are at the north entrance of the maze, there is a wall to the west and east of you with a path going south""")

                elif PlayerInput == "south" or PlayerInput == "s":
                    row = 19
                    col = 4
                    PlayerPos = [row,col]
                    VisitedRooms.add((row, col))
                    print("""South Side of the maze

    You are at the south entrance of the maze, there is a wall to the west and east of you with a path going north""")

                elif PlayerInput == "east" or PlayerInput == "e":
                    row = 9
                    col = 19
                    PlayerPos = [row,col]
                    VisitedRooms.add((row, col))
                    print("""East Side of the maze

    You are at the east entrance of the maze, there is a wall to the north and south of you with a path going west""")

                elif PlayerInput == "west" or PlayerInput == "w":
                    row = 5
                    col = 0
                    PlayerPos = [row,col]
                    VisitedRooms.add((row, col))
                    print("""West Side of the maze

    You are at the west entrance of the maze, there is a wall to the north and south of you with a path going west""")
                else:
                    print("What does",PlayerInput,"even mean?")

            else:
                print("You cant go to the side as you are inside the maze!")

        elif PlayerInput == "go":
            print("Youll have to say which compass direction to go in")
            PlayerInput = input("\n>").lower().strip()

            if PlayerInput == "n" or PlayerInput == "north":

                if Maze[row - 1][col] == 8: 
                    npc_pos = (row - 1, col)
                    if npc_pos in NPCs and not NPCs[npc_pos]["solved"]:
                        print(f"{NPCs[npc_pos]['name']} blocks your path!")
                        print(f"\"{NPCs[npc_pos]['dialogue_before']}\"")
                    else:
                        row -= 1
                        PlayerPos = [row, col]
                        VisitedRooms.add((row, col))
                        check_for_trap(row, col)
                        print(get_room_description(row, col)) 
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))

                elif Maze[row - 1][col] == 5: 
                    enemy_pos = (row - 1, col)
                    if enemy_pos in enemies and not enemies[enemy_pos]["dead"]:
                        print(f"{enemies[enemy_pos]['name']} blocks your path!")
                        print(f"{enemies[enemy_pos]['requirement']}")
                    else:
                        row -= 1
                        PlayerPos = [row, col]
                        VisitedRooms.add((row, col))
                        check_for_trap(row, col)  
                        print(get_room_description(row, col)) 
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))

                elif Maze[row - 1][col] != 1:
                    if Maze[row - 1][col] == 9:
                        door_pos = (row - 1, col)
                        if door_pos in Doors and Doors[door_pos]["locked"]:
                            print(f"The door is locked! {Doors[door_pos]['description']}")
                        else:
                            row -= 1
                            PlayerPos = [row,col]
                            check_for_trap(row, col)
                            print(get_room_description(row, col))

                            pos = (row, col)
                            if pos in RoomItems and RoomItems[pos]:
                                print("You see:", ", ".join(RoomItems[pos]))
                    else:
                        row -= 1
                        PlayerPos = [row,col]
                        check_for_trap(row, col)
                        print(get_room_description(row, col))
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))
                else:
                    print("Theres a wall in the way!") 
            
            elif PlayerInput == "s" or PlayerInput == "south":
                if Maze[row + 1][col] == 8:
                    npc_pos = (row + 1, col)
                    if npc_pos in NPCs and not NPCs[npc_pos]["solved"]:
                        print(f"{NPCs[npc_pos]['name']} blocks your path!")
                        print(f"\"{NPCs[npc_pos]['dialogue_before']}\"")
                    else:
                        row += 1
                        PlayerPos = [row, col]
                        VisitedRooms.add((row, col))
                        check_for_trap(row, col)
                        print(get_room_description(row, col))
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))

                elif Maze[row + 1][col] == 5: 
                    enemy_pos = (row + 1, col)
                    if enemy_pos in enemies and not enemies[enemy_pos]["dead"]:
                        print(f"{enemies[enemy_pos]['name']} blocks your path!")
                        print(f"{enemies[enemy_pos]['requirement']}")
                    else:
                        row += 1
                        PlayerPos = [row, col]
                        VisitedRooms.add((row, col))
                        check_for_trap(row, col) 
                        print(get_room_description(row, col)) 
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))

                elif Maze[row + 1][col] != 1:
                    if Maze[row + 1][col] == 9:
                        door_pos = (row + 1, col)
                        if door_pos in Doors and Doors[door_pos]["locked"]:
                            print(f"The door is locked! {Doors[door_pos]['description']}")
                        else:
                            row += 1
                            PlayerPos = [row,col]
                            check_for_trap(row, col)
                            print(get_room_description(row, col))

                            pos = (row, col)
                            if pos in RoomItems and RoomItems[pos]:
                                print("You see:", ", ".join(RoomItems[pos]))
                    else:
                        row += 1
                        PlayerPos = [row,col]
                        check_for_trap(row, col)
                        print(get_room_description(row, col))
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))
                else:
                    print("Theres a wall in the way!") 
            
            elif PlayerInput == "e" or PlayerInput == "east":
                if Maze[row][col + 1] == 8:
                    npc_pos = (row, col + 1)
                    if npc_pos in NPCs and not NPCs[npc_pos]["solved"]:
                        print(f"{NPCs[npc_pos]['name']} blocks your path!")
                        print(f"\"{NPCs[npc_pos]['dialogue_before']}\"")
                    else:
                        col += 1
                        PlayerPos = [row, col]
                        VisitedRooms.add((row, col))
                        check_for_trap(row, col)
                        print(get_room_description(row, col))
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))

                elif Maze[row][col + 1] == 5: 
                    enemy_pos = (row, col + 1)
                    if enemy_pos in enemies and not enemies[enemy_pos]["dead"]:
                        print(f"{enemies[enemy_pos]['name']} blocks your path!")
                        print(f"{enemies[enemy_pos]['requirement']}")
                    else:
                        col += 1
                        PlayerPos = [row, col]
                        VisitedRooms.add((row, col))
                        check_for_trap(row, col)
                        print(get_room_description(row, col)) 
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))

                elif Maze[row][col + 1] != 1:
                    if Maze[row][col + 1] == 9:
                        door_pos = (row, col + 1)
                        if door_pos in Doors and Doors[door_pos]["locked"]:
                            print(f"The door is locked! {Doors[door_pos]['description']}")
                        else:
                            col += 1
                            PlayerPos = [row,col]
                            check_for_trap(row, col)
                            print(get_room_description(row, col))

                            pos = (row, col)
                            if pos in RoomItems and RoomItems[pos]:
                                print("You see:", ", ".join(RoomItems[pos]))
                    else:
                        col += 1
                        PlayerPos = [row,col]
                        check_for_trap(row, col)
                        print(get_room_description(row, col))
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))
                else:
                    print("Theres a wall in the way!") 
            
            elif PlayerInput == "w" or PlayerInput == "west":
                if Maze[row][col - 1] == 8:
                    npc_pos = (row, col - 1)
                    if npc_pos in NPCs and not NPCs[npc_pos]["solved"]:
                        print(f"{NPCs[npc_pos]['name']} blocks your path!")
                        print(f"\"{NPCs[npc_pos]['dialogue_before']}\"")
                    else:
                        col -= 1
                        PlayerPos = [row, col]
                        VisitedRooms.add((row, col))
                        check_for_trap(row, col)
                        print(get_room_description(row, col))
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))
                elif Maze[row][col - 1] == 5: 
                    enemy_pos = (row, col - 1)
                    if enemy_pos in enemies and not enemies[enemy_pos]["dead"]:
                        print(f"{enemies[enemy_pos]['name']} blocks your path!")
                        print(f"{enemies[enemy_pos]['requirement']}")
                    else:
                        col -= 1
                        PlayerPos = [row, col]
                        VisitedRooms.add((row, col))
                        check_for_trap(row, col) 
                        print(get_room_description(row, col)) 
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))

                elif Maze[row][col - 1] != 1:
                    if Maze[row][col - 1] == 9:
                        door_pos = (row, col - 1)
                        if door_pos in Doors and Doors[door_pos]["locked"]:
                            print(f"The door is locked! {Doors[door_pos]['description']}")
                        else:
                            col -= 1
                            PlayerPos = [row,col]
                            check_for_trap(row, col)
                            print(get_room_description(row, col))

                            pos = (row, col)
                            if pos in RoomItems and RoomItems[pos]:
                                print("You see:", ", ".join(RoomItems[pos]))
                    else:
                        col -= 1
                        PlayerPos = [row,col]
                        check_for_trap(row, col)
                        print(get_room_description(row, col))
                        pos = (row, col)
                        if pos in RoomItems and RoomItems[pos]:
                            print("You see:", ", ".join(RoomItems[pos]))
                else:
                    print("Theres a wall in the way!") 

            else:
                print("Not a valid direction, choose either north, east, south or west")

        elif PlayerInput == "look":
            print("Look at what?")
            PlayerInput = input("\n>").lower().strip()

            if PlayerInput == "health" or PlayerInput == "h":
                print("You have", PlayerHealth, "health")

            elif PlayerInput == "inventory" or PlayerInput == "i":
                if PlayerInventory:
                    current_weight = get_inventory_weight()
                    print(f"You are carrying ({current_weight}/{MAX_WEIGHT} weight):")
                    print(", ".join(PlayerInventory))
                else:
                    print("You are not carrying anything")

            elif PlayerInput == "room":
                pos = (row, col)
                
                adjacent_doors = get_adjacent_doors(row, col)
                if adjacent_doors:
                    for direction, d_row, d_col in adjacent_doors:
                        door_pos = (d_row, d_col)
                        if door_pos in Doors:
                            if Doors[door_pos]["locked"]:
                                print(f"There is a locked door {direction} to you")
                            else:
                                print(f"There is an unlocked door {direction} to you")
                        else:
                            print(f"There is a door {direction} to you")

                adjacent_npcs = get_adjacent_npcs(row, col)
                for direction, npc_row, npc_col in adjacent_npcs:
                    npc = NPCs[(npc_row, npc_col)]
                    print(f"There is a {npc['description']} {direction} to you")

                adjacent_enemies = get_adjacent_enemies(row, col)
                for direction, enemy_row, enemy_col in adjacent_enemies:
                    enemy = enemies[(enemy_row, enemy_col)]
                    print(f"There is a {enemy['name']} {direction} to you")           

                if pos in RoomItems and RoomItems[pos]:
                    print("You see:", ", ".join(RoomItems[pos]))
                else:
                    print("There are no useful items here")
            else:
                print("Thats not something that you can see")

        elif PlayerInput == "pick up":
            print("What do you want to pick up?")
            PlayerInput = input("\n>").lower().strip()

            pos = (row, col)
            
            if pos in RoomItems and PlayerInput in RoomItems[pos]:
                item = PlayerInput
                item_weight = Items[item].get("weight", 1)
                current_weight = get_inventory_weight()
                
                if current_weight + item_weight > MAX_WEIGHT:
                    print(f"That {item} weighs {item_weight}. You're carrying {current_weight}/{MAX_WEIGHT} weight.")
                    print("You can't carry any more!")
                elif Items[item]["grabbable"]:
                    RoomItems[pos].remove(item)
                    PlayerInventory.append(item)
                    print(f"You picked up the {item} (weight: {item_weight})")
                    print(f"Total weight: {get_inventory_weight()}/{MAX_WEIGHT}")
                    if not RoomItems[pos]:
                        del RoomItems[pos]
                else:
                    print(f"You can't pick up the {item}!")
            else:
                print(f"There is no {PlayerInput} here!")

        elif PlayerInput == "pick up all":
            pos = (row, col)
            
            if pos not in RoomItems or not RoomItems[pos]:
                print("There's nothing here to pick up!")
            else:
                items_picked = []
                items_left = []
                current_weight = get_inventory_weight()
                
                for item in RoomItems[pos][:]:
                    if not Items[item]["grabbable"]:
                        items_left.append(item)
                        print(f"You can't pick up the {item}!")
                        continue
                    
                    item_weight = Items[item].get("weight", 1)
                    
                    if current_weight + item_weight <= MAX_WEIGHT:
                        PlayerInventory.append(item)
                        items_picked.append(item)
                        RoomItems[pos].remove(item)
                        current_weight += item_weight
                    else:
                        items_left.append(item)
                
                if items_picked:
                    print(f"You picked up: {', '.join(items_picked)}")
                    print(f"Current weight: {current_weight}/{MAX_WEIGHT}")
                
                if items_left:
                    print(f"Couldn't carry: {', '.join(items_left)}")
                
                if not RoomItems[pos]:
                    del RoomItems[pos]

        elif PlayerInput == "drop all":
            if PlayerInventory:
                items_dropped = PlayerInventory.copy()
                PlayerInventory.clear()
                
                pos = (row, col)
                if pos not in RoomItems:
                    RoomItems[pos] = []
                RoomItems[pos].extend(items_dropped)
                
                print(f"You dropped: {', '.join(items_dropped)}")
                print("Your inventory is now empty.")
            else:
                print("You have nothing to drop!")

        elif PlayerInput == "drop":
            if PlayerInventory:
                print("What do you want to drop? ")
                PlayerInput = input("\n>").lower().strip()
                if PlayerInput in PlayerInventory:
                    PlayerInventory.remove(PlayerInput)
                    pos = (row, col)
                    if pos not in RoomItems:
                        RoomItems[pos] = []
                    RoomItems[pos].append(PlayerInput)
                    print(f"You dropped the {PlayerInput}")
                else:
                    print(f"You don't have a {PlayerInput}!")
            else:
                print("You have nothing to drop!")

        elif PlayerInput == "read":
            print("What do you want to read? ")
            PlayerInput = input("\n>").lower().strip()
            if PlayerInput in PlayerInventory:
                if Items[PlayerInput]["readable"]:
                    print(f'"{Items[PlayerInput]["text"]}"')
                else:
                    print(f"You can't read the {PlayerInput}!")
            else:
                #this is only needed if there are some signs in the maze
                pos = (row, col)
                if pos in RoomItems and PlayerInput in RoomItems[pos]:
                    if Items[PlayerInput]["readable"]:
                        print(f"You read the {PlayerInput}:")
                        print(f'"{Items[PlayerInput]["text"]}"')
                    else:
                        print(f"You can't read the {PlayerInput}!")
                else:
                    print(f"There is no {PlayerInput} to read!")

        elif PlayerInput == "inspect":
            print("What do you want to inspect? ")
            PlayerInput = input("\n>").lower().strip()
            if PlayerInput in PlayerInventory:
                print(Items[PlayerInput]["description"])
            else:
                pos = (row, col)
                if pos in RoomItems and PlayerInput in RoomItems[pos]:
                    print(Items[PlayerInput]["description"])
                else:
                    print(f"There is no {PlayerInput} to inspect!")

        elif PlayerInput == "fight":
            print("Are you sure you want to fight?")
            PlayerInput = input("\n>").lower().strip()
            if PlayerInput == "yes":
                nearby_enemies = get_adjacent_enemies(row, col)
                
                if nearby_enemies:
                    direction, enemy_row, enemy_col = nearby_enemies[0]
                    enemy = enemies[(enemy_row, enemy_col)]
                    PlayerHealth,PlayerPos = handle_enemy_interaction(enemy, enemy_row, enemy_col)
                else:
                    print("There's no one here to fight.")
            elif PlayerInput == "no":
                print("Wasting my time honestly")
            else:
                print("Please answer with a yes or no")

        elif PlayerInput == "use":
            print("What do you want to use? ")
            PlayerInput = input("\n>").lower().strip()
            if PlayerInput in PlayerInventory:

                if PlayerInput == "bread":
                    PlayerHealth += 30
                    if PlayerHealth > 100:
                        PlayerHealth = 100
                    PlayerInventory.remove("bread")
                    print("You just gained 30 health, you now have", PlayerHealth, "health")

                elif PlayerInput == "bandage":
                    PlayerHealth += 50
                    if PlayerHealth > 100:
                        PlayerHealth = 100
                    PlayerInventory.remove("bandage")
                    print("You just gained 50 health, you now have", PlayerHealth, "health")

                elif PlayerInput == "cheese":
                    PlayerHealth += 20
                    if PlayerHealth > 100:
                        PlayerHealth = 100
                    PlayerInventory.remove("cheese")
                    print("You just gained 20 health, you now have", PlayerHealth, "health")

                elif PlayerInput == "gruel":
                    PlayerHealth += 10
                    if PlayerHealth > 100:
                        PlayerHealth = 100
                    PlayerInventory.remove("gruel")
                    print("You just gained 10 health, you now have", PlayerHealth, "health")

                elif PlayerInput == "brass key":
                    adjacent_doors = get_adjacent_doors(row, col)
                    if adjacent_doors:
                        unlocked_any = False
                        for direction, d_row, d_col in adjacent_doors:
                            door_pos = (d_row, d_col)
                            if door_pos in Doors and Doors[door_pos]["locked"]:
                                if Items["brass key"]["opens"] == Doors[door_pos]["key_needed"]:
                                    Doors[door_pos]["locked"] = False
                                    print(f"You unlock the door to the {direction} with your key!")
                                    unlocked_any = True
                        if not unlocked_any:
                            print("None of the adjacent doors can be unlocked with this key.")
                    else:
                        print("There are no doors nearby to use the key on.")

                elif PlayerInput == "copper key":
                    adjacent_doors = get_adjacent_doors(row, col)
                    if adjacent_doors:
                        unlocked_any = False
                        for direction, d_row, d_col in adjacent_doors:
                            door_pos = (d_row, d_col)
                            if door_pos in Doors and Doors[door_pos]["locked"]:
                                if Items["copper key"]["opens"] == Doors[door_pos]["key_needed"]:
                                    Doors[door_pos]["locked"] = False
                                    print(f"You unlock the door to the {direction} with your key!")
                                    unlocked_any = True
                        if not unlocked_any:
                            print("None of the adjacent doors can be unlocked with this key.")
                    else:
                        print("There are no doors nearby to use the key on.")                

                elif PlayerInput == "iron key":
                    adjacent_doors = get_adjacent_doors(row, col)
                    if adjacent_doors:
                        unlocked_any = False
                        for direction, d_row, d_col in adjacent_doors:
                            door_pos = (d_row, d_col)
                            if door_pos in Doors and Doors[door_pos]["locked"]:
                                if Items["iron key"]["opens"] == Doors[door_pos]["key_needed"]:
                                    Doors[door_pos]["locked"] = False
                                    unlocked_any = True

                                    if door_pos == (17,14):
                                        NPCs[(17, 14)]["free"] = True
                                        print("You unlocked the prison door")
                                    else:
                                        print(f"You unlock the door to the {direction} with your key!")

                        if not unlocked_any:
                            print("None of the adjacent doors can be unlocked with this key.")
                    else:
                        print("There are no doors nearby to use the key on.")

                elif PlayerInput == "gold key":
                    adjacent_doors = get_adjacent_doors(row, col)
                    if adjacent_doors:
                        unlocked_any = False
                        for direction, d_row, d_col in adjacent_doors:
                            door_pos = (d_row, d_col)
                            if door_pos in Doors and Doors[door_pos]["locked"]:
                                if Items["gold key"]["opens"] == Doors[door_pos]["key_needed"]:
                                    Doors[door_pos]["locked"] = False
                                    print(f"You unlock the door to the {direction} with your key!")
                                    unlocked_any = True
                        if not unlocked_any:
                            print("None of the adjacent doors can be unlocked with this key.")
                    else:
                        print("There are no doors nearby to use the key on.")                       
                else:
                    print(f"You can't use the {PlayerInput} right now")
            else:
                print(f"You don't have a {PlayerInput}!")

        elif PlayerInput == "talk":
            nearby_npcs = get_adjacent_npcs(row, col)
            
            if nearby_npcs:
                direction, npc_row, npc_col = nearby_npcs[0]
                npc = NPCs[(npc_row, npc_col)]
                
                if npc.get("type") == "riddler":
                    handle_npc_interaction(npc, npc_row, npc_col)

                elif npc.get("type") == "prisoner":
                    if npc["free"] == False:
                        if prisoner_dialogue_done == False:
                            prisoner_dialogue_done = True
                            prisoner_dialogue()
                        else:
                            typewriter("\nWilliam: Have you found the key?")
                            print("\n1 - Yes")
                            print("2 - No")
                            PlayerInput = int(input("\n>"))
                            while PlayerInput not in [1,2]:
                                print("Enter a number")
                                PlayerInput = int(input("\n>"))
                            if PlayerInput == 2:
                                typewriter("\nWilliam: Well take your time, im not going anywhere")
                            else:
                                typewriter("\nWilliam: Well then get me out here!")
                    else:
                        if prisoner_dialogue_done2 == False:
                            prisoner_dialogue_done2 = True
                            prisoner_dialogue2()
                        else:
                            typewriter("\nWilliam: Less talking, more escaping please")
                elif npc.get("type") == "shop":
                    current_shop = shop.get((npc_row, npc_col))
                    if current_shop:
                        handle_shop_interaction(current_shop, npc_row, npc_col)
                    else:
                        print(f"{npc['name']}: \"{npc['dialogue']}\"")
                else:
                    print(f"{npc['name']}: \"{npc['dialogue']}\"")
            else:
                print("There's no one here to talk to.")

        elif PlayerInput == "give":
            if prisoner_dialogue_done2 == True:
                print("What would you like to give William?")
                PlayerInput = input("\n>").lower().strip()
                
                if PlayerInput in PlayerInventory:
                    valid_weapons = ["mace", "sword", "spear", "rusty dagger", "rock"]
                    
                    if PlayerInput in valid_weapons:
                        if william_weapon != None:
                            PlayerInventory.append(william_weapon)
                            print(f"William gives you back the {william_weapon}")
                            william_multi = 1.0
                        
                        PlayerInventory.remove(PlayerInput)
                        william_weapon = PlayerInput
                        
                        if PlayerInput == "mace":
                            william_multi = 2.0
                            print("You gave William your mace! He will now do 2.0x damage!")
                        elif PlayerInput == "sword":
                            william_multi = 1.8
                            print("You gave William your sword! He will now do 1.8x damage!")
                        elif PlayerInput == "spear":
                            william_multi = 1.6
                            print("You gave William your spear! He will now do 1.6x damage!")
                        elif PlayerInput == "rusty dagger":
                            william_multi = 1.4
                            print("You gave William your rusty dagger! He will now do 1.4x damage!")
                        elif PlayerInput == "rock":
                            william_multi = 1.2
                            print("You gave William your rock! He will now do 1.2x damage!")
                        
                    else:
                        print(f"You can't give the {PlayerInput} to William")
                else:
                    print(f"You don't have a {PlayerInput}")
            else:
                print("There's no one here to give anything to")

        elif PlayerInput == "take":
            if prisoner_dialogue_done2 == True:
                if william_weapon is not None:
                    PlayerInventory.append(william_weapon)
                    print(f"William gives you back the {william_weapon}.")
                    william_weapon = None
                    william_multi = 1.0
                else:
                    print("William doesn't have any weapon to give back.")
            else:
                print("There's no one here to take from.")

        elif PlayerInput == "info":
            print("""
    These are the commands that exist in the game, USE THEM and please make sure to check your spelling
        side - This will let you switch to a different side of the maze (only works at the entrances)
        go - This will allow you to move around the maze in 4 directions (north,east,south,west)
        look - This will allow you to look at either your health, inventory or the room you are in
        pick up - self explanatory, it lets you pick stuff up and hold it in yyour inventory
        pick up all - Works after the 'pick up' command and allows you to pick up all items avaliable to you 
        drop - Literatlly the opposite of pick up
        drop all - Allows you to drop everything in your inventory
        read - lets you read whatver you have in your inventory
        inspect - This will describe an item in your inventory of choosing (this is not the same as read)
        use - This will allow you to use the item of choosing from your inventory
        talk - Allows you to talk to NPCs near you
        fight - Allows you to fight enemies near you
        template - Gives you a template of the map of the maze
        map - Shows your current position in the maze
        cheats - This will give you invincibility, all of the items to beat the game and prints you a map of the whole maze
    Top tips:
        Whenever you use an item, make sure you spell it EXACTLY the same as when you see it
        
        The direction commands are shortened to the first letter, so;
            n - north
            s - south
            e - east
            w - west
        This also applies to;
            i - inventory
            t - template
            h - health
            """)

        elif PlayerInput == "help":
            print("""
    To win, you have to enter the maze and find the centre to escape through the ladder to the surface of the earth
    You have to make sure you are healthy, have good weapons and items that help you to kill the final boss in the centre
    It is highly recommended to keep track of what the maze looks like so you can backtrack and go into different areas 
    (type "template" for the template of what the maze looks lke or "cheats" for invincibility, all of the items to beat the game and a map of the whole maze)""")

        elif PlayerInput == "template" or PlayerInput == "t": #DONT CHANGE--------
            print("""                     
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 2
        1, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 1, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
        1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

    The 1's represent walls 
    The 9's represent the final exit
    the 2's represent the 4 entrances
    Thats all of the info that im giving you
    Good luck traveller
    """)

        elif PlayerInput == "cheats": #DONT CHANGE--------
            print("You really thought i was going to give you all that? LOOOOOL Nice try")

        elif PlayerInput == "quit": #DONT CHANGE--------
            print("Are you sure you want to quit?")
            PlayerInput = input("\n>").lower().strip()
            if PlayerInput == "yes":
                print("GoodBye! Hope you had fun!")
                exit()
            elif PlayerInput == "no":
                print("Then why ask? Wasting my damn time")
            else:
                print("Please answer with a yes or no")

        elif PlayerInput == "swear": #DONT CHANGE--------
            RandomNumber = random.randint(1,2)
            if RandomNumber == 1:
                print("F*ck")
            elif RandomNumber == 2:
                print("Sh*t")
        
        elif PlayerInput == "map":
            print("Your map:")
            for r in range(20):
                for c in range(20):
                    if (r, c) == (row, col):
                        print("@", end=" ")
                    else:
                        print("?", end=" ")
                print()

        elif PlayerInput == "hello": #DONT CHANGE--------
            print("Good day.")

        elif PlayerInput == "what": #DONT CHANGE--------
            print("What do you want to what is?")

        elif PlayerInput == "where": #DONT CHANGE--------
            print("Where do you want to where is?")

        elif PlayerInput == "time": #DONT CHANGE--------
            elapsed_seconds = time.time() - start_time
            minutes = int(elapsed_seconds // 60)
            seconds = int(elapsed_seconds % 60)
            if minutes == 0:
                print(f"You have been playing for {seconds} seconds too long")
            else:
                print(f"You have been playing for {minutes} minutes and {seconds} seconds too long")

        elif PlayerInput == "shout" or PlayerInput == "scream" or PlayerInput == "yell": #DONT CHANGE--------
            print("AAAARRRRRRRGGGGGHHHHhhhhh")

        elif PlayerInput == "":
            print("I beg your pardon?")

        else: #DONT CHANGE--------
            print("Thats not a verb i recognise")

    if lost == 1:
        time.sleep(3)
        typewriter("\nOh dear, you died ")
        time.sleep(1)
        typewriter("\nIt happens to the best of us! ")
        typewriter("\nAll it takes is a retry and eventually youll make it")
        typewriter("\nHere are some stats of your journey")
        print("\n================================================================")
        print("\nYou took", stepCount)
        elapsed_seconds = time.time() - start_time
        minutes = int(elapsed_seconds // 60)
        seconds = int(elapsed_seconds % 60)
        time.sleep(1)
        print(f"You wasted {minutes} minutes and {seconds} seconds")
        print("Would you like to play again?")
        PlayerInput = input("\n>")
        if PlayerInput == "yes":
            Zork_2()
        else:
            print("Hope you had fun!")
            exit()
        time.sleep(10)

    else:
        typewriter("\nWow you made it! Well done traveller")
        time.sleep(3)
        typewriter("\nHere are some stats of your journey")
        print("\n================================================================")
        print("\nIt took you", stepCount,"steps to complete your journey")
        elapsed_seconds = time.time() - start_time
        minutes = int(elapsed_seconds // 60)
        seconds = int(elapsed_seconds % 60)
        print(f"and {minutes} minutes and {seconds} seconds to complete the game!")
        time.sleep(5)
        typewriter("\nYou now step and see the world for the first time in 7 years..")
        print()
        time.sleep(10)

Zork_2()