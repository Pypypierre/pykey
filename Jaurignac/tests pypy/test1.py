from tkinter import * 
from tkinter import messagebox
import tkinter.font as font 
import os 



fenetre = Tk ()
fenetre.attributes('-topmost', True)
label = Label(fenetre, text="Did it")
label.pack()
f = font.Font(weight="bold")
logo = BitmapImage('logo.jpg')
Label(image = logo ).grid
bouton = Button(fenetre, text="Fermer",fg="cyan", width=50, height=100, command=fenetre.quit)
bouton['font'] = f 
bouton.pack(side=RIGHT)
bouton1 = Button(fenetre, fg="blue", text="Scan", width=50, height=100, command= fenetre.quit )
bouton1.pack(side=LEFT)
bouton1['font'] = f

liste = Listbox(fenetre)
liste.insert(1, "Scan clé")
liste.insert(2, "Charger clé")
liste.select_set(0)
liste.pack()

fenetre.mainloop()
