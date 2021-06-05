import psutil
from tkinter import Tk
import tkinter as tk

popup = Tk()
popup.title("Monitoring- Les Ressources Utilisées")
popup.geometry("300x80")
popup.resizable(0,0)

cpu = tk.Label(popup, text="CPU")
cpu.grid(row=0, column=0, ipadx=20, padx=5, pady=5)
cpuValue = tk.Message(popup, text=(psutil.cpu_percent(),"%"))
cpuValue.grid(row=1, column=0, ipadx=20, padx=5, pady=5)

memory = tk.Label(popup, text="Memoire")
memory.grid(row=0, column=2, ipadx=20, padx=5, pady=5)
memoryValue = tk.Message(popup, text=(psutil.virtual_memory().percent,"%"))
memoryValue.grid(row=1, column=2, ipadx=20, padx=5, pady=5)

disk = tk.Label(popup, text="Stockage")
disk.grid(row=0, column=3, ipadx=20, padx=5, pady=5)
diskValue = tk.Message(popup, text=(psutil.disk_usage('C:\\').percent,"%"))
diskValue.grid(row=1, column=3, ipadx=20, padx=5, pady=5)

popup.mainloop()
