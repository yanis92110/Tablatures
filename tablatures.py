import tkinter as tk
from tkinter import *
from pynput.keyboard import Listener
import keyboard

global continuer,selecteur
selecteur = 0
continuer = True



# Initialisation de la tablature
corde_mi_grave = ["--"]
corde_la = ["--"]
corde_re = ["--"]
corde_sol = ["--"]
corde_si = ["--"]
corde_mi_aigu = ["--"]

tablature = [corde_mi_grave, corde_la, corde_re, corde_sol, corde_si, corde_mi_aigu]


# Fonction pour maintenir l'alignement
def ajouter_note_harmonieux():
    max_len = max(len(c) for c in tablature)
    for corde in tablature:
        if len(corde) < max_len:
            while(len(corde) < max_len):
                corde.append("--")
    continuer = True
    afficher_tablature()
#Fonction pour ajouter une note

# Fonction d'affichage de la tablature
def afficher_tablature():
    tablature_text.delete("1.0", tk.END)  # Efface le texte existant
    cordes_noms = ["E ", "A ", "D ", "G ", "B ", "e "]
    for i, corde in enumerate(tablature):
        ligne = cordes_noms[i] + "| " + " ".join(str(note) for note in corde) + "\n"
        tablature_text.insert(tk.END, ligne)

# Fonction déclenchée par le bouton "Ajouter"
def ajouter_note(corde, case,selecteur):
    print(f"Selecteur dans ajouter_note:{selecteur}")
    index_corde = int(corde)  # Convertit l'entrée en index (0-5)
    if 0 <= index_corde < 6:
        if case == "p":
            case=case+"-"
        elif case=="⌢":
            case="⌢"+" "
        elif case<10:
            case = str(case)+"-"

        tablature[index_corde][selecteur] = case

    afficher_tablature()
    

# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Création de Tablatures de Guitare")

# Affichage de la tablature
tablature_text = tk.Text(root, width=30, height=7)
tablature_text.pack()
afficher_tablature()  # Affiche la tablature initiale


Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
Frame1.pack(side=TOP, padx=30, pady=3)



for ligne in range(6):
    for colonne in range(17):        
        Button(Frame1, text='%s' % (colonne), command=lambda ligne=ligne, colonne=colonne, selecteur=selecteur: ajouter_note(ligne, colonne,selecteur), borderwidth=5).grid(row=ligne, column=colonne, pady=5)
    Button(Frame1, text="⌢", command=lambda ligne=ligne, colonne=colonne, selecteur=selecteur: ajouter_note(ligne, "⌢",selecteur), borderwidth=5).grid(row=ligne, column=colonne+1, pady=5)
    Button(Frame1, text="p", command=lambda ligne=ligne, colonne=colonne, selecteur=selecteur: ajouter_note(ligne, "p",selecteur), borderwidth=5).grid(row=ligne, column=colonne+2, pady=5)
fill=Button(root, text='Finir la corde', command=lambda: ajouter_note_harmonieux())
fill.pack()

def on_key_event(event):
    global selecteur
    if event.name=="gauche":
        if selecteur>0:
            selecteur-=2
        print("gauche")
    elif event.name=="droite":
        print("droite")
        max_len = max(len(c) for c in tablature)
        if selecteur<max_len:
            selecteur+=2
        else:
            for corde in tablature:
                corde.append("--")
            selecteur+=2
    print(f"Selecteur dans on_key_event:{selecteur}")

keyboard.on_press(on_key_event)
# Fonction pour détecter qu'un bouton est cliqué
def bouton_clique(event):
    global continuer
    if not continuer:
        print("TEst")
        return
    print(f"Bouton cliqué: {event.widget}")
    continuer = False


# Liaison de l'événement de clic de bouton
for widget in Frame1.winfo_children():
    if isinstance(widget, Button):
        widget.bind("<Button-1>", bouton_clique)

# Label d'erreur
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()