from tkinter import * 
from tkinter import messagebox
import tkinter.font as font 
import os 
i=1 

while :
	def scan() : 
		print("hey")
		os.system('echo PJ est un beau gosse')
		boutonbis = Button(fenetre, text="lancer la copie", bg="blue", fg="white", height=5, command=fenetre.quit) 
		boutonbis.pack()
		exit

	fenetre = Tk ()
	fenetre.attributes('-fullscreen', True)
	label = Label(fenetre, text="Did it")
	label.pack()
	f = font.Font(weight="bold")

	bouton = Button(fenetre, text="Fermer",fg="blue", width=50, height=100, command=fenetre.quit)
	bouton['font'] = f 
	bouton.pack(side=RIGHT)

	bouton1 = Button(fenetre, fg="blue", text="Scan", width=50, height=100, command= scan )
	bouton1.pack(side=LEFT)
	bouton1['font'] = f

	liste = Listbox(fenetre)
	liste.insert(1, "Scan clé")
	liste.insert(2, "Charger clé")
	liste.select_set(0)
	liste.pack()

	fenetre.mainloop()
