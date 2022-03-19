class Agence:

    def __init__(self, adress:str, nomAgence:str):
        self.__AdressAgence = adress
        self.__NomAgance = nomAgence
        self.__listeClients = []
        self.__listesEmployer = []

    def getListeClients(self) -> list:
        return self.__listeClients

    def addClient(self, client) -> None:
        self.__listeClients.append(client)

    def getNomAgence(self) -> str:
        return self.__NomAgance

    def getAdress(self) -> str:
        return self.__AdressAgence

    def setNomAgence(self, nomAgence: str) -> None:
        self.__NomAgance = nomAgence

    def setAdress(self, adress: str) -> None:
        self.__AdressAgence = adress
    def addEmployer(self,employer)->None:
        self.__listesEmployer.append(employer)
    def getListesEmployer(self)->list:
        return self.__listesEmployer

    def __str__(self) -> str:
        return f'''Nom de l'agence : {self.__NomAgance}
Adress : {self.__AdressAgence}
listes des employer : {self.getListesEmployer()}
listes des clients : {self.getListeClients()}'''
