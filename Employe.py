from Agence import Agence
from Client import Client
from CompteNR import CompteNR
from CompteR import CompteR
from Personne import Personne


class Employe(Personne):

    def __init__(self, nom: str, prenom: str, dateEmbauche: str, agence: Agence):
        super().__init__(nom, prenom)
        self.__dateEmbauche = dateEmbauche
        agence.addEmployer(self)
        self.__listeClients = []


    def getDateDembauche(self) -> str:
        return self.__dateEmbauche

    def setDateDembauche(self, date: str) -> None:
        self.__dateEmbauche = date

    def CreeCompteR(self, client: Client, solde: float, numero: int, taux: float) -> None:
        client.addCompte(CompteR(solde, numero, taux))
        self.__listeClients.append(client)

    def CreeCompteNR(self, client: Client, solde: float, numero: int) -> None:
        client.addCompte(CompteNR(solde, numero))
        self.__listeClients.append(client)

    def getListeClients(self) -> list:
        return self.__listeClients
