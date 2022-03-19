from Agence import Agence
from Compte import Compte
from Personne import Personne


class Client(Personne):

    def __init__(self, nom: str, prenom: str, agence: Agence):
        super().__init__(nom, prenom)
        agence.addClient(self)
        self.__Adress = agence.getAdress()
        self.__listeComptes = []


    def addCompte(self, compte: Compte) -> None:
        self.__listeComptes.append(compte)

    def getListeComptes(self) -> str:
        for compte in self.__listeComptes:
            print(compte)

    def setAgence(self, agence: Agence) -> None:
        self.__Adress = agence.getAdress()

    def getAgence(self) -> str:
        return self.__Adress

    def __str__(self) -> str:
        return f'''{super().__str__()}
{self.__Adress}
liste des comptes :
{self.getListeComptes()}'''
