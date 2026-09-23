# Group 16
# Andrew Arroyos
# Michael Sena
# Lab 5 - Class/Objects - Traps & Treasures

import trap
import treasure
import random

#==================#
# HELPER FUNCTIONS #
#==================#

def get_random_coordinates():
    random_row = random.randint(0,9)
    random_column = random.randint(0,9)
    random_coordinate = [random_row, random_column]
    return random_coordinate

def intro_menu():
    """
    Intro menu
    """
    print("-Traps & Treasures-\nThere are three treasures to find.\nHints will be given every three steps.")
    print("But look out for the traps!\nYou will sense any traps nearby.")
    print("Dig up all three treasures without getting\ncaught in a trap to win.")
    
def spawn_player():
    
    return
    
def generate_trap():
    """Generate a random trap on a 10x10 field"""
    trap_coordinate = get_random_coordinates()
    hidden_trap = trap.Trap(trap_coordinate)
    return hidden_trap

def generate_treasure():
    treasure_coordinate = get_random_coordinates()
    hidden_treasure = treasure.Treasure(treasure_coordinate)
    return hidden_treasure
    

def player_move_menu():
    """
    This menu will be used for player moves.
    """
    print("Player Move:\n1. North\n 2. South\n 3. West\n 4. East\n 5. Dig")
    

def main():
    # CONSTANTS
    GRID_ROWS = 10
    GRID_COLUMNS = 10
    player_alive = True
    
    # Game boot up
    intro_menu()
    trap01 = generate_trap()
    print(trap01.location)
    


main()