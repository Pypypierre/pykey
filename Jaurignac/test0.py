from tkinter import *


def callbackFunc():
    resultString.set("{}".format(s.get()))
     
app = Tk() 
app.geometry('200x100')

S = Label(app,text = "Somme")
S.grid(column=0, row=0, sticky="W")
s= StringVar()
entryLand = Entry(app, width=20, textvariable=s)
entryLand.grid(column=1, row=0, padx=10)
resultButton = Button(app, text = 'Valider',command=callbackFunc)
resultButton.grid(column=0, row=2, pady=10, sticky="W")
resultString=StringVar()
resultLabel = Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=2, padx=10, sticky="W")

app.mainloop()


