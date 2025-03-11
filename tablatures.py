

#from fonctions import *
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import keyboard

global selecteur
selecteur=0

def afficher_tablature():
    global selecteur
    tablature_text.delete("1.0", tk.END)  # Efface le texte existant
    cordes_noms = ["E ", "A ", "D ", "G ", "B ", "e "]
    for i, corde in enumerate(tablature):
        ligne = cordes_noms[i] + "| " + " ".join(str(note) for note in corde) + "\n"
        tablature_text.insert(tk.END, ligne)
    # Colorier la colonne du sélecteur
    for i in range(6):
        start_index = f"{i + 1}.{selecteur * 4}"
        end_index = f"{i + 1}.{selecteur * 4 + 2}"
        tablature_text.tag_add("highlight", start_index, end_index)
    tablature_text.tag_config("highlight", background="yellow")

# Fonction pour maintenir l'alignement
def ajouter_note_harmonieux():
    max_len = max(len(c) for c in tablature)
    for corde in tablature:
        if len(corde) < max_len:
            while(len(corde) < max_len):
                corde.append("--")
    continuer = True
    afficher_tablature()

def corde_vide():
    for corde in tablature:
        corde.append("--")
    afficher_tablature()

def supprimer_corde():
    for corde in tablature:
        corde.pop()
    afficher_tablature()

def ajouter_note(corde, case,selecteur):
    index_corde = int(corde)  # Convertit l'entrée en index (0-5)
    if case == "p":
        case=case+"-"
    elif case=="⌢":
        case="⌢"+" "
    elif case<10:
        case = str(case)+"-"
    if selecteur==max(len(c) for c in tablature):

        tablature[index_corde].append(case)
        #selecteur+=2
    else:
        #tablature[index_corde].insert(selecteur, case) code copilot
        tablature[index_corde][selecteur]=case

    afficher_tablature()
def quitter_application():
    if tk.messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'application?"):
        root.quit()


def sauvegarder_tablature():
    # Demande à l'utilisateur de choisir un emplacement de sauvegarde
    fichier = open(f"C:/Users/Yanis/Documents/tablatures/{nom_fichier}.txt", "w")  # Ouvre le fichier en écriture
    if fichier is None:  # Si l'utilisateur annule
        return

    # Écriture de la tablature dans le fichier
    for corde in tablature:
        fichier.write(" ".join(str(note) for note in corde) + "\n")

    fichier.close()  # Ferme le fichier
    error_label.config(text="Tablature enregistrée avec succès", fg="green")

def on_key_event(event):
    print("Entré dans on_key_event")
    global selecteur
    if event.name=="enter":
        ajouter_note_harmonieux()
        selecteur=len(tablature[0])-1
    if event.name=="gauche":
        if selecteur>0:
            if selecteur-2<0:
                selecteur=0
            else:
                selecteur-=2
    elif event.name=="droite":
        max_len = max(len(c) for c in tablature)
        print(max_len)
        if selecteur<max_len:
            if selecteur+2>max_len:
                selecteur=max_len
            else:
                selecteur+=2
    print(f"Selecteur dans on_key_event:{selecteur}")
    afficher_tablature()
    return selecteur

def bouton_clique(event):

    print(f"Bouton cliqué: {event.widget}")

def ajouter_note_avec_selecteur(ligne, case):
    global selecteur
    ajouter_note(ligne, case, selecteur)


print("Entrer un nom de fichier")

nom_fichier=input()
# Initialisation de la tablature
corde_mi_grave = ["--"]
corde_la = ["--"]
corde_re = ["--"]
corde_sol = ["--"]
corde_si = ["--"]
corde_mi_aigu = ["--"]

tablature = [corde_mi_grave, corde_la, corde_re, corde_sol, corde_si, corde_mi_aigu]


# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Création de Tablatures de Guitare")


# Affichage de la tablature de base
tablature_text = tk.Text(root, width=300, height=7)
Label(root, text=nom_fichier, font=("Helvetica", 16)).pack()
tablature_text.pack()
afficher_tablature()  # Affiche la tablature initiale


Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
Frame1.pack(side=TOP, padx=30, pady=3)

print(f"Le selecteur vaut: {selecteur}")

#Création des boutons de notes
for ligne in range(6):
    for colonne in range(17):        
        Button(Frame1, text='%s' % (colonne), command=lambda ligne=ligne, colonne=colonne: ajouter_note_avec_selecteur(ligne, colonne), borderwidth=5).grid(row=ligne, column=colonne, pady=5)
    Button(Frame1, text="⌢", command=lambda ligne=ligne, colonne=colonne: ajouter_note_avec_selecteur(ligne, "⌢"), borderwidth=5).grid(row=ligne, column=colonne+1, pady=5)
    Button(Frame1, text="p", command=lambda ligne=ligne, colonne=colonne: ajouter_note_avec_selecteur(ligne, "p"), borderwidth=5).grid(row=ligne, column=colonne+2, pady=5)


# Use a frame to organize the buttons
button_frame = Frame(root, borderwidth=2, relief=GROOVE)
button_frame.pack(side=BOTTOM, pady=10)

fill=Button(button_frame, text='Finir la corde', command=lambda: ajouter_note_harmonieux())
fill2=Button(button_frame, text='Vide', command=lambda: corde_vide())
fill3=Button(button_frame, text='Supprimer', command=lambda: supprimer_corde())
fill4=Button(button_frame, text='Enregistrer', command=lambda: sauvegarder_tablature())
fill5=Button(button_frame, text='Quitter', command=quitter_application)
fill6=Button(button_frame, text='test', command=lambda: keyboard.on_press(on_key_event))

fill.pack(side=LEFT, padx=5)
fill2.pack(side=LEFT, padx=5)
fill5.pack(side=RIGHT, padx=5)
fill4.pack(side=RIGHT, padx=5)
fill3.pack(side=RIGHT, padx=5)
fill6.pack(side=RIGHT, padx=5)




keyboard.on_press(on_key_event)
# Fonction pour détecter qu'un bouton est cliqué

# Liaison de l'événement de clic de bouton
for widget in Frame1.winfo_children():
    if isinstance(widget, Button):
        widget.bind("<Button-1>", bouton_clique)

# Label d'erreur
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()