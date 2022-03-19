class Banque:
    __NomDirecteur = ""

    def __init__(self, adressSiege: str, capital: int):
        self.__adressSiege = adressSiege
        self.__capital = capital

    def getNomDirecteur(self) -> str:
        return self.__NomDirecteur

    def getCapital(self) -> int:
        return self.__Capital

    def getAdress(self) -> str:
        return self.__adressSiege

    def setNomDirecteur(self, nomDirecteur: str) -> None:
        if self.__NomDirecteur == "":
            self.__NomDirecteur = nomDirecteur

    def setCapital(self, montant: int) -> None:
        self.__Capital = montant

    def setAdress(self, adress: str) -> None:
        self.__adressSiege = adress

    def __str__(self):
        return f'''directeur de la banque : {self.__NomDirecteur}
adress : {self.__adressSiege}
Capital : {self.__Capital}'''
