from tkinter import * 
from tkinter import messagebox
import tkinter.font as font 
import os 
from subprocess import *


def scan():
	exit()
def restart():
	exit()
def shutdown():
	exit()

fenetre = Tk()
fenetre.attributes('-topmost', True)
f = font.Font(weight="bold")
menubar = Menu(fenetre)
fenetre.config(menu=menubar)

fenetre.title('Super Jaurignac')

label1 = Label(fenetre, text=("Utilitaire clé"))

label1.pack()

bouton1 = Button(fenetre, fg="blue", text="Scan", width=50, height=100, command= scan )
bouton1.pack()
#logo = BitmapImage('/Bureau/Jaurignac/logo.jpg')
#menu1 = Menu(menubar, title="Super Jaurignac")
#menubar.add_cascade(label(image = logo), menu=menu1)
#menubar.add_title("Utilitaire clé")

menu2 = Menu(menubar)
menu2.add_command(label="Quitter", command = fenetre.quit)
menu2.add_command(label="Redémarrer", command = restart)
menu2.add_command(label="Éteindre", command = shutdown)
menubar.add_cascade(label="Menu", menu=menu2)




#b = Button(fenetre, fg="blue", text="Scan", width=50, height=100, command= scan ).pack(side=LEFT)
#b['font'] = f
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.geometry("%dx%d" % (w, h))
fenetre.mainloop()
