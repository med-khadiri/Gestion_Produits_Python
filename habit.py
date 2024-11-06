from produit import Produit
class Habit(Produit):
    def __init__(self,id,designation,prix,couleur,taille):
       super().__init__(id,designation,prix)
       self.setCouleur(couleur)
       self.setTaille(taille)     
     

    def getCouleur(self)  :
        return self.__couleur
    def getTaille(self)  :
        return self.__taille  

    def setCouleur(self,couleur) :
        self.__couleur=couleur     

    def setTaille(self,taille) :
        self.__taille=taille   

    def __str__(self):
         return super().__str__()+'\t'+self.getCouleur()+'\t'+self.getTaille()

    def afficher(self):
        print("H ",self)