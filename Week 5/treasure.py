class Treasure:
    def __init__(self, _location):
        self._location = _location
    
    @property
    def location(self):
        return self._location
        
    def hint(self, player_position):
        """
        Pass player location. Point player to right direction of
        treasure.
        """
        treasure_row, treasure_column = self._location
        player_row, player_column = player_position
        
        # Check vertical direction first (Row 0 is top)
        if treasure_row < player_row:
            return "A treasure is north of you."
        elif treasure_row > player_row:
            return "A treasure is south of you."

        # If rows are equal -> check horizontal direction
        if treasure_column > player_column:
            return "A treasure is east of you."
        elif treasure_column < player_column:
            return "A treasure is west of you."
    