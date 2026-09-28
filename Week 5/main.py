# Group 16
# Andrew Arroyos
# Michael Sena
# Lab 5 - Class/Objects - Traps & Treasures  

import random
import check_input
from trap import Trap
from treasure import Treasure

#==================#
# HELPER FUNCTIONS #
#==================#

def create_field():
    """Creates a 10x10 field."""
    field = []
    for row in range(10):
        field.append(["*"] * 10)
    return field


def display_field(field, player_position):
    """Displays the field with the player's current location."""
    # Go through every row and col on the field
    for row in range(10):
        for col in range(10):

            # Display P at the player's current location
            if [row, col] == player_position:
                print("P", end=" ")
            else:
                print(field[row][col], end=" ")
        
        print()


def generate_location(used_locations):
    """Generates random location that has not already been used"""
    # Generate a random row and col 0 through 9
    location = [random.randint(0,9), random.randint(0, 9)]

    # Keep generating until an unused location is found 
    while location in used_locations:
        location = [random.randint(0,9), random.randint(0, 9)]
    
    return location

def get_move():
    """Displays the player move menu and gets the user's choice."""
    
    print("Player Move:")
    print("1. North")
    print("2. South")
    print("3. West")
    print("4. East")
    print("5. Dig")

    # Validates the users choice is between 1 and 5
    move = check_input.get_int_range("> ", 1, 5)
    return move

def move_player(field, player_position, move):
    """Moves the player in the selected direction"""
    
    # Move north
    if move == 1:
        if player_position[0] > 0:
            field[player_position[0]][player_position[1]] = "."
            player_position[0] -= 1
        else:
            print("You cannot move there!")
    # Move south
    elif move == 2:
        if player_position[0] < 9:
            field[player_position[0]][player_position[1]] = "."
            player_position[0] += 1
        else:
            print("You cannot move there!")
    # Move west
    elif move == 3:
        if player_position[1] > 0:
            field[player_position[0]][player_position[1]] = "."
            player_position[1] -= 1
        else:
            print("You cannot move there!")
    # Move east
    elif move == 4:
        if player_position[1] < 9:
            field[player_position[0]][player_position[1]] = "."
            player_position[1] += 1
        else:
            print("You cannot move there!")


#==========#
#   MAIN   #
#==========#           
            
def main():
    """Starts running the traps and treasures game"""
    # Create the 10x10 field
    field = create_field()

    # Keep track of occupied starting locations so no duplicates
    used_locations = []

    # Generate the players starting position
    player_position = generate_location(used_locations)
    used_locations.append(player_position)

    # Create three treasure objects in diff locations
    treasures = []

    for i in range(3):
        location = generate_location(used_locations)
        treasures.append(Treasure(location))
        used_locations.append(location)
    
    # Create three trap objects in diff locations
    traps = []

    for i in range(3):
        location = generate_location(used_locations)
        traps.append(Trap(location))
        used_locations.append(location)
    
    # Display instructions/menu
    print("-Traps & Treasures-")
    print("There are three treasures to find.")
    print("Hints will be given every three steps.")
    print("But look out for the traps!")
    print("You will sense any traps nearby.")
    print("Dig up all three treasures without getting")
    print("caught in a trap to win.")

    # Track the number of rounds and when the player hits a trap
    round_count = 0
    caught = False

    # Continue until all treasures are found or the player hits a trap 
    while len(treasures) > 0 and not caught:
        display_field(field, player_position)

        # Check if the player is within one space of any trap
        for trap in traps:
            if trap.hint(player_position):
                print("You sense a trap nearby")
                break
        
        # Display treasure hints every third round
        if round_count % 3 == 0:
            for treasure in treasures:
                print(treasure.hint(player_position))
        
        # Get the players next choice 
        move = get_move()

        if move <= 4:
            move_player(field, player_position, move)

            for trap in traps:
                if player_position == trap.location:
                    display_field(field, player_position)
                    print("You fell in a trap!")
                    caught = True
        
                    break
        # Choice 5 means the player wants to dig
        else:
            found = False

            # Check whether a treasure is at the players location
            for treasure in treasures:
                if player_position == treasure.location:
                    print("You found a treasure!")
                    treasures.remove(treasure)
                    print("Treasures remaining =", len(treasures))
                    found = True
                    break
            # No treasure was found at players location     
            if not found:
                print("You didn't find anything here!")
        
        # Increases the round count after each choice 
        round_count += 1

    # Display the final result of the game
    if caught:
        print("Game Over")
    else:
        print("You found all three treasures!")
        print("You win!")

main()