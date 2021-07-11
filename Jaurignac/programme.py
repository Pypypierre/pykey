from tkinter import * 
from tkinter import messagebox
import tkinter.font as font 
import os 
import subprocess
from tkinter.messagebox import *
import time 

def callbackFunc():
    #resultString.set("{}".format(landString.get()))
     resultString.set("{}".format(s.get()))
def scan():
	r = subprocess.check_output('nfc-list')
	rt = r.decode()
	if "No NFC device found" in rt:
		showwarning('Informations', 'aucune clé')	
	else : 
		showinfo('Informations', 'clé détectée!')
def restart():
	os.system('shutdown -r now')
def shutdown():
	os.system('shutdown -h now')
def start():
	os.system('echo good')
	#os.system('mfoc -f /home/pierrot/Bureau/Jaurignac/clé.txt -O /home/pierrot/Bureau/Jaurignac/dumpbis.mfd')
	showinfo('Informations', 'clé décodée !')
	#Fs = Frame(fenetre)
	#S = Label(Fs,text = "Somme").pack()
	#S.grid(column=0, row=0, sticky="W")
	#s= StringVar()
	#entryLand = Entry(Fs, width=20, textvariable=s).pack()
	#entryLand.grid(column=1, row=0, padx=10)
	#resultButton = Button(Fs, text = 'Valider',command=callbackFunc).pack()
	#resultButton.grid(column=0, row=2, pady=10, sticky="W")
	#resultString=StringVar()
	#resultLabel = Label(Fs, textvariable=resultString).pack()
	#resultLabel.grid(column=1, row=2, padx=10, sticky="W")
	#os.system('echo good' + )	
	#Fs.pack(side=TOP)
	#time.sleep(120)
	app = Frame(fenetre)
	S = Label(app,text = "Somme")
	S.pack(side=LEFT)
	s= StringVar()
	entryLand = Entry(app, width=20, textvariable=s)
	entryLand.pack(side=LEFT)
	resultButton = Button(app, text = 'Valider',command=callbackFunc)
	resultButton.pack(side=RIGHT)
	resultString=StringVar()
	resultLabel = Label(app, textvariable=resultString)
	resultLabel.pack()
	app.pack(expand=1)
	


fenetre = Tk()
fenetre['bg']= 'white'
fenetre.wm_iconbitmap(bitmap = "@logo.xbm")
fenetre.attributes('-topmost', True)
fenetre.title('Super Jaurignac')
f = font.Font(weight="bold")
menubar = Menu(fenetre)
fenetre.config(menu=menubar)
img = PhotoImage(file='logo.png')


menu1 = Menu(menubar,tearoff=0)
menubar.add_cascade(label= "Utilitaire clé nfc", state = DISABLED, menu=menu1)


menu0 = Menu(menubar, tearoff=0)
menu0.add_command(label="scan", command = scan)
menu0.add_command(label="Commancer", command = start)
menubar.add_cascade(label="Menu", menu=menu0)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Quitter", command = fenetre.quit)
menu2.add_command(label="Redémarrer", command = restart)
menu2.add_command(label="Éteindre", command = shutdown)
menubar.add_cascade(label="Sortie", menu=menu2)


F0 = Frame(fenetre).pack(side=TOP)
b0 = Button(F0, image = img, command=start).pack(side=LEFT)


b1 = Button(fenetre, fg="blue", text="Scan", width=50, height=100, command=scan ).pack(side=RIGHT)


w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.geometry("%dx%d" % (w, h))


fenetre.mainloop()
