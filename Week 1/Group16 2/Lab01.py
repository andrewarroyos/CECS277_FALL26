'''
Group: 16
Name 1: Andrew Arroyos
Name 2: Michael Sena
Assignment: Lab 01 - Three Card Monte
'''

import check_input as ci
import random

def main():
    game_on = True
    wallet = 100

    # Title of game
    print("-Three Card Monte-\nFind the queen to double your bet!")
        
    while game_on and wallet > 0:
        print(f"\nYou have ${wallet}")
        
        # Make sure bet is between $1 - wallet amount
        bet = ci.get_int_range("How much you wanna bet? ", 1, wallet)
    
        # Display cards
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  1  | |  2  | |  3  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
        
        # Find the queen prompt
        guess = ci.get_int_range("Find the queen: ", 1, 3)
    
        # Holds value of queen
        queen_place = random.randint(1,3)
    
        # Reveal the queen's actual position
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
 
        if queen_place == 1:
            print("|  Q  | |  K  | |  K  |")
        elif queen_place == 2:
            print("|  K  | |  Q  | |  K  |")
        else:
            print("|  K  | |  K  | |  Q  |")
 
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
        
        # Update wallet depending on win or lose
        if guess == queen_place:
            print("You got lucky this time...\n")
            wallet += bet
        else:
            print("Sorry... you lose.")
            wallet -= bet
        
        # Check if player still has money and ask to play again
        if wallet > 0:
            game_on = ci.get_yes_no("Play Again? (Y/N): ")
        else:
            print("You're out of money. Beat it loser!")

main()
