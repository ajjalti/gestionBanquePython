from Banque import Banque
from Client import Client
from CompteNR import CompteNR
from Directeur import Directeur
from Employe import Employe
from Agence import Agence


banque= Banque("centre Berkane",100000000)
directeur = Directeur("ajjalti","ahmed",1000,banque)
#print(banque1)
#print(directeur)
agence = Agence("oujda","happy")
employe = Employe("nom","prenom","12/2/1990",agence)
client = Client("ajjalti","ahmed",agence)
print(agence)
#print(client)
employe.CreeCompteNR(client,1000,12)
comte = CompteNR(1000,13)
print(client)

#print(agence)