from tkinter import *
from tkinter.messagebox import *


fenetre = Tk()
#label
label = Label(fenetre,text="Hello World !",bg="yellow")
label.pack()

#Bouton de sortie

bouton=Button(fenetre,text="Fermer",command=fenetre.quit)
bouton.pack()

#entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str, width=30)
entree.pack()

#checkbox

box = Checkbutton(fenetre,text="Nouveau ?")
box.pack()

# radiobutton
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peu être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

# liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

# canvas
canvas = Canvas(fenetre, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()

"""
create_arc()        :  arc de cercle
create_bitmap()     :  bitmap
create_image()      :  image
create_line()       :  ligne
create_oval()       :  ovale
create_polygon()    :  polygone
create_rectangle()  :  rectangle 
create_text()       :  texte
create_window()     :  fenetre

 Si vous voulez changer les coordonnées d'un élement crée dans le canevas, vous pouvez utiliser la méthode coords .

canvas.coords(élément, x0, y0, x1, y1)

"""
value = DoubleVar()
scale = Scale(fenetre, variable=value)
scale.pack()


fenetre['bg']='white'

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)

#Permet de choisir des chiffres
s = Spinbox(fenetre, from_=0, to=10)
s.pack()

# Le labelframe est un cadre avec un label.

l = LabelFrame(fenetre, text="Titre de la frame", padx=20, pady=20)
l.pack(fill="both", expand="yes")
 
Label(l, text="A l'intérieure de la frame").pack()

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

Button(text='Action', command=callback).pack()

def clavier(event):
    touche = event.keysym
    print(touche)

canvas = Canvas(fenetre, width=500, height=500)
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()

fenetre.mainloop()