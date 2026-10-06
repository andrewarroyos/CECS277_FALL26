# Die class has two attributes:
    # - number of sides of th die
    # - value of the rolled die

    # They should be named using a leading underscore.
    # They do not need property methods.
    
import random
import check_input

class Die:
    def __init__(self, sides=6):
        """
        passes in the number of sides of the die.
        Assigns sides using the parameter and set value to either 0 or the returned value of roll()
        """
        self._sides = sides
        self._value = 0
        
        
    def roll(self):
        """
        generate a random number between 1 and the number of sides and assign it to value.
        Return the value of value
        """
        self._value = random.randint(1,self._sides)
        return self._value
    
    
    def __str__(self):
        """
        return the Die's value as a string
        """
        return str(self._value)
    
    
    def __lt__(self, other):
        """
        return true if the value of self is LESS than the value of other
        """
        if self._value < other._value:
            return True
        else:
            return False
        
        
    def __eq__(self, other):
        """
        return true if the value of self is equal to the value of other
        """
        if self._value == other._value:
            return True
        else:
            return False
        
        
    def __sub__(self, other):
        """
        return the difference between the value of self and value of other
        (hint: take absolute value to always get a positive difference)
        """
        return abs(self._value - other._value)
        