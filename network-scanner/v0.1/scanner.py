from time import sleep
from tkinter import *
import tkinter as tk
from scapy.all import *
import nmap

popup= Tk()
popup.title("Network Tools")
popup.geometry("200x365")
popup.resizable(0,0)

button1 = tk.Button(popup, text="Scanner le réseau", command=lambda:[hosts_scan()])
button1.grid(row=0, column=0, ipadx=1, padx=5, pady=5)
listbox1 = Listbox(popup)
listbox1.grid(row=1, column=0, ipadx=30, ipady=78, padx=5, sticky=N)


def hosts_scan ():
    interface = "Ethernet"
    ips = "192.168.1.0/24"
    conf.verb = 0
    ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips),timeout = 5,iface = interface,inter = 0.1)
    for snd,rcv in ans:
        hosts = (rcv.sprintf(r"%ARP.psrc% - %Ether.src%")) 
        listbox1.insert(1,hosts)

popup.mainloop()

