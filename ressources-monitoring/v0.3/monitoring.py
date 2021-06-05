import psutil
from tkinter import Tk
import tkinter as tk
from tkinter import ttk

popup = Tk()
popup.title("Les Ressources Utilisées")
popup.geometry("300x105")
popup.resizable(0,0)

normal = 40
warning = 75
critical = 100

cpuUsage = psutil.cpu_percent()
cpu = tk.Label(popup, text="CPU")
cpu.grid(row=0, column=0, ipadx=20, padx=5, pady=5)
if cpuUsage <= normal:
    cpuValue = tk.Message(popup,bg= "green2", text=(cpuUsage,"%"))
elif cpuUsage <= warning:
    cpuValue = tk.Message(popup,bg= "gold", text=(cpuUsage,"%"))
elif cpuUsage <= critical:
    cpuValue = tk.Message(popup,bg= "red", text=(cpuUsage,"%"))
cpuValue.grid(row=1, column=0, ipadx=20, padx=5, pady=5)


memoryUsage = psutil.virtual_memory().percent
memory = tk.Label(popup, text="Memoire")
memory.grid(row=0, column=2, ipadx=20, padx=5, pady=5)
if memoryUsage <= normal:
    memoryValue = tk.Message(popup,bg= "green2", text=(memoryUsage,"%"))
elif memoryUsage <= warning:
    memoryValue = tk.Message(popup,bg= "gold", text=(memoryUsage,"%"))
elif memoryUsage <= critical:
    memoryValue = tk.Message(popup,bg= "red", text=(memoryUsage,"%"))
memoryValue.grid(row=1, column=2, ipadx=20, padx=5, pady=5)


def action(refreshSelection):
    diskUsage = psutil.disk_usage(listDisk.get()).percent
    if diskUsage <= normal:
        diskValue = tk.Message(popup,bg= "green2", text=(diskUsage,"%"))
    elif diskUsage <= warning:
        diskValue = tk.Message(popup,bg= "gold", text=(diskUsage,"%"))
    elif diskUsage <= critical:
        diskValue = tk.Message(popup,bg= "red", text=(diskUsage,"%"))
    diskValue.grid(row=1, column=3, ipadx=20, padx=5, pady=5)

diskName = ["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]
listDisk = ttk.Combobox(values=diskName,width=4)
listDisk.current(2)
listDisk.bind("<<ComboboxSelected>>", action)
listDisk.grid(column=3, row=2, ipadx=1)

disk = tk.Label(popup, text="Stockage")
disk.grid(row=0, column=3, ipadx=20, padx=5, pady=5)

diskUsage = psutil.disk_usage(listDisk.get()).percent
disk = tk.Label(popup, text="Stockage")
disk.grid(row=0, column=3, ipadx=20, padx=5, pady=5)
if diskUsage <= normal:
    diskValue = tk.Message(popup,bg= "green2", text=(diskUsage,"%"))
elif diskUsage <= warning:
    diskValue = tk.Message(popup,bg= "gold", text=(diskUsage,"%"))
elif diskUsage <= critical:
    diskValue = tk.Message(popup,bg= "red", text=(diskUsage,"%"))
diskValue.grid(row=1, column=3, ipadx=20, padx=5, pady=5)


popup.mainloop()
