#Group 16
# Michael Sena, Andrew Arroyos
# 9/15/2026
# Lab Assignment 4
# This program quizzes a student on finding the correct capital of a random state that is given.

import random

def read_file_to_dict(file_name):
    """

    Reads in each line from the file and seperates the state and capital
    Then stores them as a key:value pair in a dictionary 

    Args:
        file_name: a file filled with states and capitals that the program reads.

    Returns:
        a filled dictionary

    """
    states = {}

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            # seperates each line into a state and it's capital
            state, capital = line.split(",")
            states[state] = capital

    return states


def get_random_state(states):
    """

    Passes in the states dictionary and converts the dictionary to a list of keys
    Then chooses a random key from the list

    Args:
        states: a dictionary of the states

    Returns:
        a random key (selected state)

    """
    state_list = list(states.keys())

    random_state = random.choice(state_list)

    return random_state


def get_random_choices(states, correct_state):
    """
    Passes in the states dictionary and the correct state, places the correct state into a list then
    calls get_random_state to add three other unique states to this list. Then create a list of capitals
    from the list of states, shuffles it then returns it.

    Args:
        states: dictionary of the states and their capitals

        correct_state: the state used for the quiz question

    Returns:
        a shuffled list of four capitals choices

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
    """

    Reads in the file then have a loop that repeats 10 times (one for each of the questions)
    For each question, choose a random state as the correct answer, generate the possible answers, display the
    question number and the quiz question. Then compare the user's selection (0-3) against the location of the correct
    capital(0-3). If the user is correct display a congratulatory message and give them a point, otherwise tell them
    that they were inccorect and dispaly the correct answer.
    After all 10 questions are finished, display the total points they received. 

    Args:
        None

    Returns:
        None
    """
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