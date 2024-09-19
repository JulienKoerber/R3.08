from Personnage import Personnage
class Guerrier(Personnage):
    def __init__(self, pseudo : str, niveau = 1):
        super().__init__(pseudo, niveau, niveau)