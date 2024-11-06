from tkinter import messagebox
from produit import Produit
from habit import Habit
import pickle as pk
from produit_electrique import ProduitElectrique
class Magasin:
    def __init__(self,nom):
        self.produits=list()
        self.currentProduit=None
        self.setNom(nom)



    def setNom(self,nom):
        if len(nom)>0:
             self.__nom=nom
        else:
            err= Exception("Attention La désignation du Magasin ne doit pas être vide !!!.")
            raise err

    def getNom(self):
        return self.__nom
        

    def ajouter(self) : 
        if  not self.exists(self.currentProduit.getId()):
            self.produits.append(self.currentProduit)
        else:
            ex=Exception("Un produit est déjà existant avec le même Id\nAjout refusé !!!")    
            raise ex
    def afficher(self)    :
        for item in self.produits:
            item.afficher()
    
    def afficherHabits(self)    :
        for item in self.produits:
            if isinstance(item,Habit):
                    item.afficher()

    def afficherProduitElectriques(self)    :
        for item in self.produits:
            if isinstance(item,ProduitElectrique):
                    item.afficher()
    def enregistrer(self):
        with open(self.getNom()+".dat","wb") as f:
            pk.dump(self.produits,f)

    def charger(self):
        with open(self.getNom()+".dat","rb") as f:
            self.produits=pk.load(f)
    def exists(self,id):
        existance =False
        for item in self.produits:
            if item.getId()==id:
                existance=True
                break
        return existance
    
    def chercherParId(self,id):
        self.currentProduit=None
        for item in self.produits:
            if int(item.getId())==id:
                self.currentProduit=item
                break
        if self.currentProduit is None:
            ex=Exception ("Aucun produit ne possède cet Id dans la liste !")
            raise ex
            
        return self.currentProduit
    

    def chercherPositionParId(self,id):
        i=0
        for item in self.produits:
            if int(item.getId())==id:
                break
            else:
                i+=1
            
        return i

    def supprimer(self):
        if self.currentProduit is None:
            ex=Exception("Il n'ya rien à supprimer !")
            raise ex
        else:
            self.produits.remove(self.currentProduit)
       

