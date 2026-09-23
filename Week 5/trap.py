
class Trap:
    def __init__(self, location):        
        self._location = list(location)
        
    @property
    def location(self):
        return self._location
    
    def hint(self, player_position):
        """
        Pass player's current position. If location is in
         surrounding eight spaces to trap location, return True.
        """
        
        player_row = player_position[0]
        player_column = player_position[1]
        trap_row = self._location[0]
        trap_column = self.location[1]
        
        row_distance = abs(trap_row - player_row)
        column_distance = abs(trap_column - player_column)
        
        return max(row_distance, column_distance) == 1
            