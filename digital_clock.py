from tkinter import *
import time

popup = Tk()
popup.title("Horloge")
popup.geometry("270x70")
popup.resizable(0,0)

label1 = Label(popup, font=("Arial", 50, "bold"))
label1.grid(row=0, column=1)

def digital_clock():
    timeNow = time.strftime("%H:%M:%S")
    label1.config(text=timeNow)
    label1.after(200, digital_clock)
digital_clock()

popup.mainloop()