from Compte import Compte


class CompteR(Compte):
    def __init__(self, solde: float, numero: int, taux: float):
        super().__init__(solde, numero)
        self.__taux = taux

    def getTaux(self) -> float:
        return self.__taux

    def setTaux(self, taux: float) -> None:
        self.__taux = taux

    def VerserInteret(self):
        pass
