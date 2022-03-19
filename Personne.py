class Personne:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

    def setNom(self, nom: str) -> None:
        self.__nom = nom

    def setPrenom(self, prenom: str) -> None:
        self.__prenom = prenom

    def getNom(self) -> str:
        return self.__nom

    def getPrenom(self) -> str:
        return self.__prenom

    def __str__(self) -> str:
        return f'''Nom : {self.__nom}
Prenom : {self.__prenom}'''
