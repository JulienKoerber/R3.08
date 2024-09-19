from Personnage import Personnage

class Mage(Personnage):
    def __init__(self, pseudo, niveau=1):
        super().__init__(pseudo, niveau, niveau * 5 + 10, niveau * 6 + 4)
        self.mana = niveau * 5

    def degats(self):
        if self.mana > 0:
            self.mana -= 4
            return self.__niveau + 3
        else:
            return self.__niveau