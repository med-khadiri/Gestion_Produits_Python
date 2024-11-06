from produit import Produit
from habit import Habit
from produit_electrique import ProduitElectrique
class Clavier:
    @staticmethod
    def getProduit():
        error=True
        p=None
        while error:
            try:
                p=Produit(Clavier.getInt("Tapez Id du produit"),Clavier.getString("Tapezle nom du produit"),Clavier.getfloat("Tapezle prix du produit"))
                error=False
            except Exception as ex:
                print(ex)
        return p
    
    @staticmethod
    def getHabit():
        return   Habit(Clavier.getInt("Tapez Id du produit ? "),Clavier.getString("Tapezle nom du produit ? "),Clavier.getfloat("Tapez le prix du produit ? "),Clavier.getString("Tapez la couleur du produit ? "),Clavier.getString("Tapez la taille du produit ? "))
        
    @staticmethod
   
    def getProduitElect():
        return ProduitElectrique(Clavier.getInt("Tapez Id du produit ? "),Clavier.getString("Tapezle nom du produit ? "),Clavier.getfloat("Tapez le prix du produit ? "),Clavier.getfloat("Tapez la puissance du produit ? "),Clavier.getInt("Tapez le poids du produit ? "),Clavier.getInt("Tapez la durée de garantie du produit ? "))
        
    @staticmethod
    def getString(msg):
        return input(msg)
    @staticmethod
    def getInt(msg):
        error=True
        n=0
        while error:
            try:
                n= int(Clavier.getString(msg))
                error=False
            except Exception as ex:
                print(ex)
        return n

    @staticmethod
    def getfloat(msg):
        error=True
        n=0
        while error:
            try:
                n= float(Clavier.getString(msg))
                error=False
            except Exception as ex:
                print(ex)
        return n