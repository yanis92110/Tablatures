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
        while len(corde) < max_len:
            #probleme ici
            if(not str(corde[-1]).isdigit()):
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
    print(corde)
    print(case)
    try:
        index_corde = int(corde)  # Convertit l'entrée en index (0-5)
        print("Entré dans le try")
        if 0 <= index_corde < 6:
            print("Entré dans le if")
            tablature[index_corde].append(case)
            
        else:
            raise ValueError
    except ValueError:
        error_label.config(text="Erreur : veuillez entrer une corde (1-6) et une case valide.")
    afficher_tablature()
    

# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Création de Tablatures de Guitare")

# Affichage de la tablature
tablature_text = tk.Text(root, width=30, height=7)
tablature_text.pack()
afficher_tablature()  # Affiche la tablature initiale

# Entrées pour la corde et la case
frame_inputs = tk.Frame(root)
frame_inputs.pack()

tk.Label(frame_inputs, text="Corde (1-6):").grid(row=0, column=0)
entry_corde = tk.Entry(frame_inputs, width=5)
entry_corde.grid(row=0, column=1)

tk.Label(frame_inputs, text="Case:").grid(row=0, column=2)
entry_case = tk.Entry(frame_inputs, width=5)
entry_case.grid(row=0, column=3)

# Bouton pour ajouter la note
btn_ajouter = tk.Button(frame_inputs, text="Ajouter Note", command=ajouter_note)
btn_ajouter.grid(row=0, column=4)

Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)



for ligne in range(6):
    for colonne in range(10):
        if(colonne==1000):
            tk.Label(Frame1,text='Corde %s' % (ligne))
            #Button(Frame1, text='C%s' % (ligne), borderwidth=5).grid(row=ligne, column=colonne)
        
        Button(Frame1, text='%s' % (colonne), command=lambda ligne=ligne, colonne=colonne: ajouter_note(ligne,colonne), borderwidth=5).grid(row=ligne, column=colonne)
fill=Button(root, text='Finir la corde', command=lambda: ajouter_note_harmonieux())
fill.pack()
#bouton1=Button(Frame1,text="0", command=case_choix(0,0))

#outon1.pack()
#bouton2=Button(Frame1,text="0",command=NULL)
#bouton2.pack()
#bouton3=Button(Frame1,text="0",command=NULL""")
#bouton3.pack()
#bouton4=Button(Frame1,text="0",command=NULL""")
#bouton4.pack()
#bouton5=Button(Frame1,text="0",command=NULL""")
#bouton5.pack()
#bouton6=Button(Frame1,text="0",command=NULL""")
#bouton6.pack()
# Ajout de labels
#Label(Frame1, text="Frame 1").pack(padx=10, pady=10)

# Label d'erreur
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()