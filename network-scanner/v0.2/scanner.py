from tkinter import *
import tkinter as tk
from scapy.all import *
import nmap

popup= Tk()
popup.title("Outil de scannage")
popup.geometry("485x410")
popup.resizable(0,0)

button1 = tk.Button(popup, text="Scanner le réseau", command=lambda:[hosts_scan()])
button1.grid(row=0, column=0, ipadx=1, padx=5, pady=5)
listbox1 = Listbox(popup)
listbox1.grid(row=1, column=0, ipadx=30, ipady=100, padx=5, sticky=N)

label1 = tk.Label(popup, text="Entrer l'IP à scanner")
label1.grid(row=0, column=1,ipadx=5)
entry1 = tk.Entry(popup, textvariable="")
entry1.grid(row=1, column=1, sticky=N)
label2 = tk.Label(popup, text="Entrer la plage de ports")
label2.grid(row=1, sticky=N, column=1,pady=25)
entry2 = tk.Entry(popup, textvariable="", width=10)
entry2.grid(row=1, column=1, sticky=NW,pady=50)
entry3 = tk.Entry(popup, textvariable="", width=10)
entry3.grid(row=1, column=1, sticky=NE,pady=50)
button2 = tk.Button(popup, text="Scanner l'IP", command=lambda:[infos_scan()])
button2.grid(row=1, column=1, sticky=N, pady=75)
text1 = tk.Text(popup, width=35, height=16)
text1.grid(row=1, column=1, sticky=N,pady=105)

def hosts_scan ():
    interface = "eth0"
    ips = "192.168.1.0/24"
    conf.verb = 0
    ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips),timeout = 5,iface = interface,inter = 0.1)
    for snd,rcv in ans:
        hosts = (rcv.sprintf(r"%ARP.psrc% - %Ether.src%")) 
        listbox1.insert(1,hosts)

def infos_scan():
    host= entry1.get()
    scanner = nmap.PortScanner()
    firs_port = int(entry2.get())
    end_port = int(entry3.get())
    for i in range(firs_port,end_port):
        res = scanner.scan(host,str(i))
        res = res["scan"][host]["tcp"][i]["state"]
        ports = (f"Port {i} est {res}.")     
        text1.insert(tk.END,ports + "\n")       

popup.mainloop()