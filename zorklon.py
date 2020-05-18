"""Still to do:

backpack?
restrict travel to the south
write a finish
fix 'run' mechanic in fights

tweaks:
balance food scarcity
balance monster strength
format to look nice

"""

import random

cthulhu = ['Cthulhu', 300, 15]
snake = ['Snekky Snek', 40, 5]
shroom = ['Angry Mushroom', 100, 10]

north = {
    'north': 1,
    'south': 6,
    'east': 4,
    'west': 2,
    'mapname': 'North',
    'mapDescript': 'Mountain Foothills',
    'aText': "After a day of travel, you find yourself in the mountains.",
    'aText2': "\tThe sky is grey and threatening. \n\tThere is a winding path to the west, \n\ta jagged path up the mountain to the north, \n\tand another rocky path to the east.",
    'items': 'raw vegetables'
}

farnorth = {
    'south': 3,
    'mapname': 'Far North',
    'mapDescript': 'Craggy Mountains',
    'aText': "You find yourself high in the mountains.",
    'aText2': "\tThe air is thin. \nThere are no plants, just rock and wind for miles.",
    'items': 'metal ore'
}

northeast = {
    'west': 3,
    'mapname': 'Northeast',
    'mapDescript': 'Light Jungle',
    'aText': "The mountain pass begins to clear, you find yourself overlooking a sunny jungle.",
    'aText2': "\tIt is hot. \n\tThe only path leads back west.",
    'items': 'flint'    
}

northwest = {
    'east': 3,
    'mapname': 'Northwest',
    'mapDescript': 'Dense Jungle',
    'aText': "Hacking through thick, dense undergrowth, you find yourself in a dense jungle.",
    'aText2': "\tYou cannot see the sky. \n\tThe only path leads back east.",
    'items': 'gillyweed',
    'monster': shroom
}

ship = {
    'north': 3,
    'east': 7,
    'west': 5,
    'south': 9,
    'mapname': 'Ship',
    'mapDescript': 'A wrecked spaceship',
    'aText': "You are on your ship. It is safe here.",
    'aText2': "After a night of rest, you feel refreshed. \nHealth at 100%"
}

east = {
    'west': 6,
    'mapname': 'East',
    'mapDescript': 'Damp Woods',
    'aText': "Leaving the ship, you follow the path into the woods.",
    'aText2': "\tIt is misty. \n\tThe only path leads back west to the ship.",
    'items': 'Backpack',
    'monster': snake
}

west = {
    'east': 6,
    'mapname': 'West',
    'mapDescript': 'Sunny Beach',
    'aText': "Leaving the ship, you walk along the beach.",
    'aText2': "\tIt is a beautiful day. \n\tThe only path leads back east to the ship.",
    'items': 'Pulse Crystal'    
}

south = {
    'north': 6,
    'east': 10,
    'west': 8,
    'mapname': 'South',
    'mapDescript': 'Ocean',
    'aText': "You attach the breather, allowing you to breathe underwater!",
    'aText2': "You step beneath the waves. You can travel east or west.",   
}

southeast = {
    'west': 9,
    'mapname': 'Southeast',
    'mapDescript': 'Evil Ocean Cave',
    'aText': "You step deeper and deeper into the dark waters. You find the entrance of an underwater cave.",
    'aText2': "You are attacked by a vicious sea monster! \nIt has horrible teeth and nasty fangs! \aIt looks like Leonard Nimoy on Acid!",
    'items': 'Pulse Crystal',  
    'monster': cthulhu
}

southwest = {
    'east': 9,
    'mapname': 'Southwest',
    'mapDescript': 'Shallow Ocean Floor',
    'aText': "You walk along the bottom of the ocean.",
    'aText2': "Ancient shipwrecks around you, you see the distant lights above you. \nThe only way to go is back east.",
    'items': 'raw vegetables'  
}

locations = {
    1: farnorth,
    2: northwest,
    3: north,
    4: northeast,
    5: west,
    6: ship,
    7: east,
    8: southwest,
    9: south,
    10: southeast
}

def start():
    """Commences the game."""
    print("\n" * 10)
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

def myTurn():
    global health
    while True:
        print("What would you like to do? Type H for help.")
        choice = input("> ")
        choice = choice.lower()
        
        if choice == 'h':
            print("""You may do the following:
            travel
            supplies
            search
            check health
            eat
            map
            workshop""")
        elif choice == 'travel':
            travel()
            break
        elif choice == "supplies":
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == 'search':
            if 'items' in myLocation:
                print(f"You found {myLocation['items']}!")
                supplies.append(myLocation['items'])
                del myLocation['items']
            else:
                print("There is nothing of significance here.")
        elif choice == 'check health':
            print(f"Your health is currently at {health}")
        elif choice == 'eat':
            eat()
        elif choice == 'workshop':
            if myLocation == ship:
                workshop()
                break
            else: 
                print("You can only do this at the ship!")
        elif choice == "map":
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        else:
            print("Sorry, you cannot do that here.")
        
def travel():
    global health
    while True:
        print("Which direction would you like to go?")
        direction = input("> ")
        direction = direction.lower()
        if direction in myLocation:
            destinationIndex = myLocation[direction]
            destination = locations[destinationIndex]
            arrive(destination)
        elif direction == 'home':
            if health <= 20:
                dead("On the way home, you collapse from exhaustion.")
            else:
                arrive(ship)
        else:
            print("Sorry, you cannot travel that direction from here.")

def arrive(newLocation):
    global myLocation
    global health
    health -= 10
    if health <= 0:
        dead("You collapse from exhaustion.")
    myLocation = newLocation
    map[newLocation['mapname']] = newLocation['mapDescript']
    if newLocation == ship:
        health = 100
    if 'monster' in newLocation:
        fight(newLocation['monster'])
        del newLocation['monster']
    print("\n" * 20)
    print(newLocation['aText'])
    print(newLocation['aText2'])
    myTurn()

def fight(baddie):
    global health
    hit = 10
    if 'spear' in supplies:
        hit = 20

    if 'blade' in supplies:
        hit = 40
    print("\n" * 20)
    print(f"You are attacked by a {baddie[0]}!")

    while True:
        if health <= 0:
            dead("You just got dieded!")

        # player's turn
        while True:
            print("\n")
            print(f"your health: {health}")
            print(f"baddie's health: {baddie[1]}")
            print("What do you do? Type H for help.")
            choice = input("> ")
            choice = choice.lower()
            if choice == "h":
                print("""You may do the following:
                Run
                Attack
                Eat""")
            elif choice == 'eat':
                eat()
                break
            elif choice == 'attack':
                myAttack = random.randint(1,21)
                print("\n" * 20)
                if myAttack >= 19:
                    print(f"CRITICAL HIT! \nYou have badly wounded the {baddie[0]}!\n")
                    baddie[1] -= (hit * 2)
                    break
                elif myAttack >= 4:
                    print(f"You have wounded the {baddie[0]}!\n")
                    baddie[1] -= hit
                    break
                else:
                    print("Your attack missed!\n")
                    break
#            elif choice == 'run':
#                arrive(ship)
#                break
            else:
                print("Sorry, you can't do that now!")
        
        if baddie[1] <= 0:
            print(f"You have defeated the {baddie[0]}!\n")
            print("Hit RETURN to continue.")
            input("> ")
            break
        
        # baddie's turn
        print(f"The {baddie[0]} attacks!")
        baddieAttack = random.randint(0,20)
        if baddieAttack >= 18:
            print("CRITICAL HIT!\n")
            health -= (baddie[2] * 2)
        elif baddieAttack >= 8:
            print("You are hit!\n")
            health -= baddie[2]
        else:
            print(f"The {baddie[0]} misses!")

def eat():
    global health
    print("\n" *20)
    if 'food' in supplies:
        print("You eat the food and feel much better!")
        health += 25
        if health >= 100:
            health = 100
        print(f"Your health is now at {health}.\n")
        supplies.remove('food')
    else:
        print("You have no food to eat!\n")

def workshop():
    global supplies
    print("You have the following to work from:")
    for n in supplies:
        print(n)
    print("What would you like to work with?")
    workWith = input("> ")
    workWith = workWith.lower()
    if workWith not in supplies:
        print("Sorry, you don't have that with you.")
        workshop()
    
    if workWith == 'gillyweed':
        print("""You set to work on the gillyweed. 
        After several hours, you emerge with a breather.""")
        supplies.remove('gillyweed')
        supplies.append('breather')
    elif workWith == 'raw vegetables':
        print("""
        You set to work on the raw vegetables.
        After several hours, you emerge with three pieces of food.""")
        supplies.remove('raw vegetables')
        supplies.append('food')
        supplies.append('food')
        supplies.append('food')
    elif workWith == "flint":
        print("""
        You set to work on the flint.
        After several hours, you emerge with a spear.""")
        supplies.remove('flint')
        supplies.append('spear')
        if 'blade' in supplies:
            print("""
            \nAfter consideration, you realize that it isn't as strong as your blade.)
            You leave it here.""")
            supplies.remove('spear')
    elif workWith == 'metal ore':
        print("""
        You set to work with the metal ore.
        After several hours, you emerge with a blade.""")
        supplies.remove('metal ore')
        supplies.append('blade')
        if 'spear' in supplies:
            supplies.remove('spear')


    print("\n"*3)
    myTurn()

def pickup(item):
    global supplies
    if backpack not in supplies:
        if len(supplies) >= 8:
            print("Sorry, you cannot carry more than 8 things!")
        else:
            print(f"You've added ${item} to your supplies!")
            supplies.append(item)
    else:
        print(f"You've added ${item} to your supplies!")
        supplies.append(item)

def dead(reason):
    print(reason)
    print("You died! Haha loser")
    exit(0)

health = 100
map = {'North': '?', 'Far North': '?', 'Northwest': '?', 'Northeast': "?", 'West': '?', 'East': '?', 'South': '?', 'Southwest': '?', 'Southeast': '?'}
supplies = ['food', 'food', 'food']
myLocation = ship

start()
myTurn()