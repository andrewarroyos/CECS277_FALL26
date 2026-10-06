"""
Player class:
    - has two attributes:
        - a list of 3 Die objects
        - player's points
"""

import die

class Player:
    def __init__(self):
        """
        constructs and sorts the list of three Die objects and then initializes the player's points to 0.
        """
        d1 = die.Die()
        d2 = die.Die()
        d3 = die.Die()
        die_list = [d1, d2, d3]
        
