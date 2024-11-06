from produit import Produit
from magasin import Magasin
from clavier import Clavier
import os

os.system('cls')
choix=0
m=Magasin()

while choix!=9:
    choix=int(input("1. Ajouter Produit \n2. Afficher Tout \n3. Ajouter Habit\n4. Ajouter Electrique\n5. Afficher Habits\n6. Afficher Produits Elect.\n7. Enregistrer\n8. Charger\n9. Quitter\nVotre choix?\n"))
    if choix==1:
       try:
          m.ajouter(Clavier.getProduit())
       except Exception as ex:
          print(ex)
       os.system('pause')


    elif choix==2:
       m.afficher()
       os.system('pause')
    elif choix==3:
         m.ajouter(Clavier.getHabit())
    elif choix==4:
         m.ajouter(Clavier.getProduitElect())

    elif choix==5:
       m.afficherHabits()
       os.system('pause')
    elif choix==6:
       m.afficherProduitElectriques()
       os.system('pause')
    elif choix==7:
       m.enregistrer()
    elif choix==8:
       try:
          m.charger()   
       except Exception as ex:
          print(ex)
          os.system('pause') 
    os.system('cls')    