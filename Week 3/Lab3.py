# Group 16
# Andrew Arroyos
# Michael Sena
# Lab 3 - Lists

import check_input
import random

def generate_code():
    """
    Randomly generate the computer's secret 4 digit code. Between 1-6.
    All unique numbers. Return code as list.
    """
    
    computer_code = []
    
    # Fill computer code return list with unique numbers
    while len(computer_code) < 4:
        random_number = random.randint(1,6)
        if random_number not in computer_code:
            computer_code.append(random_number)
    
    return computer_code
    

def get_guess():
    """
    Prompt user to enter a 4 digit guess. Each digit will be validated
    that it is unique and within range 1-6. Return guess as list.
    """
    guess_list = []
    
    # Prompt user to guess 4 unique numbers
    while len(guess_list) < 4:
        guess = check_input.get_int_range(f"- Enter digit {len(guess_list) + 1}: ", 1,6)
        
        # Only add to return list if it is a unique number
        if guess not in guess_list:
            guess_list.append(guess)
        else:
            print("Invalid input – cannot enter a duplicate value.")
    return guess_list
    

def check_guess(code, guess):
    """
    Pass computer's code and player's guess. Determine number of
    exact matches and misplaced matches. Return results as two item list.
    """
    exact_matches = 0
    mismatches = 0 
    index = 0
    
    # Check each index of the list to see if any of the guesses
    # match with the computer's code
    while index < 4:
        if guess[index] == code[index]:
            exact_matches += 1
        elif guess[index] in code:
            mismatches += 1
        
        index = index + 1
            
    matchup_list = [exact_matches, mismatches]
    return matchup_list
        

def display_results(results):
    """
    Displays results after every attempt
    """
    
    print("Results:")
    print(f"- Exact matches: {results[0]}")
    print(f"- Misplaced matches: {results[1]}")
    return results


def main():

    print("--Code Breaker!--\nCrack the 4-digit code within 8 attempts to open the safe.\nEach digit is between 1-6.")
    
    # Start game - generate computer code
    computer_code = generate_code()
    
    # Left here on purpose to play with code shown - testing purposes
    print(computer_code)
    
    attempts = 1
    while attempts <= 8:
            
        print(f"\nAttempt #{attempts}")
        attempts += 1
        
        player_guess = get_guess()
        print(f"Your guess: {player_guess}")
        check_score = check_guess(computer_code, player_guess)
        display_results(check_score)
        
        # If attempts pass 8, game ends.
        if attempts > 8:
            print("\nYou couldnt crack the code!")
        elif check_score[0] == 4:
            print("\nYou have cracked the code!")
            break


main()