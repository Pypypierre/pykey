from tkinter import *
 
  
 

  
fen = Tk()

fen.iconbitmap("/home/pierrot/Bureau/Jaurignac/logo.ico")
img = PhotoImage(file='logo.ppm')
l = Label(fen, image=img)
l.pack()



button = Button(fen, image=img, bg='#dee5dc', bd=0, relief=SUNKEN)
button.pack()

fen.mainloop ()
