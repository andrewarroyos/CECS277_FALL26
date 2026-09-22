# Group 16
# Andrew Arroyos
# Michael Sena
# Lab 4 - File IO - State Capitals Quiz

import random

def read_file_to_dict(file_name):
    """Read state,capital lines into a dictionary and return it."""
    
    states = {}
    with open(file_name) as file:
        for line in file:
            if line.strip():
                state, capital = line.strip().split(",")
                states[state.strip()] = capital.strip()
    return states

def get_random_state(states):
    """Return a random state from the dictionary's keys"""
    state_names = list(states.keys())
    return random.choice(state_names)

def get_random_choices(states, correct_state):
    """
    pass in the states
    dictionary and the correct state. Place the correct state into a list and then call
    get_random_state to add three other states to this list. These states should be
    different from the correct state and also different from each other. Using the list of states,
    create a list of capitals, shuffle it, and then return that list. This is the list of possible
    answers that the user will choose from.
    """
    choices = [correct_state]
    # Add random states until there are four unique choices
    while len(choices) < 4:
        random_state = get_random_state(states)

        if random_state not in choices:
            choices.append(random_state)
    
    possible_answers = []
    # convert the four states into their capitals
    for state in choices:
        possible_answers.append(states[state])

    random.shuffle(possible_answers)

    return possible_answers
    
    # states = master_dictionary.keys()

def ask_question(correct_state, possible_answers):
    """
    Passes in the name of the correct state and the list of four possible answers.
    Then displays the question to the user with the four possible answers.
    Gets the user's selection(input) and checks if valid(A-D).
    Args:
        correct_state: the correct state answer
        possible_answers: a list of four possible answers
    
    Returns:
        The users choice of a value(0-3)
    """
    
    print(f"The capital of {correct_state} is:")
    print(f"A. {possible_answers[0]} B. {possible_answers[1]} C. {possible_answers[2]} D. {possible_answers[3]}")

    selection = input("Enter selection: ").upper()

    while selection not in ["A", "B", "C", "D"]:
        print("Invalid input. Input choice A-D.")
        selection = input("Enter selection: ").upper()
    # convert the letter choice A-D into list indexes 0-3
    if selection == "A":
        return 0
    elif selection == "B":
        return 1
    elif selection == "C":
        return 2
    else:
        return 3

def main():
    states = read_file_to_dict("statecapitals.txt")

    score = 0
    
    print("- State Capitals Quiz -")

    for question_num in range(1, 11):
        correct_state = get_random_state(states)
        possible_answers = get_random_choices(states, correct_state)

        print(f"{question_num}. ", end = "")
        user_answer = ask_question(correct_state, possible_answers)

        # find the location of the correct capital in the shuffled answers
        correct_capital = states[correct_state]
        correct_index = possible_answers.index(correct_capital)

        if user_answer == correct_index:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_capital}.")
    print(f"End of test. You got {score} correct.")
    

main()