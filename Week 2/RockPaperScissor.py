# Michael Sena & Andrew Arroyos
# Group 16
# Date: 9/1/2026
# This program is a Rock, Paper, Scissors game that allows the player to compete against the computer.
# It includes a menu for selecting weapons, determining the winner of each round, and displaying scores.
# It also includes a loop to allow the player to play multiple rounds and check_input for input validation. 

import random
import check_input


def weapon_menu():
    """
    Prompts the player to choose Rock, Paper, Scissors, or Back
    and validates the input.

    Returns:
        The player's valid weapon choice as R, P, S, or B.
    """
    print("Choose your weapon:")
    print("R. Rock")
    print("P. Paper")
    print("S. Scissors")
    print("B. Back")
    weapon = input().upper()

    # Validate the player's weapon choice
    while weapon not in ["R", "P", "S", "B"]:
        print("Invalid input. Please choose a valid weapon.")
        weapon = input().upper()
    
    if weapon == "R":
        print("You chose Rock")
    elif weapon == "P":
        print("You chose Paper")
    elif weapon == "S":
        print("You chose Scissors")

    return weapon


def comp_weapon():
    """
    Randomly selects the computer's weapon from Rock, Paper, or Scissors.

    Returns:
        The computer's weapon choice as R, P, or S.
    """
    # Randomly select the computer's weapon
    c_wep = random.choice(['R', 'P', 'S'])
    if c_wep == "R":
        print("Computer chose Rock")
    elif c_wep == "P":
        print("Computer chose Paper")
    elif c_wep == "S":
        print("Computer chose Scissors")

    return c_wep

    
def find_winner(p_wep, c_wep):
    """
    Compares the player's weapon and the computer's weapon
    to determine and display the winner.

    Args:
        p_wep: The player's weapon choice.
        c_wep: The computer's weapon choice.

    Returns:
        0 for a tie, 1 if the player wins, or 2 if the computer wins.
    """
    # Compare the player's weapon to the computer's weapon
    if p_wep == c_wep:
        print("Tie")
        return 0
    elif (p_wep == "R" and c_wep == "S") or (p_wep == "P" and c_wep == "R") or (p_wep == "S" and c_wep == "P"):
        print("You win")
        return 1
    else:
        print("Computer wins")
        return 2


def display_scores(p_score, c_score):
    """
    Displays the current player and computer scores.

    Args:
        p_score: The player's current score.
        c_score: The computer's current score.

    Returns:
        None.
    """
    print(f"Player = {p_score}")
    print(f"Computer = {c_score}")


def main():
    p_score = 0
    c_score = 0

    menu_choice = 0

    # Repeat the main menu until the player chooses to quit
    while menu_choice != 3:

        print("RPS Menu:")
        print("1. Play game")
        print("2. Show Score")
        print("3. Quit")
        menu_choice = check_input.get_int_range("", 1, 3)

        if menu_choice == 1:
            p_wep = ""
            
            while p_wep != "B":
                p_wep = weapon_menu()
                if p_wep != "B":
                    c_wep = comp_weapon()
                    winner = find_winner(p_wep, c_wep)

                    # Update the score based on the winner
                    if winner == 1:
                        p_score += 1
                    elif winner == 2:
                        c_score += 1
        
        elif menu_choice == 2:
            display_scores(p_score, c_score)
    print("Final Score:")
    display_scores(p_score, c_score)


main()