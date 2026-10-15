# Player Class

class Player:
    def __init__(self) -> None:
        """
        Player Attributes:
            - hp: int
            - gold: int
            - key: int
            - location: list
            - escaped: bool
        """
        self.hp = 50
        self.gold = 0
        self.key = 0
        self.location = [0,0]
        self.escaped = False
    
    
    def take_dmg(self, dmg: int) -> int:
        """
        pass in the amount of damage and subtract it from the player's current HP. If HP is < 0,
        then resest the HP to 0.
        """
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
        
        
    def inc_gold(self, g: int) -> int:
        """
        pass in an amount of gold and add it to the player's gold.
        """
        self.gold += g
        return self.gold
    
    
    def inc_key(self) -> int:
        """
        add 1 to the player's keys
        """
        self.key = 1
        return self.key
        