from tkinter import * 
import tkinter as tk

popup = Tk()
popup.geometry("335x100")
popup.title("Taches à Faire")
popup.resizable(0,0) 


def newTask():
    newTask = Label(popup, text= newtask.get()) 
    newTask.grid(row=2, column=0)

    newButton = Button(popup, text = 'Fait',command=lambda:[newTask.grid_forget(), newButton.grid_forget()])
    newButton.grid(row=2, column=1)

newtask = tk.Entry(popup,width=30)
newtask.grid(row=0, columnspan=2)

newtaskButton = Button(popup, text = 'AJOUTER',command = newTask)
newtaskButton.grid(row=0, column=2, ipadx=1, ipady=1)

columntasktoDo = Label(popup, text="Taches à Faires")
columntasktoDo.grid(row=1, column=0) 

popup.mainloop()