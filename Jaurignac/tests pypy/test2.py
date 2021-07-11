from tkinter import * 
from tkinter import messagebox
import tkinter.font as font 
import os 

fenetre = Tk ()
def callback():
	if messagebox.askyesno('Titre1', 'Êtes-vous sûre  vouloir faire ça ?'):
		messagebox.showwarning('Titre2', 'Tant pis...')
	else:
		messagebox.showinfo('Titre4', 'Vous avez peur !')
		messagebox.showerror('TItre4', 'Aha')
		
Button(text='Action', command=callback).pack()

fenetre.mainloop()
