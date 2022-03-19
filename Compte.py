class Compte:
    def __init__(self, solde: float, numero: int):
        self.__solde = solde
        self.__numero = numero

    def setSolde(self, solde: float) -> None:
        self.__solde = solde

    def setNumero(self, numero: int) -> None:
        self.__numero = numero

    def getSolde(self) -> float:
        return self.__solde

    def getNumero(self) -> int:
        return self.__numero

    def __str__(self) -> str:
        return f'''Numero du compte : {self.__numero}
Solde : {self.__solde}'''
