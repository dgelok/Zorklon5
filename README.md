# Hero RPG!

Zorklon5 (heroRPG.py) is a python-based RPG to be run on the command line. It was my first "big" self-developed project. 


## Developed by

Dan Gelok

[email me](dgelok@gmail.com) / [github](https://github.com/dgelok)


## Requirements

- Python3 or later (built on Python3.8)
- random module


## To run

- On Mac Terminal: `python3 zorklon.py`
- On Windows Command Line: `python zorklon.py`


## Similar projects

I've designed two more text-based RPG games that are similar in concept; [heroRPG](https://github.com/dgelok/heroRPG) and [Pyramid_Game](https://github.com/dgelok/pyramidGame). Both utilize OOP principles, but heroRPG is significantly larger, and was made as part of DigitalCrafts curriculum (June 2020 Houston cohort).

Zorklon5.py was designed to develop my coding skills across a larger project. At the time of development, I did not know how to properly utilize classes or import other modules. It was started largely thanks to the help of Zed Shaw's excellent book, *Learn Python the Hard Way* (available [here](https://www.amazon.com/Learn-Python-Hard-Way-Introduction/dp/0134692888/ref=sr_1_1?keywords=python+the+hard+way&qid=1577465107&sr=8-1)).


## How it works

| Feature | Description |
| ----------- | ----------- |
| Locations | Zorklon5 involves traveling to and interacting with locations. Locations are dictionaries, each containing visual descriptions, interactive text, items, enemies, and references to other locations that you can travel to from here. The map is laid out in a 9X9 grid with an extra location at the far north. |
| Items | Items are appended to a list of supplies and can be used in various ways. Most items found must be worked with in the workshop() function in order to be usable. Each item found can be transformed into a useful tool (like weapons or an underwater breathing apparatus) or food. The game cannot advance without developing items, which in turn are used to develop other items. Items are distributed around the map. Once an item is observed, it is appended to the player's supplies and does not regenerate.|
| Fights | Since enemies are present, each enemy (stored as a list) is given attack power and hit points, and left in various locations around the map. Once an enemy is defeated, it is removed from the map. The fight() function is a while loop that passes a baddie as an argument and prompts the user for choices in battle; run, attack, or eat to regain health.|
| Eating | The player's health diminishes in several ways; they can be attacked or lose strength by traveling. If the player takes too much damage from an enemy or moves around too much without returning to the ship (home base), they will die. Eating food regenerates health, but it also diminishes supplies.|
| Dying or Winning | If a player runs out of health completely, they die and the game exits. Similarly, if you defeat the final boss and gain the final item needed to complete the game, a final() function executes and ends the program successfully.|


## Current bugs and possible additional developments

- Visual cleanup to make the game easier to follow for the user
- Add a backpack mechanic to limit how many supplies one can carry
