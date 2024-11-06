class Produit:
   def __init__(self,id,designation,prix):
       self.setId(id)
       self.setDesignation(designation)
       self.setPrix(prix)
   
   def getId(self):
        return self.__id
   def getDesignation(self):

        return self.__designation
   def getPrix(self):
        return self.__prix
   def setId(self,id):
        if id>0:
             self.__id=str(id)
        else:
             err= Exception("Attention Le code du produit doit être strictement positif !!!.")
             raise err

   def setDesignation(self,designation):
         if len(designation)>0:
             self.__designation=designation
         else:
             err= Exception("Attention La désignation du produit ne doit pas être vide !!!.")
             raise err
   def setPrix(self,prix):
         if prix>0:
             self.__prix=prix  
         elif prix==0:
              self.__prix="FREE"
         else:
               err= Exception("Attention Le prix du produit doit être strictement positif !!!.")
               raise err


             
        
  
   def __str__(self)   :
        return str(self.getId()) +'\t' +self.getDesignation() +'\t'+ str(self.getPrix())
   
   def afficher(self):
        print("P ",self) 
