"""
Do not remove this file. Ensure your main function is in this file.

I will execute your game like this:

python3 game.py

Yes, you may add additional files to this folder.
"""
import itertools
import random
import text
import time


def make_board(rows: int, columns: int) -> dict:
    """Create a dictionary containing a set of coordinates for the playing space.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows >= 2
    :precondition: columns >= 2
    :postcondition: function creates a dictionary that contains rows * columns key/value pairs
    :postcondition: function creates a dictionary where each key is a tuple that contains a set of coordinates
    :postcondition: function creates a dictionary where each value is a short string description
    :postcondition: in the dictionary, the short string description in each value is randomly chosen from a
                    predetermined tuple
    :return: a dictionary
    """

    world_map = {(column, row): f"{random.choice(text.area_description_beginning)}"
                                f"{random.choice(text.area_description_middle)}"
                                f"{random.choice(text.area_description_end)}"
                 for column in range(columns) for row in range(rows)}

    return world_map


def describe_current_location(board_dictionary: dict, character_dictionary: dict):
    """Retrieve description of the room located in the character's coordinates.

    Print the description onto the terminal.

    :param board_dictionary: a dictionary
    :param character_dictionary: a dictionary
    :precondition: board_dictionary is a dictionary where each key is a coordinate and each value is a description of
    the area
    :precondition: character_dictionary is a dictionary containing vital information about the character
    :postcondition: board_dictionary is not modified in the function
    :postcondition: character_dictionary is not modified in the function
    :postcondition: function prints the description of the room located in the character's coordinates

     >>> board = {(0, 0): "Empty room", (0, 1): "Room with a cozy fireplace", (1, 0): "Room containing a rusty car",
     ... (1, 1): "Room filled completely with random items"}
     >>> character = {'X-coordinate': 0, 'Y-coordinate': 1}
     >>> describe_current_location(board, character)
     Area description: Room with a cozy fireplace
    """

    current_coordinate = (character_dictionary['X-coordinate'], character_dictionary['Y-coordinate'])
    sentinel_value = False

    while not sentinel_value:
        for key, value in board_dictionary.items():
            if key == current_coordinate:
                print(f"Area description: {value}")
                sentinel_value = True


def get_user_direction_choice():
    """Obtain the user's choice for which direction they want to go.

    Function prints a numbered list of directions then asks the user to enter the direction they wish to travel.

    :postcondition: function asks the player which cardinal direction they want to travel via a print statement
    :postcondition: if the player inputs a number not in the range [1, 4], the function
     will keep asking the user for input
    :postcondition: if the player inputs the integer 1, then the direction is North
    :postcondition: if the player inputs the integer 2, then the direction is East
    :postcondition: if the player inputs the integer 3, then the direction is South
    :postcondition: if the player inputs the integer 4, then the direction is West
    :return: a string containing a number corresponding to the direction that the user wants to go
    """

    direction_choices = ['North', 'East', 'South', 'West']
    print("Please enter a number between 1 - 4 representing the direction that you wish to travel: ")
    user_direction_choice = get_user_choice(direction_choices)

    return user_direction_choice


def get_user_choice_string(choice_list: list):
    r"""Loop through each element in choice list and append its index and the element in a string.

    :param choice_list: a list
    :precondition: choice_list must be a list containing the choices for the user in string format
    :postcondition: the range of possible inputs is [1, len(choice_list) + 2]
    :postcondition: choice_list is not modified
    :return: a string containing the index and choices one after another

    >>> direction_choice_list = ['North', "East", "South", "West"]
    >>> get_user_choice_string(direction_choice_list)
    '\t[1] North\n\t[2] East\n\t[3] South\n\t[4] West\n\t[q/Q] Quit\n'
    """

    input_string = ""
    index = itertools.count(1)

    for choice in choice_list:
        input_string += f"\t[{next(index)}] {choice}\n"

    input_string += "\t[q/Q] Quit\n"

    return input_string


def get_user_choice(choice_list: list):
    """Obtain users choice in integer form when the user is asked for input.

    A reusable function that outputs a numbered list of choices which the user will input.

    :param choice_list: a list
    :precondition: choice_list must be a list containing the choices for the user in string format
    :postcondition: the range of possible inputs is [1, len(choice_list) + 2]
    :postcondition: if the user inputs 'q' or 'Q', a thank-you message is printed to the console then the program ends
    :return: a string containing the user's choice
    """
    correct_input = False
    user_choice_integer = 0

    while not correct_input:
        user_choice_integer = input(get_user_choice_string(choice_list))

        if user_choice_integer in ['q', 'Q']:
            print("Thanks for playing the game!")
            exit()

        try:
            if int(user_choice_integer) in list(range(1, len(choice_list) + 1)):
                correct_input = True
        except ValueError:
            print("Invalid input. Please try again.")

    return user_choice_integer


def validate_move(rows: int, columns: int, character_dictionary: dict, direction_string: str) -> bool:
    """Determine whether the player will cross the boundaries of the game board.

    Function determines where the player is located on the board and whether they can travel to the intended direction.

    :param rows: an integer
    :param columns: an integer
    :param character_dictionary: a dictionary
    :param direction_string: a string
    :precondition: rows >= 2
    :precondition: columns >= 2
    :precondition: character_dictionary is a dictionary containing vital information about the character
    :precondition: direction_string is a string that contains either "1", "2", "3" or "4"
    :postcondition: rows is not modified
    :postcondition: columns is not modified
    :postcondition: character_dictionary is not modified
    :postcondition: direction_string is not modified
    :return: a boolean value, True or False; if the direction the player wants to travel is outside the game board
    boundary, return False, else return True

    >>> validate_move(2, 2, {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}, "3")
    True
    """

    max_coordinate = (rows - 1, columns - 1)
    current_coordinate = (character_dictionary['X-coordinate'], character_dictionary['Y-coordinate'])
    next_coordinate = ()

    if direction_string == "1":  # Travel North
        next_coordinate = (current_coordinate[0], current_coordinate[1] - 1)
    elif direction_string == "2":  # Travel East
        next_coordinate = (current_coordinate[0] + 1, current_coordinate[1])
    elif direction_string == "3":  # Travel South
        next_coordinate = (current_coordinate[0], current_coordinate[1] + 1)
    elif direction_string == "4":  # Travel West
        next_coordinate = (current_coordinate[0] - 1, current_coordinate[1])

    return not (next_coordinate[0] > max_coordinate[0] or next_coordinate[1] > max_coordinate[1] or
                next_coordinate[0] < 0 or next_coordinate[1] < 0)


def move_character(character_dictionary: dict, direction_string: str):
    """Update the character's X and Y coordinates according to the direction.

    :param character_dictionary: a dictionary
    :param direction_string: a string
    :precondition: character_dictionary is a dictionary containing vital information about the character
    :precondition: direction_string is a string that contains either "1", "2", "3" or "4"
    :postcondition: character_dictionary is modified in the function
    """

    if direction_string == "1":  # North
        character_dictionary["Y-coordinate"] -= 1
    elif direction_string == "2":  # East
        character_dictionary["X-coordinate"] += 1
    elif direction_string == "3":  # South
        character_dictionary["Y-coordinate"] += 1
    elif direction_string == "4":  # West
        character_dictionary["X-coordinate"] -= 1


def check_if_goal_attained(rows: int, columns: int, character_dictionary: dict) -> bool:
    """Determine whether the player has reached the bottom right-hand corner of the board.

    :param rows: an integer
    :param columns: an integer
    :param character_dictionary: a dictionary
    :precondition: rows >= 2
    :precondition: columns >= 2
    :precondition: character_dictionary is a dictionary containing vital information about the character
    :postcondition: character_dictionary is not modified
    :postcondition: rows is not modified
    :postcondition: columns is not modified
    :return: a boolean value; True if player has reached the bottom right-hand corner of the board, otherwise False is
    returned

    >>> character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> check_if_goal_attained(2, 2, character)
    True
    """

    max_coordinate = (rows - 1, columns - 1)
    current_coordinate = (character_dictionary['X-coordinate'], character_dictionary['Y-coordinate'])

    return is_alive(character_dictionary) and max_coordinate == current_coordinate


def percent_chance(decimal_form_percentage: float) -> float:
    """Determine whether the player has encountered a foe.

    Function ensures that the player encounters a foe 20% of the time.

    :param decimal_form_percentage: a float
    :precondition: decimal_form_percentage is a percentage value in decimal form;
                   for example, 65% is 0.65 in decimal_form_percentage
    :return: a boolean value, True or False; if there is a foe, return True, else, return False
    """

    return random.random() < decimal_form_percentage


def make_enemy(character_dictionary: dict):
    """Create an enemy according to the player's level.

    :param character_dictionary: a dictionary containing vital information about the character
    :postcondition: if character_dictionary['level'] == 1, a random function from [make_evil_fairy, make_wraith,
                    make_bandit, make_panda] is called
    :postcondition: if character_dictionary['level'] == 2, a random function from [make_golem, make_dragon, \
                    make_ghost_pirate, make_ai_droid] is called
    :return: a function
    """

    def filter_level_one_enemies(enemy_function):
        """Filter level one enemies from enemy_functions.

        :param enemy_function: a function
        :postcondition: only functions that make level one enemies will be filtered out
        return: a function
        """
        return True if enemy_function in [make_evil_fairy, make_wraith, make_bandit, make_panda] else False

    def filter_level_two_enemies(enemy_function):
        """Filter level two enemies from enemy_functions.

        :param enemy_function: a function
        :postcondition: only functions that make level two enemies will be filtered out
        return: a function
        """
        return True if enemy_function in [make_golem, make_dragon, make_ghost_pirate, make_ai_droid] else False

    enemy_functions = [make_evil_fairy, make_wraith, make_bandit, make_panda,
                       make_golem, make_dragon, make_ghost_pirate, make_ai_droid]

    filtered_enemy_functions = filter(filter_level_one_enemies, enemy_functions) \
        if character_dictionary['level'] == 1 else filter(filter_level_two_enemies, enemy_functions)

    return random.choice(list(filtered_enemy_functions))()


def make_evil_fairy() -> dict:
    """Create a dictionary containing vital information about the Evil Fairy.

    :postcondition: function creates a dictionary containing Evil Fairy data
    :return: a dictionary
    """

    return {
        'name': 'Evil Fairy',
        'enemy_description': text.evil_fairy_description,
        'Current HP': 50,
        'Max HP': 50,
        'attack_stat': 10,
        'defense_stat': 5,
        'skills': ['Fairy Wind',
                   'Fleur Cannon',
                   'Misty Explosion'],
        'level': 1,
        'percent_accuracy': 0.50
    }


def make_wraith() -> dict:
    """Create a dictionary containing vital information about the Wraith.

    :postcondition: function creates a dictionary containing Wraith data
    :return: a dictionary

    """

    return {
        'name': 'Wraith',
        'enemy_description': text.wraith_description,
        'Current HP': 50,
        'Max HP': 50,
        'attack_stat': 10,
        'defense_stat': 5,
        'skills': ['Soul Sucker',
                   'Spirit Strike',
                   'Chilling Scream'],
        'level': 1,
        'percent_accuracy': 0.50
    }


def make_bandit() -> dict:
    """Create a dictionary containing vital information about the Bandit.

    :postcondition: function creates a dictionary containing Bandit data
    :return: a dictionary
    """

    return {
        'name': 'Bandit',
        'enemy_description': text.bandit_description,
        'Current HP': 50,
        'Max HP': 50,
        'attack_stat': 5,
        'defense_stat': 10,
        'skills': ['Back Stab',
                   'Rifle Blast',
                   'Shotgun Burst'],
        'level': 1,
        'percent_accuracy': 0.50
    }


def make_panda() -> dict:
    """Create a dictionary containing vital information about the Panda.

    :postcondition: function creates a dictionary containing Panda data
    :return: a dictionary
    """

    return {
        'name': 'Panda',
        'enemy_description': text.panda_description,
        'Current HP': 50,
        'Max HP': 50,
        'attack_stat': 7,
        'defense_stat': 8,
        'skills': ['Karate Chop',
                   'One Inch Punch',
                   'Roundhouse Kick'],
        'level': 1,
        'percent_accuracy': 0.50
    }


def make_golem() -> dict:
    """Create a dictionary containing vital information about the Golem.

    :postcondition: function creates a dictionary containing Golem data
    :return: a dictionary
    """

    return {
        'name': 'Golem',
        'enemy_description': text.golem_description,
        'Current HP': 100,
        'Max HP': 100,
        'attack_stat': 10,
        'defense_stat': 20,
        'skills': ['Rock Throw',
                   'Earthquake',
                   'Mud Slap'],
        'level': 2,
        'percent_accuracy': 0.50
    }


def make_dragon() -> dict:
    """Create a dictionary containing vital information about the Dragon.

    :postcondition: function creates a dictionary containing Dragon data
    :return: a dictionary
    """

    return {
        'name': 'Dragon',
        'enemy_description': text.dragon_description,
        'Current HP': 100,
        'Max HP': 100,
        'attack_stat': 15,
        'defense_stat': 15,
        'skills': ['Dragons Breathe',
                   'Tail Whip',
                   'Bite'],
        'level': 2,
        'percent_accuracy': 0.50
    }


def make_ghost_pirate() -> dict:
    """Create a dictionary containing vital information about the Ghost Pirate.

    :postcondition: function creates a dictionary containing Ghost Pirate data
    :return: a dictionary
    """

    return {
        'name': 'Ghost Pirate',
        'enemy_description': text.ghost_pirate_description,
        'Current HP': 100,
        'Max HP': 100,
        'attack_stat': 20,
        'defense_stat': 10,
        'skills': ['Pistol Whip',
                   'Snipe',
                   'Somersault Kick'],
        'level': 2,
        'percent_accuracy': 0.50
    }


def make_ai_droid() -> dict:
    """Create a dictionary containing vital information about the AI Droid.

    :postcondition: function creates a dictionary containing AI Droid data
    :return: a dictionary
    """

    return {
        'name': 'AI Droid',
        'enemy_description': text.ai_droid_description,
        'Current HP': 100,
        'Max HP': 100,
        'attack_stat': 10,
        'defense_stat': 20,
        'skills': ['Punch',
                   'Kick',
                   'Outsmart'],
        'level': 2,
        'percent_accuracy': 0.50
    }


def make_boss() -> dict:
    """Create a dictionary containing vital information about the Nameless King.

    :postcondition: function creates a dictionary containing Nameless King data
    :return: a dictionary
    """

    return {
        'name': 'The Nameless King',
        'enemy_description': text.boss_description,
        'Current HP': 300,
        'Max HP': 300,
        'attack_stat': 40,
        'defense_stat': 40,
        'skills': ['Electrified Spear Strike',
                   'Dragons Breath',
                   'Dragon Barrage',
                   'Giant Stomp'],
        'level': 3,
        'percent_accuracy': 0.50
    }


def is_alive(character_dictionary: dict) -> bool:
    """Determines whether the player is still alive.

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary with the format
    {'X-coordinate': Int, 'Y-coordinate': Int, 'Current HP': Int} where Int is an integer
    :postcondition: character_dictionary is not modified
    :return: a boolean value, True or False; if character_dictionary['Current HP'] == 0, return False, else, return True

    >>> is_alive({'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5})
    True
    """

    return not character_dictionary['Current HP'] == 0


def display_map(rows: int, columns: int, character_dictionary: dict):
    """Display player location on the board using ASCII art.

    :param rows: an integer
    :param columns: an integer
    :param character_dictionary: a dictionary
    :precondition: rows >= 2
    :precondition: columns >= 2
    :precondition: character_dictionary is a dictionary with the format
    {'X-coordinate': Int, 'Y-coordinate': Int, 'Current HP': Int} where Int is an integer
    :postcondition: character_dictionary is not modified
    :postcondition: location of player is marked with "X"

    >>> character = {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5}
    >>> display_map(3, 3, character)
    [X] [ ] [ ]
    [ ] [ ] [ ]
    [ ] [ ] [B]
    """

    current_coordinate = (character_dictionary['X-coordinate'], character_dictionary['Y-coordinate'])

    for row in range(rows):
        for column in range(columns):
            if current_coordinate == (column, row) and column < columns - 1:
                print("[X] ", end="")
            elif current_coordinate == (column, row) and column == columns - 1:
                print("[X]", end="")
            elif (column, row) == (columns - 1, rows - 1):
                print("[B]", end="")
            elif current_coordinate != (column, row) and column < columns - 1:
                print("[ ] ", end="")
            else:
                print("[ ]", end="")
        print()


def get_character_class():
    """Request user for their character's class.

    :return: a string containing an integer
    """

    mage_description = text.mage_description
    ninja_description = text.ninja_description
    warrior_description = text.warrior_description
    archer_description = text.archer_description

    class_choices = [mage_description, ninja_description, warrior_description, archer_description]
    print("Please enter a number between 1 - 4 representing the class that you wish to play: ")
    user_class_choice = get_user_choice(class_choices)

    return user_class_choice


def make_mage(name: str) -> dict:
    """Create a dictionary containing vital information about the mage class.

    :postcondition: function creates a dictionary containing mage class data
    :return: a dictionary
    """

    return {'name': name, 'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 70, 'Current HP': 70,
            'character_class': 'Mage', 'attack_stat': 50, 'defense_stat': 10,
            'skills': ['Blizzard', 'Flame Strike', 'Water Prison'], 'level': 1,
            'level_up_exp': 50, 'current_exp': 0, 'ranks': ['Initiate', 'Adept', 'Grand Master'],
            'percent_accuracy': 0.40}


def make_ninja(name: str) -> dict:
    """Create a dictionary containing vital information about the ninja class.

    :postcondition: function creates a dictionary containing ninja class data
    :return: a dictionary
    """

    return {'name': name, 'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 150, 'Current HP': 150,
            'character_class': 'Ninja', 'attack_stat': 20, 'defense_stat': 20,
            'skills': ['Shuriken Throw', 'Dagger Strike', 'Assassinate'], 'level': 1,
            'level_up_exp': 50, 'current_exp': 0, 'ranks': ['Genin', 'Chunin', 'Jonin'], 'percent_accuracy': 0.95}


def make_warrior(name: str) -> dict:
    """Create a dictionary containing vital information about the warrior class.

    :postcondition: function creates a dictionary containing warrior class data
    :return: a dictionary
    """

    return {'name': name, 'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 200, 'Current HP': 200,
            'character_class': 'Warrior', 'attack_stat': 30, 'defense_stat': 30,
            'skills': ['Execute', 'Heroic Strike', 'Charge'],
            'level': 1, 'level_up_exp': 50, 'current_exp': 0, 'ranks': ['Fighter', 'Hero', 'Dark Knight'],
            'percent_accuracy': 0.70}


def make_archer(name: str) -> dict:
    """Create a dictionary containing vital information about the archer class.

    :postcondition: function creates a dictionary containing archer class data
    :return: a dictionary
    """

    return {'name': name, 'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 100, 'Current HP': 100,
            'character_class': 'Archer', 'attack_stat': 25, 'defense_stat': 15,
            'skills': ['Rapid Fire', 'Poison Arrow', 'Penetrating Arrow'],
            'level': 1, 'level_up_exp': 50, 'current_exp': 0, 'ranks': ['Hunter', 'Ranger', 'Bow Master'],
            'percent_accuracy': 0.90}


def make_character():
    """Create a dictionary containing vital information about the player.

    :postcondition: function creates a dictionary containing character data
    :return: a dictionary
    """

    character_name = input("Please enter your character's name below: \n")
    character_class_input = int(get_character_class())
    make_class_function_list = [make_mage, make_ninja, make_warrior, make_archer]
    for index, make_class_function in enumerate(make_class_function_list):
        if character_class_input == index + 1:
            return make_class_function(character_name)


def attack_the_defender(attacker_dictionary: dict, defender_dictionary: dict, attack_skill: str):
    """Decrease the defenders HP.

    :param attacker_dictionary: a dictionary
    :param defender_dictionary: a dictionary
    :param attack_skill: a string
    :precondition: attacker_dictionary is a dictionary containing vital information about the attacker
    :precondition: defender-dictionary is a dictionary containing vital information about the defender
    :precondition: attack_skill is a string containing the skill used by the attacker
    :postcondition: if percent_chance == True, defender dictionary is modified else defender_dictionary is not modified
    :postcondition: if percent_chance == True, the amount of HP defender lost is printed to console, else function
                    prints to the console that the attack did not hit
    """

    attack_defense_difference = attacker_dictionary['attack_stat'] - defender_dictionary['defense_stat']
    decrement_value = attack_defense_difference if attack_defense_difference > 0 else 0
    base_attack_decrement = 10
    damage_taken = decrement_value + base_attack_decrement

    if percent_chance(attacker_dictionary['percent_accuracy']):
        defender_dictionary['Current HP'] -= damage_taken
        print(f"{attack_skill} hit {defender_dictionary['name']}")
        print(f"{defender_dictionary['name']} lost {damage_taken} HP!\n")
        if defender_dictionary['Current HP'] < 0:
            defender_dictionary['Current HP'] = 0
    else:
        print(f"{attack_skill} did not hit. No damage taken.\n")


# This function has already been tested in test_get_user_choice.py
def get_user_pre_combat_choice() -> str:
    """Get the user's decision on what they want to do in that round of combat.

    :return: a string containing an integer
    """

    print('Please enter a number between 1 - 4 which corresponds to what you want to do this round.')
    pre_combat_choices = ['Enemy Description', 'Attack', 'Heal', 'Flee']

    return get_user_choice(pre_combat_choices)


def get_random_enemy_skill(enemy_dictionary: dict) -> str:
    """Gets a random enemy skill from enemy_dictionary['skills'].

    :param enemy_dictionary: a dictionary
    :precondition: enemy_dictionary is a dictionary containing vital information about the enemy
    :postcondition: function randomly gets a skill from enemy_dictionary['skills']
    :return: a string
    """
    return random.choice(enemy_dictionary['skills'])


def get_user_attack_skill_choice(character_dictionary: dict, enemy_dictionary: dict):
    """Get the user's decision on what attack they want to use.

    :param character_dictionary: a dictionary
    :param enemy_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary containing vital information about the character
    :precondition: enemy_dictionary is a dictionary containing vital information about the enemy
    :return: a string containing the skill that the user wants to use
    """
    print(f"Please enter a number between 1 - {len(character_dictionary['skills'])} representing the skill that you "
          f"want to use on {enemy_dictionary['name']}: ")
    user_attack_skill_choice_index = get_user_choice(character_dictionary['skills'])

    return character_dictionary['skills'][int(user_attack_skill_choice_index) - 1]


def increment_character_exp(character_dictionary: dict, enemy_dictionary: dict):
    """Increment character exp based on enemy level

    :param character_dictionary: a dictionary
    :param enemy_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary containing vital information about the character
    :precondition: enemy_dictionary is a dictionary containing vital information about the enemy
    :postcondition: character_dictionary is modified

    >>> character = {'current_exp': 0, 'level_up_exp': 40}
    >>> enemy = {'level': 1, 'name': 'test_enemy'}
    >>> increment_character_exp(character, enemy)
    You gained 25 EXP for killing the test_enemy.
    <BLANKLINE>
    >>> character == {'current_exp': 25, 'level_up_exp': 40}
    True
    """

    exp_to_increment = 25 if enemy_dictionary['level'] == 1 else 40

    print(f"You gained {exp_to_increment} EXP for killing the {enemy_dictionary['name']}.\n")
    character_dictionary['current_exp'] += exp_to_increment

    if character_dictionary['current_exp'] >= character_dictionary['level_up_exp']:
        character_dictionary['current_exp'] = character_dictionary['level_up_exp']


def is_character_level_up(character_dictionary: dict) -> bool:
    """Determines whether the character levels up.

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary that contains vital character data
    :postcondition: function returns True if character_dictionary['current_exp'] == character_dictionary['level_up_exp']
                    else return False
    :postcondition: character_dictionary is modified
    :return: a boolean value

    >>> character = {'current_exp': 20, 'level_up_exp': 20}
    >>> is_character_level_up(character)
    True
    """

    return character_dictionary['current_exp'] == character_dictionary['level_up_exp']


def increment_character_level(character_dictionary: dict):
    """Increment the characters' level by one

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary that contains vital character data
    :postcondition: character_dictionary['level'] is incremented by one
    :postcondition: character_dictionary is modified

    >>> character = {'level': 1}
    >>> increment_character_level(character)
    >>> character == {'level': 2}
    True
    """

    character_dictionary['level'] += 1


def increase_attack_stat(character_dictionary: dict):
    """Increase attack stat based on characters' class

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary that contains vital character data
    :postcondition: character_dictionary['attack_stat'] is doubled
    :postcondition: character_dictionary is modified

    >>> character = {'attack_stat': 20}
    >>> increase_attack_stat(character)
    >>> character == {'attack_stat': 40}
    True
    """

    character_dictionary['attack_stat'] *= 2


def increase_defense_stat(character_dictionary: dict):
    """Increase defense stat based on characters' class

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary that contains vital character data
    :postcondition: character_dictionary['defense_stat'] is doubled
    :postcondition: character_dictionary is modified

    >>> character = {'defense_stat': 20}
    >>> increase_defense_stat(character)
    >>> character == {'defense_stat': 40}
    True
    """
    character_dictionary['defense_stat'] *= 2


def increase_max_hp(character_dictionary: dict):
    """Increase max hp based on characters' class.

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary that contains vital character data
    :postcondition: character_dictionary['Max HP'] is doubled
    :postcondition: character_dictionary is modified

    >>> character = {'Max HP': 20}
    >>> increase_max_hp(character)
    >>> character == {'Max HP': 40}
    True
    """
    character_dictionary['Max HP'] *= 2


def increase_level_up_exp(character_dictionary: dict):
    """Increase level up exp based on characters' level.

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary that contains vital character data
    :postcondition: character_dictionary['level_up_exp'] is doubled
    :postcondition: character_dictionary is modified

    >>> character = {'level_up_exp': 20}
    >>> increase_level_up_exp(character)
    >>> character == {'level_up_exp': 40}
    True
    """

    character_dictionary['level_up_exp'] *= 2


# This function is unittested via the helper functions.
def level_up_character(character_dictionary: dict):
    """Level up the character by modifying its character dictionary respectively.

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary containing vital character data
    :postcondition: function instructs the user to head over to boss map when the character is level 3
    :postcondition: function displays current level and current rank
    :postcondition: function resets character_dictionary['current_exp'] to 0
    """
    increment_character_level(character_dictionary)
    increase_attack_stat(character_dictionary)
    increase_defense_stat(character_dictionary)
    increase_max_hp(character_dictionary)
    increase_level_up_exp(character_dictionary)

    if character_dictionary['level'] == 3:
        print(f"Congratulations {character_dictionary['name']}! You leveled up! \n"
              f"You are now level {character_dictionary['level']}. Please make \n"
              f"your way to the boss so that you can complete the game.\n")
    else:
        print(f"Congratulations {character_dictionary['name']}! You leveled up! \n"
              f"You are now level {character_dictionary['level']}.\n"
              f"Your rank is now {get_character_rank(character_dictionary)}.\n")

    print("You feel stronger and more durable!\n")

    character_dictionary['current_exp'] = 0


def can_fight_boss(some_rows: int, some_columns: int, character_dictionary: dict) -> bool:
    """Determines whether the player can fight the boss.

    The player can fight the boss if they are in the bottom right of the map and if they are level 3.

    :param some_rows: an int
    :param some_columns: an int
    :param character_dictionary: a dictionary
    :precondition: rows >= 2
    :precondition: columns >= 2
    :precondition: character_dictionary is a dictionary containing vital information about the character
    :postcondition: character_dictionary is not modified
    :postcondition: if character is located in the boss's location and is level 3, then the function returns True
    :return: a boolean value, True or False

    >>> character = {'X-coordinate': 9, 'Y-coordinate': 9, 'level': 3}
    >>> can_fight_boss(10, 10, character)
    True
    """

    character_location = (character_dictionary['X-coordinate'], character_dictionary['Y-coordinate'])
    boss_location = (some_rows - 1, some_columns - 1)

    return True if character_dictionary['level'] >= 3 and character_location == boss_location else False


def heal_character(character_dictionary: dict, amount_to_increase: int):
    """Increase the hp of the player character.

    :param character_dictionary: a dictionary
    :param amount_to_increase: an integer
    :precondition: character_dictionary is a dictionary containing vital information about the character
    :precondition: amount_to_increase is an integer corresponding to the HP increase for the character
    :postcondition: character_dictionary is modified
    :postcondition: Current HP will never increase above Max HP

    >>> character = {'Current HP': 100, 'Max HP': 200}
    >>> heal_character(character, 50)
    >>> character == {'Current HP': 150, 'Max HP': 200}
    True
    """

    character_dictionary['Current HP'] += amount_to_increase

    if character_dictionary['Current HP'] > character_dictionary['Max HP']:
        character_dictionary['Current HP'] = character_dictionary['Max HP']


def get_character_rank(character_dictionary: dict) -> str:
    """Obtain the current rank of the character based on their level.

    :param character_dictionary: a dictionary
    :precondition: character_dictionary is a dictionary containing vital data about the character
    :postcondition: character_dictionary is not modified
    :return: a string containing the rank of the character

    >>> character = {'ranks': ['Fighter', 'Hero', 'Dark Knight'], 'level': 2}
    >>> get_character_rank(character)
    'Hero'
    """

    return (character_dictionary['ranks'][character_dictionary['level'] - 1] if character_dictionary['level'] <= 3
            else character_dictionary['ranks'][2])


def opening_scene(character_dictionary: dict):
    """Displays the opening scene for the game

    :param character_dictionary: a dictionary containing vital information about the player.
    """
    print(text.opening_scene_one)
    time.sleep(5)
    print(text.opening_scene_two)
    time.sleep(5)
    print(f"This is where you come in {character_dictionary['name']} the {character_dictionary['character_class']} of "
          f"rank {get_character_rank(character_dictionary)}. The fate of Artura depends on you.\n")
    time.sleep(5)
    print(text.opening_scene_four)
    time.sleep(5)
    print(f"Best of luck {character_dictionary['name']} the {character_dictionary['character_class']} "
          f"of rank {get_character_rank(character_dictionary)}.\n")
    time.sleep(3)


def combat_controller(some_rows, some_columns, character_dictionary: dict, enemy_dictionary: dict):
    print(f"You have encountered a {enemy_dictionary['name']}\n")
    flee = False
    enemy_flee = False
    time.sleep(2)

    # Each iteration in the while loop is a round of combat.
    while not flee and is_alive(character_dictionary) and is_alive(enemy_dictionary):
        print(f"Your HP: {character_dictionary['Current HP']}/{character_dictionary['Max HP']}")
        print(f"{enemy_dictionary['name']} HP: {enemy_dictionary['Current HP']}/{enemy_dictionary['Max HP']}")
        print(f"Your EXP: {character_dictionary['current_exp']}/{character_dictionary['level_up_exp']}\n")

        user_pre_combat_choice = get_user_pre_combat_choice()

        if user_pre_combat_choice == '1':
            print(enemy_dictionary['enemy_description'])
            print()
        else:
            if user_pre_combat_choice == '2':
                user_attack_skill_choice = get_user_attack_skill_choice(character_dictionary, enemy_dictionary)
                print(f"You used {user_attack_skill_choice} on the {enemy_dictionary['name']}\n")
                time.sleep(1)
                attack_the_defender(character_dictionary, enemy_dictionary, user_attack_skill_choice)
                time.sleep(1)

                # Print player and enemy HP
                print(f"Your HP: {character_dictionary['Current HP']}/{character_dictionary['Max HP']}")
                print(f"{enemy_dictionary['name']} HP: {enemy_dictionary['Current HP']}/{enemy_dictionary['Max HP']}\n")
            elif user_pre_combat_choice == "3":
                print(f"You drank a healing potion.\n")
                heal_character(character_dictionary, 50)
                time.sleep(1)
                print("You gained 50 HP.")
                print(f"Your HP: {character_dictionary['Current HP']}/{character_dictionary['Max HP']}\n")
            elif user_pre_combat_choice == '4':
                print('Attempting to flee')
                time.sleep(3)
                flee = percent_chance(0.20)
                if not flee:
                    print('You failed your attempt to flee.\n')
                elif flee:
                    print("You were able to flee successfully.\n")

            # Enemy attacks' player. 5% chance for enemy to flee after they attack.
            if is_alive(enemy_dictionary) and is_alive(character_dictionary):
                time.sleep(2)
                enemy_attack_skill_used = get_random_enemy_skill(enemy_dictionary)
                print(f"The {enemy_dictionary['name']} used {enemy_attack_skill_used}!\n")
                time.sleep(1)
                attack_the_defender(enemy_dictionary, character_dictionary, enemy_attack_skill_used)
                time.sleep(1)

            # if character died mid-battle, early exit out of combat_controller()
            if not is_alive(character_dictionary):
                return 0

            # Enemy has a five percent chance to flee. At 20%,
            # it seemed like the enemy was fleeing in nearly every fight
            enemy_flee = percent_chance(0.05)
            if enemy_flee and not can_fight_boss(some_rows, some_columns, character_dictionary):
                print(f"The {enemy_dictionary['name']} ran away from you\n")
                time.sleep(1)
                flee = True
    if is_alive(character_dictionary) and not is_alive(enemy_dictionary) and not enemy_flee:
        print(f"You killed the {enemy_dictionary['name']}!\n")
        increment_character_exp(character_dictionary, enemy_dictionary)
        print(f"Your EXP: {character_dictionary['current_exp']}/{character_dictionary['level_up_exp']}")

    heal_character(character_dictionary, 100)
    print(f"You, {character_dictionary['name']} the {character_dictionary['character_class']} of rank "
          f"{get_character_rank(character_dictionary)} rested up after the fight. \n")
    time.sleep(2)
    print("You gained 100 HP.")
    print(f"Your HP: {character_dictionary['Current HP']}/{character_dictionary['Max HP']}\n")
    time.sleep(2)


def game() -> None:
    game_rows = 10
    game_columns = 10
    board = make_board(game_rows, game_columns)
    is_boss_dead = False

    print(f"\nWelcome to Evon's COMP 1510 Assignment 4 game. Enjoy!\n")
    time.sleep(2)

    character = make_character()
    achieved_goal = False
    opening_scene(character)
    while is_alive(character) and not is_boss_dead:
        # Tell the user where they are
        print("Map: ")
        print("X is your current location.")
        print("B is the Nameless King's last known location.\n")
        display_map(game_rows, game_columns, character)
        print()
        describe_current_location(board, character)
        print()
        print(f"Your HP: {character['Current HP']}/{character['Max HP']}")
        print(f"Your EXP: {character['current_exp']}/{character['level_up_exp']}")
        print(f"You are currently a level {character['level']} {character['character_class']} of rank "
              f"{get_character_rank(character)}.\n")
        direction = get_user_direction_choice()

        valid_move = validate_move(game_rows, game_columns, character, direction)

        if valid_move:
            move_character(character, direction)

            # There is a 20% chance of an enemy appearance when entering a new area.
            there_is_a_challenger = percent_chance(0.20)

            # Character fights the boss if can_fight_boss() returns True
            if can_fight_boss(game_rows, game_columns, character):
                print(f"{character['name']} the {character['character_class']} of rank "
                      f"{get_character_rank(character)}, the Nameless King has deemed you worthy \n"
                      f"enough for a fight. Good luck. The land depends on your success.\n")
                boss = make_boss()
                combat_controller(game_rows, game_columns, character, boss)
                is_boss_dead = True
            elif there_is_a_challenger:
                enemy = make_enemy(character)
                combat_controller(game_rows, game_columns, character, enemy)
            achieved_goal = check_if_goal_attained(game_rows, game_columns, character)
            print()
        else:
            print("You cannot go that way. \n")
            time.sleep(2)

        if is_character_level_up(character):
            time.sleep(2)
            level_up_character(character)
            time.sleep(2)

    if is_alive(character) and achieved_goal and is_boss_dead:
        print("You did it! You saved Artura from the Nameless King! Well done!\n")
    elif not is_alive(character) and not achieved_goal and not is_boss_dead:
        print("You died. Try again.")

    time.sleep(4)
    print("Thank you for playing the game!")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
