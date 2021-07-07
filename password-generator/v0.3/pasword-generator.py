from tkinter import *
from tkinter.ttk import Combobox
import random
import pyperclip

root = Tk()
root.title("Générateur de Mot de Passe")
root.geometry("320x100")
root.configure()
root.resizable(0,0)

def Assembler():
    passwd = ""
    length = int(numberEntry.get())
    
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    special = "@#$&*€^+-&o-><ø?_¿ "

    if choice.get()=="Faible":
        for i in range(0,length):
            passwd = passwd + random.choice(lowercase + uppercase)
        Lenght.set(passwd)
    elif choice.get()=="Moyen":
        for i in range(0,length):
            passwd = passwd + random.choice(lowercase + uppercase + number)
        Lenght.set(passwd)
    elif choice.get()=="Fort":
        for i in range(0,length):
            passwd = passwd + random.choice(lowercase + uppercase + number + special)
        Lenght.set(passwd)
Lenght=StringVar("")

label1 = Label(root,text="Nombre de caractères:")
label1.grid(row=0,column=0)

numberEntry=Entry(root)
numberEntry.grid(row=0,column=1)

label2 = Label(root,text="Difficulté:")
label2.grid(row=1,column=0)

choice = Combobox(root,state="readonly",width=10)
choice["values"]=("Faible","Moyen","Fort")
choice.current(0)
choice.grid(row=1,column=1)

generate = Button(root,text="Générer",width=10,command=Assembler)
generate.grid(row=2,column=0)

label3 = Label(root,text="Mot de Passe:")
label3.grid(row=3,column=0)

passwdGenerate = Entry(root,textvariable=Lenght)
passwdGenerate.grid(row=3,column=1)

def copy_password():
    pyperclip.copy(passwdGenerate.get())

copy = Button(root,text="Copier",width=5,command=copy_password)
copy.grid(row=3,column=2)

root.mainloop()