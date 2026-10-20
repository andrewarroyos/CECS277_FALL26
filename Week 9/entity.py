import abc

class Entity(abc.ABC):
    def __init__(self, name, max_hp):
        """
        1. __init__(self, name, max_hp) – set the _name, _max_hp, and _hp. Assign the
        max_hp value to both the _max_hp and _hp attributes.
        """
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    
        
    @property
    def name(self):
        """
        Return name
        """
        return self._name
    
    
    @property    
    def hp(self):
        """
        Return hp
        """
        return self._hp
    
        
    def take_damage(self, dmg):
        """
        Subtract damage value from entity's _hp value. Do not let hp go past 0. If negative, set to 0.
        """
        self._hp -= dmg
        
        if self._hp < 0:
            self._hp = 0
    
    
    def __str__(self):
        """
        Display the entity's name and hp in the format in "Name: hp/max".
        """
        return f"{self._name}: {self._hp}/{self._max_hp}"
    
    
    # ABSTRACT METHODS
    #=================
    @abc.abstractmethod
    def basic_attack(self, other):
        pass
        

    @abc.abstractmethod
    def special_attack(self, other):
        pass
    