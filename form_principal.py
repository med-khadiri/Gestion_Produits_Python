#from cProfile import label
#from cgitb import text
import tkinter as tk
from tkinter import Entry, messagebox
from tkinter.messagebox import YES

from form_produit import  FormProduit
class FormPrincipal:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Formulaire Principal")
        self.root.geometry("780x500")
        #self.root.iconbitmap("bing.ico")
        self.root.config(bg='#4465A4')
        self.label1=tk.Label(self.root,text="Bienvenue dans l'application Gestion des Produits",font="Arial 16 italic bold",bg='BLUE',fg='YELLOW')
        self.label1.pack(side=tk.TOP)
        self.frame1=tk.Frame(self.root,bd=1,relief="groove",padx=20,pady=20)

        self.btnGestProduit=tk.Button(self.frame1,text="Gestion des Produits",font=("Arial", 10, "italic", "bold"),bg="BLUE",fg='WHITE',bd=10,command=self.openGestionProduit)
        self.btnGestProduit.pack(side="left")

        self.btnGestHabit=tk.Button(self.frame1,text="Gestion des Habits",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.openGestionHabit)
        self.btnGestHabit.pack(side="left")

        self.btnGestProduitElect=tk.Button(self.frame1,text="Gestion des Produits Eléctriques",font="Arial 10 italic bold",bg="BLUE",fg='WHITE',bd=10,command=self.openGestionProduitElect)
        self.btnGestProduitElect.pack(side="right")
        

        self.btnQuitter=tk.Button(self.root,text="Quitter",font="Arial 16 italic bold",bg="red",fg='WHITE',bd=10,command=self.MessageQuitter)
        self.btnQuitter.pack(side=tk.BOTTOM)

        self.frame1.pack(expand=YES)
        self.root.mainloop()
    def MessageQuitter(self):
        if messagebox.askyesno("[Confirmation]","Etes vous sûr de vouloir Quitter ?"):
            self.root.destroy()
    

    
        
    def openGestionProduit(self):
        """""
        fenetre= tk.Tk()
        fenetre.title('Select File')
        fenetre.geometry("220x100")
        fenetre.minsize(height=100, width=220)
        fenetre.maxsize(height=100, width=220)
        fenetre.config(bg='#4465A4')
        frameInput=tk.Frame(fenetre)
        labelFile=tk.Label(frameInput,text="Nom du Magasin",font="Arial 10 italic bold")
        EntryFile=tk.Entry(frameInput)
        frameInput.pack(expand=1)
        labelFile.pack(side="top")
        EntryFile.pack(side="top")

        btnFile=tk.Button(fenetre,text="ok",font="Arial 12 italic bold",command=EntryFile.get)
        
        btnFile.pack(side="bottom")
        nom= EntryFile.get()
        
        fenetre.mainloop()
        """
        nom="produits"
        FormProduit(self.root,nom)
        
            
    def openGestionHabit(self):
        pass
    def openGestionProduitElect(self):
        pass
