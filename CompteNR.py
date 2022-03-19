from Compte import Compte


class CompteNR(Compte):
    def __init__(self, solde: float, numero: int) -> None:
        super().__init__(solde, numero)
