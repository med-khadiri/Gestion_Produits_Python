from asyncio.proactor_events import _ProactorDuplexPipeTransport
from produit import Produit
class ProduitElectrique(Produit):
    def __init__(self,id,designation,prix,puissance,poids,dureeGar):
       super().__init__(id,designation,prix)
       self.setPuissance(puissance)
       self.setPoids(poids)  
       self.setDureeGar(dureeGar)     
     

    def getPuissance(self)  :
        return self.__puissance
    def getPoids(self)  :
        return self.__poids  
    def getDureeGar(self)  :
        return self.__dureeGar

    def setPuissance(self,puissance) :
        self.__puissance=puissance     

    def setPoids(self,poids) :
        self.__poids=poids   
    def setDureeGar(self,dureeGar) :
        self.__dureeGar=dureeGar 
    def __str__(self):
         return super().__str__()+'\t'+str(self.getPuissance())+'\t'+str(self.getPoids())+'\t'+ str(self.getDureeGar())

    def afficher(self):
        print("PE",self)
