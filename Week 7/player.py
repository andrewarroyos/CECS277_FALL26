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
        self._dice = [d1, d2, d3]
        self._dice.sort()
        self._points = 0
        
        
    @property    
    def points(self):
        """
        get property that returns the player's points
        """
        return self._points
    
    
    def roll_dice(self):
        """
        calls roll on each of th Die objects in the list and then sorts the list
        """
        for die in self._dice:
            die.roll()
        self._dice.sort()
    
    
    def has_pair(self):
        """
        returns true if only two dice in the list have the same value
        """
        value1 = self._dice[0]
        value2 = self._dice[1]
        value3 = self._dice[2]
        
        if value1 == value2 and value1 != value3:
            self._points += 1
            return True
        elif value1 == value3 and value1 != value2:
            self._points += 1
            return True
        elif value2 == value3 and value2 != value1:
            self._points += 1
            return True
        else:
            return False
        
        
    def has_three_of_a_kind(self):
        """
        returns true if all three dice in the list have the same value (use ==). Increments points by 3.
        """
        value1 = self._dice[0]
        value2 = self._dice[1]
        value3 = self._dice[2]
        
        if value1 == value2 == value3:
            self._points += 3
            return True
        else:
            return False
    
    
    def has_series(self):
        """
        returns true if the values of each of the dice in the list are in a sequence. Increments by 2.
        """
        value1 = self._dice[0]
        value2 = self._dice[1]
        value3 = self._dice[2]
        
        if value3 - value2 == 1 and value2 - value1 == 1:
            self._points += 2
            return True
        else:
            return False
        
        
    def __str__(self):
        """
        returns a string in the format "D1=2, D2=4, D3=6"
        """
        return f"D1={str(self._dice[0])}, D2={str(self._dice[1])}, D3={str(self._dice[2])}"
    