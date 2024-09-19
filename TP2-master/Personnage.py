from Guerrier import Guerrier
from Mage import Mage
class Personnage:
    def __init__(self, pseudo : str, niveau : int):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__PointsVie = niveau
        self.__initiative = niveau

    def __str__(self):
        return (f"Le personnage s'appelle {self.__pseudo} et il est de niveau {self.__niveau} !")

    def attaque(self, opposant : 'Personnage') -> None:
        if self.__initiative > opposant.__initiative:
            opposant.__PointsVie -= self.__niveau
            print(f'{opposant.__pseudo} à pris {self.__niveau} dégats !')
            if opposant.__PointsVie > 0:
                self.__PointsVie -= opposant.__niveau
                print(f'{self.__pseudo} à pris {opposant.__niveau} dégats !')
        elif self.__initiative < opposant.__initiative:
            self.__PointsVie -= opposant.__niveau
            print(f'{self.__pseudo} à pris {opposant.__niveau} dégats !')
            if self.__PointsVie > 0:
                opposant.__PointsVie -= self.__niveau
                print(f'{opposant.__pseudo} à pris {self.__niveau} dégats !')
        else:
            self.__PointsVie -= opposant.__niveau
            opposant.__PointsVie -= self.__niveau

    def combat(self, opposant):
        while self.__PointsVie > 0 and opposant.__PointsVie > 0:
            self.attaque(opposant)
            print(f"{self.__pseudo} a {self.__PointsVie} PV, {opposant.__pseudo} a {opposant.__PointsVie} PV")

    def soigner(self):
        self.__PointsVie = self.__niveau





Perso1 = Personnage("Eric", 100)
Perso2 = Personnage("Gregory", 120)
print(Perso1)
print(Perso2)
print(Perso1.combat(Perso2))