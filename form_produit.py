


import tkinter as tk
from tkinter import DISABLED, StringVar, messagebox
from turtle import width
from tkinter import tix
from magasin import Magasin
from produit import Produit
class FormProduit:
    def __init__(self,fenetreMere,nom) :
        self.magasin=Magasin(nom)
        self.position=0
        self.fenetreMere=fenetreMere
        self.fenetreMere.withdraw() #iconify()
        self.root=tix.Tk()
        self.root.title("Gestion des Produits")
        self.root.config(bg='#4465A4')
        self.root.geometry("1200x550")
        self.root.resizable("false","false")
        #self.root.iconbitmap("bing.ico")
        self.sw=tix.ScrolledWindow(self.root)
        
        
        

        self.label=tk.Label(self.root,text="Mise à jour des Produits",font="Arial 16 italic bold",bg='BLUE',fg='YELLOW')
        self.label.pack(side='top')
        ###################### Frame d'Actions ####################################
        self.frameInput=tk.LabelFrame(self.root,bd=1,relief="sunken",text="Input",padx=10,pady=20,bg='#4465A4')
        self.labalId=tk.Label(self.frameInput,text="Id",font="Arial 16 italic",justify="left",bg='#4465A4',fg="WHITE")
        self.labalId.grid(row=0,column=0,sticky=tk.W)
        self.entryId=tk.Entry(self.frameInput,font="Arial 16 italic")
        self.entryId.grid(row=0,column=1)

        self.labalDes=tk.Label(self.frameInput,text="Désignation",font="Arial 16 italic",bg='#4465A4',fg="WHITE")
        self.labalDes.grid(row=1,column=0,sticky=tk.W)
        self.entryDes=tk.Entry(self.frameInput,font="Arial 16 italic")
        self.entryDes.grid(row=1,column=1)

        self.labalPrix=tk.Label(self.frameInput,text="Prix",font="Arial 16 italic",bg='#4465A4',fg="WHITE")
        self.labalPrix.grid(row=2,column=0,sticky=tk.W)
        self.entryPrix=tk.Entry(self.frameInput,font="Arial 16 italic")
        self.entryPrix.grid(row=2,column=1)

        self.frameInput.place(x=20,y=100)
        self.sw.pack(side="right")
        #################### Bouttons d'actions #################################################
        self.frameButton=tk.Frame(self.root,bd=1,relief="groove",padx=20,pady=20,bg='#4465A4')
        self.frameButton.place(x=20,y=340)
        

        self.btnAjouter=tk.Button(self.frameButton,text="Ajouter",font=("Arial", 10, "italic", "bold"),bg="BLUE",fg='WHITE',pady=10,bd=10,command=self.ajouter)
        self.btnAjouter.pack(side="left")

        self.btnSupprimer=tk.Button(self.frameButton,text="Supprimer",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.supprimer)
        self.btnSupprimer.pack(side="left")

        self.btnModifier=tk.Button(self.frameButton,text="Modifier",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.modifier)
        self.btnModifier.pack(side="left")
        self.btnEffacer=tk.Button(self.frameButton,text="Actualiser",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.effacerEntry)
        self.btnEffacer.pack(side="left")
        self.btnChercher=tk.Button(self.frameButton,text="Chercher",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.chercher)
        self.btnChercher.pack(side="left")
        ############################## Removed From Action Buttons #########################################
        self.btnAfficher=tk.Button(self.frameButton,text="Actualiser",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.afficher)
        #self.btnAfficher.pack(side="left")
        self.btnSave=tk.Button(self.frameButton,text="Enregistrer",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.save)
        self.btnSave.pack(side="left")
        self.btnLoad=tk.Button(self.frameButton,text="Charger",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.load)
        self.btnLoad.pack(side="left")
        ############### Liste de Produits ###############
        self.framelist=tk.LabelFrame(self.sw.window,relief="sunken",text="Liste de Produits")
        self.framelist.pack()
        self.labelIdlist=tk.Label(self.framelist,text="id",font="Arial 10 italic bold",padx=40)
        
        self.labelDeslist=tk.Label(self.framelist,text="designation",font="Arial 10 italic bold",padx=40)
        
        self.labelPrixlist=tk.Label(self.framelist,text="Prix",font="Arial 10 italic bold",padx=40)
        self.labelIdlist.grid(row=0,column=0,sticky=tk.W)
        self.labelDeslist.grid(row=0,column=1,sticky=tk.W)
        self.labelPrixlist.grid(row=0,column=2,sticky=tk.W)
        ######################################################
        ########################## Bouttons de Navigation ############################
        self.btnNav=tk.LabelFrame(self.root,bg='#4465A4')
        
        self.btnSuivant=tk.Button(self.btnNav,text="Suivant",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',padx=10,bd=10,command=self.suivant)
        self.btnSuivant.grid(row=0,column=6)
        self.btnPrecedent=tk.Button(self.btnNav,text="Précédent",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.precedent)
        self.btnPrecedent.grid(row=0,column=0)
        self.framSpace=tk.Frame(self.btnNav,bg='#4465A4')
        self.framSpace.grid(row=0,column=2,padx=105)

        self.btnNav.place(x=15,y=270)
        









        ###############################################################################
        
        ############## Boutton Quitter ####################
        self.btnFermer=tk.Button(self.root,text="Fermer",font=("Arial", 16, "italic", "bold"),bg="red",fg='WHITE',bd=10,command=self.fermer)
       
        self.btnFermer.pack(side=tk.BOTTOM)
        
        self.root.mainloop()

    def fermer(self):
    
        if messagebox.askyesno("[Confirmation]","Voulez-vous sauvegarder avand de quitter ?"):
            self.save()
            self.fenetreMere.deiconify()
            self.root.destroy()
        else:
            self.fenetreMere.deiconify()
            self.root.destroy()

    def ajouter(self):
        try:    
            self.magasin.currentProduit=Produit(int(self.entryId.get()),self.entryDes.get(),float(self.entryPrix.get()))        
            self.magasin.ajouter()
            
            self.effacerEntry()
            self.entryId.focus_set()
            
        except Exception as ex:
            messagebox.showinfo("[Erreur]",ex)
        self.afficher()
        

    def effacerEntry(self):
        self.entryId.delete(0,tk.END)
        self.entryDes.delete(0,tk.END)
        self.entryPrix.delete(0,tk.END)
        self.magasin.currentProduit=None

    def supprimer(self):
           if  not self.magasin.currentProduit is None:
                if messagebox.askyesno("[Confirmation]","Etes vous sûr de vouloir supprimer ce produit ?"):
                    try:
                        self.magasin.supprimer()
                        self.framelist.destroy()
                        self.constructList()
                        self.afficher()
                        self.effacerEntry()
                        messagebox.showinfo("[Information]","Element Supprimé!")
                        
                    except Exception as ex:
                        messagebox.showwarning("Exclamation",ex)
           else:
                messagebox.showwarning("[Exclamation]","Faites une recherche d'abord !")
           self.afficher()        

        

    def modifier(self):
            try:
                
                self.magasin.currentProduit.setDesignation(self.entryDes.get())
                self.magasin.currentProduit.setPrix(float(self.entryPrix.get()))
                messagebox.showinfo("[Information]","Le Produit s'est modifié avec succés!")
                
                
            except Exception as ex:
                messagebox.showerror("[Erreur]",ex)
            self.afficher()
    
    def chercher(self):
            try:
                self.magasin.chercherParId(int(self.entryId.get()))
                self.entryId.delete(0,tk.END)
                self.entryId.insert(0,self.magasin.currentProduit.getId())
                self.entryDes.delete(0,tk.END)
                self.entryDes.insert(0,self.magasin.currentProduit.getDesignation())
                self.entryPrix.delete(0,tk.END)
                self.entryPrix.insert(0,self.magasin.currentProduit.getPrix())
                self.position=self.magasin.chercherPositionParId(int(self.entryId.get()))
            except Exception as ex:
                messagebox.showinfo("[Erreur]",ex)
                self.effacerEntry()
            self.entryId.focus_set()    


    def afficher(self):
        
        i=1
        for item in self.magasin.produits:
            self.entryIdFrame= tk.Entry(self.framelist)
            self.entryIdFrame.insert(0,item.getId())
            self.entryIdFrame.config(state=DISABLED)
            
            self.entryIdFrame.grid(row=i,column=0)

            self.entryDesFrame= tk.Entry(self.framelist)
            self.entryDesFrame.insert(0,item.getDesignation())
            self.entryDesFrame.config(state=DISABLED)
            
            self.entryDesFrame.grid(row=i,column=1)

            self.entryPrixFrame= tk.Entry(self.framelist)
            self.entryPrixFrame.insert(0,item.getPrix())
            self.entryPrixFrame.config(state=DISABLED)
            
            self.entryPrixFrame.grid(row=i,column=2)
            i+=1
        

    def suivant(self):
        if self.position<len(self.magasin.produits)-1:
            self.position+=1
            self.magasin.currentProduit=self.magasin.produits[self.position]
            self.affecter()
    def precedent(self):
        if self.position>0:
            self.position-=1
            self.magasin.currentProduit=self.magasin.produits[self.position]
            self.affecter()        

    def affecter(self):
        self.entryId.delete(0,tk.END)
        self.entryId.insert(0,self.magasin.currentProduit.getId())
        self.entryDes.delete(0,tk.END)
        self.entryDes.insert(0,self.magasin.currentProduit.getDesignation())
        self.entryPrix.delete(0,tk.END)
        self.entryPrix.insert(0,self.magasin.currentProduit.getPrix())


    def constructList(self):
        self.framelist=tk.LabelFrame(self.sw.window,relief="sunken",text="Liste de Produits")
        self.framelist.pack()
        self.labelIdlist=tk.Label(self.framelist,text="id",font="Arial 10 italic bold",padx=40)
        
        self.labelDeslist=tk.Label(self.framelist,text="designation",font="Arial 10 italic bold",padx=40)
        
        self.labelPrixlist=tk.Label(self.framelist,text="Prix",font="Arial 10 italic bold",padx=40)
        self.labelIdlist.grid(row=0,column=0,sticky=tk.W)
        self.labelDeslist.grid(row=0,column=1,sticky=tk.W)
        self.labelPrixlist.grid(row=0,column=2,sticky=tk.W)
    def save(self):
        if messagebox.askyesno("[Confirmation]","Etes-Vous sûr de vouloir Enregistrer ?"):
            try:
                self.magasin.enregistrer()
                messagebox.showinfo('[Information]',"La liste a été enregistrer avec succée!")
            except Exception as ex:
                messagebox.showerror("[Error]",ex)
    def load(self):
        try:
            self.magasin.charger()
            self.afficher()
        except Exception as ex:
            messagebox.showerror("[Error]",ex)