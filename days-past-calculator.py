from tkinter import *


from datetime import date
import datetime

old_day = int(input("Entrer le jour: "))
old_month = int(input("Entrer le mois: "))
old_year = int(input("Entrer l'année: "))

now_time = datetime.datetime.now()
now_day = int(now_time.strftime("%d"))
now_month = int(now_time.strftime("%m"))
now_year = int(now_time.strftime("%Y"))

date1=  date(old_year,old_month,old_day)
date2 = date(now_year,now_month,now_day)

print("Date entrée",date1)
print("Date actuelle",date2)

calcul = date2 - date1

print("Nombre de Jours passés: ",calcul.days)