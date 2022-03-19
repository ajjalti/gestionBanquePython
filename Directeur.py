from Banque import Banque
from Personne import Personne


class Directeur(Personne):
    def __init__(self, nom: str, prenom: str, revenu: float, banque: Banque):
        super().__init__(nom, prenom)
        self.__revenu = revenu
        self.__Banque = banque
        self.__Banque = banque
        banque.setNomDirecteur(nom)

    def getRevenu(self) -> float:
        return self.__revenu

    def setRevenu(self, montant: float) -> None:
        self.__revenu = montant

    def __str__(self) -> str:
        return f'''{super().__str__()}
Revenu : {self.__revenu}
Banque : {self.__Banque.getAdress()}'''
