


def start():
    """Commences the game."""
    print("\n" * 3)
    print("ZORKLON 5")
    print("\n" * 3)
    print("""\tYour spaceship crash lands on Zorklon 5. 
    Without the necessary Pulse Crystals, you cannot leave again.
    Nobody knows you are here. Nobody is coming to find you.
    You stare at the sky in fear... 
    but immediately make a resolve to survive and find a way home.""")
    print("\n" * 3)
    print("Hit RETURN to continue.")
    input("> ")

def ship():
    """Base of operations."""
    print("\n" * 20)
    print("You are on your ship. It is safe here.")
    print("After a night of rest, you feel refreshed.")
    health = 100
    print("Health at 100%\n")
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            workshop
            map""")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'north':
                north()
                break
            elif direction == 'south':
                south()
                break
            elif direction == 'east':
                east()
                break
            elif direction == 'west':
                west()
                break
            else:
                print("Sorry, you cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
            print()
        elif choice == "workshop":
            workshop()
        else:
            print("Sorry, you cannot do that here.")

def north():
    """north passage, travel towards mountains"""
    map['North'] = 'Mountain foothills'
    health -= 10
    if health <= 0:
        dead("You collapse from exhaustion.")
    print("\n" * 20)
    print("After a day of travel, you find yourself in the mountains.")
    print("\tThe sky is grey and threatening. \n\tThere is a winding path to the west, \n\ta jagged path up the mountain to the north, \n\tand another rocky path to the east.")
    items = None
    itemText = "Nothing of value is found here.\n"
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'north':
                farNorth()
                break
            elif direction == 'south':
                ship()
                break
            elif direction == 'east':
                northEast()
                break
            elif direction == 'west':
                northWest()
                break           
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items) # FIX THIS LATER
        else:
            print("Sorry, you cannot do that here.")



def farNorth():
    map['Far North'] = 'Craggy Mountains'
    print("\n" * 20)
    print("""You find yourself high in the mountains.
    The air is thin.
    There are no plants, just rock and wind for miles.""")
    items = 'Metal Ore'
    itemText = "You find metal ore!"
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'south':
                north()
                break       
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items)
        else:
            print("Sorry, you cannot do that here.")

def northWest():
    map['Northwest'] = 'Dense Jungle'
    print("\n" * 20)
    print("Hacking through thick, dense undergrowth, you find yourself in a dense jungle.")
    print("\tYou cannot see the sky. \n\tThe only path leads back east.")
    items = 'Gillyweed'
    itemText = "Nestled behind a fallen log, you find a patch of Gillyweed!\n"
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'east':
                north()
                break         
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items) # FIX THIS LATER
        else:
            print("Sorry, you cannot do that here.")

def northEast():
    map['Northeast'] = 'Light Jungle'
    print("\n" * 20)
    print("The mountain pass begins to clear, you find yourself overlooking a sunny jungle.")
    print("\tIt is hot. \n\tThe only path leads back west.")
    items = 'Ammo'
    itemText = "Someone has dropped Ammo here!\n"
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'west':
                north()
                break         
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items) # FIX THIS LATER
        else:
            print("Sorry, you cannot do that here.")

def west():
    map['West'] = 'Sunny Beach'
    print("\n" * 20)
    print("Leaving the ship, you walk along the beach.")
    print("\tIt is a beautiful day. \n\tThe only path leads back east to the ship.")
    items = 'Pulse Crystal'
    itemText = "Half buried under the sand, you find a single Pulse Crystal! \nThere must be more around here, but where?\n"
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'east':
                ship()
                break         
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items) # FIX THIS LATER
        else:
            print("Sorry, you cannot do that here.")

def east():
    map['East'] = 'Damp Woods'
    print("\n" * 20)
    print("Leaving the ship, you follow the path into the woods.")
    print("\tIt is misty. \n\tThe only path leads back east to the ship.")
    items = 'Backpack'
    itemText = "Under some leaves, you find the remains of an old leather backpack!"
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'west':
                ship()
                break         
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items) # FIX THIS LATER
        else:
            print("Sorry, you cannot do that here.")


def south():
    map['South'] = 'Ocean'
    print("\n" * 20)
    if 'Gillyweed' in supplies:
        print("You chew the gillyweed, and can now breath underwater! \nYou step beneath the waves. \nLights dance around you, and seaweed drifts by. \nYou can move to the west or the east.")
    else:
        print("You march south until your feet hit the waves of a vast ocean. \nYou can't go any further. \nYou return to the ship.")
        print("Hit RETURN to continue.")
        input("> ")
        ship()
    items = None 
    itemText = "Nothing of value is found here."
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'west':
                southWest()
                break         
            elif direction == 'east':
                southEast()
                break
            elif direction == 'north':
                ship()
                break
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items) # FIX THIS LATER
        else:
            print("Sorry, you cannot do that here.")

def southEast():
    map['Southeast'] = 'Evil Ocean Cave'
    print("\n" * 20)
    print("You are attacked by a vicious sea monster! \nIt has horrible teeth and nasty fangs! \aIt looks like Leonard Nimoy on Acid!")
    fight(cthulu)
    items = None 
    itemText = "Nothing of value is found here."
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()
            if direction == 'west':
                southWest()
                break         
            elif direction == 'east':
                southEast()
                break
            elif direction == 'north':
                ship()
                break
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items) # FIX THIS LATER
        else:
            print("Sorry, you cannot do that here.")

def southWest():
    map['Southwest'] = 'Shallow Ocean Floor'
    print("\n" * 20)
    print("You walk along the bottom of the ocean. \nAncient shipwrecks around you, you see the distant lights above you. \nThe only way to go is back east.")
    items = 'Food'
    itemText = "You find a hamburger! It's like perfect!"
    while True:
        print("What would you like to do?")
        choice = input("> ")
        choice = choice.lower()
        if choice == "help":
            print("""You may do the following:
            travel
            supplies
            search
            eat
            map""")
        elif choice == "eat":
            try:
                supplies.remove('Food')
                health += 10
            except:
                print("You are out of food!")
        elif choice == "travel":
            print("Where would you like to go?")
            direction = input("> ")
            direction = direction.lower()         
            if direction == 'east':
                south()
                break
            elif direction == 'home':
                if health <= 50:
                    dead("You collapse from exhaustion on the way home.")
                else:
                    ship()
                    break
            else:
                print("You cannot go that way.")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == "search":
            print(itemText)
            supplies.append(items) # FIX THIS LATER
        else:
            print("Sorry, you cannot do that here.")

def dead(why):
    print("\n" * 30)
    print(why)
    print("You lose! Haha!")
    exit(0)

def workshop():
    print("Hi! This is the workshop!")
    print("You have no idea what you're doing, do you?")
    dead("You trip and impale yourself on a workbench.")

def fight(monster):
    print("FIGHT SEQUENCE")
    print(f"The monster's HP is: {monster}")
    print(f"Your health is at: {health}")
    print("This doesn't end well for you.")
    print("Hit RETURN to continue.")
    input("> ")
    dead("You have been killed to death!")

    if health <= 0:
        dead("You have been killed to death!")

health = 100
map = {'North': '?', 'Far North': '?', 'Northwest': '?', 'Northeast': "?", 'West': '?', 'East': '?', 'South': 'ocean', 'Southwest': '?', 'Southeast': '?'}
food = 10
supplies = ['Food', 'Food', 'Food', 'Food', 'Ammo', 'Ammo']
cthulu = 500

start()
ship()
