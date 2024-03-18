from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def take_damage(self, dmg):
        pass

    @abstractmethod
    def heal(self, hp):
        pass

    @abstractmethod
    def lose_stamina(self, stmn)
        pass

class CharParam(ABC):
    @property
    def strength(self):
        pass

    @property
    def charisma(self):
        pass
    
    @property
    def agility(self):
        pass

    @property 
    def intelligence(self):
        pass
    
    @property
    def luck(self):
        pass

class MapCell(ABC):
    @property
    def x(self):
        pass

    @property
    def y(self):
        pass