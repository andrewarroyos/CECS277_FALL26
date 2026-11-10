# Group 16
# Andrew Arroyos
# Michael Sena
# CECS 277: Lab 8 - Inheritance - Dungeon Crawler

"""
Assignment:
    Create a program that allows the player to move around different rooms in a dungeon searching for
    treasure while trying to find the way out. Only one room in the dungeon is the exit and a key must
    be found to open the door. Other rooms may have treasures, monsters, or nothing at all. If the
    player finds a key and the exit, then they win the game. If the user runs out of hit points, then they lose.
"""

import random
from room import Room
from treasure import Treasure
from monster import Monster
from exit import Exit
from player import Player

def build_dungeon():
    """
    Build and return a random 5x5 dungeon

    Returns:
        list: 2D list containing the dungeon rooms
    """

    rooms = []

    #build the 5x5 dungeon

    # Create 5 rows
    for row in range(5):
        new_row = []

        #create 5 cols for each row
        for col in range(5):
            roll = random.randint(1, 5)

            if roll == 1:
                room = Room()
            elif roll <= 3:
                room = Treasure()
            else:
                room = Monster()
            
            # Add the room object to the current row
            new_row.append(room)
        
        # Add the completed row to the dungeon
        rooms.append(new_row)

    # Choose a random exit location
    exit_row = random.randrange(len(rooms))
    exit_col = random.randrange(len(rooms[0]))

    # So it doesn't get placed at the exit at the entrance
    while exit_row == 0 and exit_col == 0:
        exit_row = random.randrange(len(rooms))
        exit_col = random.randrange(len(rooms[0]))
    
    # Place the selected room with an Exit object
    rooms[exit_row][exit_col] = Exit()

    # Make the starting room an empty Room object
    rooms[0][0] = Room()

    return rooms

def display_dungeon(rooms, p):
    """
    Display the dungeon and player's position

    Args:
        rooms: the 2D list of room objects
        p: the player object
    """

    for row in range(len(rooms)):
        for col in range(len(rooms[row])):
            
            # Check if the player is at this position
            if p.location == [row, col]:
                print("P", end=" ")
            else:
                #display the room's character
                print(rooms[row][col].character, end=" ")

        # Move to the next line after each row
        print()

def main():
    """
    Runs the Dungeon game
    """

    # Build the dungeon 
    rooms = build_dungeon()

    # Create player
    p = Player()

    print("-Dungeon Crawler-")
    print("Find the key and find the exit to escape!")
    print("Treasure awaits, but watch out for monsters!")
    print("You enter the dungeon...")

    # Enter the starting room 
    rooms[0][0].enter_room(p)

    # Continue while the player is alive and has not escaped
    while p.hp > 0 and not p.escaped:

        #display players stats
        print(p)

        # Display dungeon map
        display_dungeon(rooms, p)

        # Ask player for a direction to go
        direction = input("Enter direction (wasd): ").lower().strip()

        # Determine where the player will move 
        if direction == "w":
            add_row = -1
            add_col = 0
        elif direction == "s":
            add_row = 1
            add_col = 0
        elif direction == "a":
            add_row = 0
            add_col = -1
        elif direction == "d":
            add_row = 0
            add_col = 1
        else:
            print("Invalid direction.")
            continue

        # Calculate the players possible new position
        new_row = p.location[0] + add_row
        new_col = p.location[1] + add_col

        # Check that the new position is inside the dungeon 
        if (0 <= new_row < len(rooms) and 0 <= new_col < len(rooms[0])):

            # Move the player
            p.move(add_row, add_col)

            # Enter the room at the players new location
            print(rooms[p.location[0]][p.location[1]].enter_room(p))
        
        else:
            print("You cannot move outside the dungeon.")
    
    # Display final dungeon 
    display_dungeon(rooms, p)

    # Determine whether the player won or lost
    if p.escaped:
        print("You win!")
    
    else:
        print("You lose!")
    
    print("Game Over.")

main()