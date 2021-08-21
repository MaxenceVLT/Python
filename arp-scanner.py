import sys
from scapy.all import *

interface = input("Entrer l'interface réseau: ")
ips = input("Entrer le réseau (Réseau/Bits): ")
print("\n [*] Scan en cours [*]")

conf.verb = 0
ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips),timeout = 5,iface = interface,inter = 0.1)
for snd,rcv in ans:
        print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))

print("\n [*] Scan terminé [*]")