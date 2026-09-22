# Group 16
# Andrew Arroyos
# Michael Sena
# Lab 2

import check_input as ci
import random

def weapon_menu():
    """
    Prompts the user to input their choice: (R)ock, (P)aper,
    (S)cissors, or (B)ack. Checks that the user’s input is an R, P, S, or B, 
    displays the user’s choice, and then returns the inputted value.
    """
    # Prompt player to choose a weapon
    valid_choice = False
    while valid_choice == False:
        weapon_choice = input("Choose your weapon:\nR. Rock\nP. Paper\nS. Scissors\nB. Back\n").upper()
        if weapon_choice in ("R", "P", "S", "B"):
            valid_choice = True
            if weapon_choice == "R":
                print("You chose Rock")
            elif weapon_choice == "P":
                print("You chose Paper")
            elif weapon_choice == "S":
                print("You chose Scissors")
        else:
            print("Make sure your choice is either \"R\", \"P\", \"S\", or \"B\" to quit.")
    else:
        return weapon_choice        

def comp_weapon():
    """
    @function randomly assigns a weapon for the computer to use against the player
    """
    
    c_wep = random.choice(["R", "P", "S"])
    if c_wep == "R":
        print("Computer chose Rock")
    elif c_wep == "P":
        print("Computer chose Paper")
    elif c_wep == "S":
        print("Computer chose Scissors")
    return c_wep

def find_winner(p_wep, c_wep):
    """
    @function returns an int of range 0-2. 0 = tie,
    1 = player win, 2 = computer win
    """

    if p_wep == c_wep:
        return 0
    elif p_wep == "R" and c_wep == "S":
        return 1
    elif p_wep == "P" and c_wep == "R":
        return 1
    elif p_wep == "S" and c_wep == "P":
        return 1
    else:
        return 2
    
def display_scores(p_score, c_score):
    """
    @function displays scores
    """
    print(f"Player = {p_score}\nComputer = {c_score}")

def main():
    
    player_score = 0
    computer_score = 0
    game_on = True
    
    while game_on:

        choice = ci.get_int_range("RPS Menu:\n1. Play game\n2. Show score\n3. Quit\n", 1, 3)

        if choice == 1:
            player_weapon = ""
            while player_weapon != "B":
                player_weapon = weapon_menu()
                if player_weapon != 'B':
                    computer_weapon = comp_weapon()
                    winner = find_winner(player_weapon, computer_weapon)

                    if winner == 1:
                        player_score += 1
                        print("Player wins!")
                    elif winner == 2:
                        computer_score += 1
                        print("Computer wins!")
                    else:
                        print("Tie!")

        elif choice == 2:
            display_scores(player_score, computer_score)
        
        else:
            print("Final Score:")
            display_scores(player_score, computer_score)
            game_on = False    
        
main()