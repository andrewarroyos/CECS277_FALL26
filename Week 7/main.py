# Group 16
# Andrew Arroyos
# Michael Sena
# Lab 7 - Class Relationships - Yahtzee

import player
import die
import check_input

def take_turn(player_object: player.Player):
  """
  This function should:
    - roll the player's dice
    - display the dice
    - check for and display any win types (pair, series, 3 O-A-K)
    - display the updated score
  """
  player_object.roll_dice()
  print(player_object)
 
  if player_object.has_three_of_a_kind():
    print("You got 3 of a kind!")
  elif player_object.has_pair():
    print("You got a pair!")
  elif player_object.has_series():
    print("You got a series of 3!")
  else:
    print("Aww. Too Bad.")
    
  print(f"Score = {player_object.points}")
  
  

def main():
  """
  The main function should:
    - construct a player object
    - then repeatedly call take_turn until user chooses to end the game
    - display final points at end of game
    - use check_input to prompt user to continue or end
  """
  
  player1 = player.Player()

  in_game = True
  while in_game:
    take_turn(player1)
    play_again = check_input.get_yes_no("Play again? (Y/N):")
    print()
    if play_again == True:
      continue
    else:
      in_game = False
      print("Game Over.")
      print(f"Final Score = {player1.points}")

main()