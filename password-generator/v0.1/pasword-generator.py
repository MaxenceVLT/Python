from tkinter import *
from tkinter.ttk import Combobox
import random

popup = Tk()
popup.title("Générateur de Mot de Passe")
popup.geometry("335x55")
popup.resizable(0,0)

def generate():
    passwd=""
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number ="0123456789"
    special = "@#$&*€^+-&o-><ø?_¿ "

    caracterAssembler = lowercase + uppercase + number + special
    for i in range(0,20):
        passwd = passwd+random.choice(caracterAssembler)
    Lenght.set(passwd)
Lenght=StringVar("")

buttonGenerate=Button(popup,text="Générer",width=10,command=generate)
buttonGenerate.grid(row=1, column=1)

label1=Label(popup,text="Le Mot de Passe:")
label1.grid(row=0, column=0)

password=Entry(popup,textvariable=Lenght,width=26)
password.grid(row=0, column=1)

popup.mainloop()