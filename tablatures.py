import tkinter as tk
from tkinter import *

# Initialisation de la tablature
corde_mi_grave = ["-"]
corde_la = ["-"]
corde_re = ["-"]
corde_sol = ["-"]
corde_si = ["-"]
corde_mi_aigu = ["-"]

tablature = [corde_mi_grave, corde_la, corde_re, corde_sol, corde_si, corde_mi_aigu]

# Fonction pour maintenir l'alignement
def ajouter_note_harmonieux():
    print("Entrer dans note harmonieux")
    max_len = max(len(c) for c in tablature)
    for corde in tablature:
        if len(corde) < max_len:
            while(len(corde) < max_len):
                corde.append("-")

    afficher_tablature()
    print("Sorti de note harmonieux")
#Fonction pour ajouter une note

# Fonction d'affichage de la tablature
def afficher_tablature():
    print("Entrer dans affichaer tablature")
    tablature_text.delete("1.0", tk.END)  # Efface le texte existant
    cordes_noms = ["E ", "A ", "D ", "G ", "B ", "e "]
    for i, corde in enumerate(tablature):
        ligne = cordes_noms[i] + "| " + " ".join(str(note) for note in corde) + "\n"
        tablature_text.insert(tk.END, ligne)

# Fonction déclenchée par le bouton "Ajouter"
def ajouter_note(corde, case):
    index_corde = int(corde)  # Convertit l'entrée en index (0-5)
    if 0 <= index_corde < 6:
        tablature[index_corde].append(case)
        if case != "⌢":
            tablature[index_corde].append(" ")

    afficher_tablature()
    

# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Création de Tablatures de Guitare")

# Affichage de la tablature
tablature_text = tk.Text(root, width=30, height=7)
tablature_text.pack()
afficher_tablature()  # Affiche la tablature initiale


Frame2 = Frame(root, borderwidth=2, relief=GROOVE)
Frame2.pack(side=TOP,padx=10)
#Button(Frame2,text="⌢", command=lambda ajouter_note)
tk.Label(Frame2, text="⌢").grid(row=0, column=0)

Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
Frame1.pack(side=TOP, padx=30, pady=3)



for ligne in range(6):
    for colonne in range(16):        
        Button(Frame1, text='%s' % (colonne), command=lambda ligne=ligne, colonne=colonne: ajouter_note(ligne, colonne), borderwidth=5).grid(row=ligne, column=colonne, pady=5)
    Button(Frame1, text="⌢", command=lambda ligne=ligne, colonne=colonne: ajouter_note(ligne, "⌢"), borderwidth=5).grid(row=ligne, column=colonne+1, pady=5)
fill=Button(root, text='Finir la corde', command=lambda: ajouter_note_harmonieux())
fill.pack()


# Label d'erreur
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()