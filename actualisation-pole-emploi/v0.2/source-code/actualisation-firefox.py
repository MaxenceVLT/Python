from selenium import webdriver
import time
from tkinter import *
import tkinter as tk

#~~~~TKINTER-PROFIL-ENTRY~~~~
popup = Tk()
popup.title("Identifiant Pole Emploi")
popup.geometry("330x100")  
popup.resizable(0, 0)

username = tk.Label(popup, text="Nom d'Utilisateur")
usernametEntry = tk.Entry(popup)
username.grid(row=0, column=0, ipadx=20, padx=5, pady=5)
usernametEntry.grid(row=0, column=1, ipadx=20, padx=5, pady=5)

password = tk.Label(popup, text="Mot de Passe")
passwordEntry = tk.Entry(popup)
password.grid(row=1, column=0, ipadx=20, padx=5, pady=5)
passwordEntry.grid(row=1, column=1, ipadx=20, padx=5, pady=5)

buttonapply = tk.Button(popup, text="VALIDER", command=lambda:[popup.quit()])
buttonapply.grid(columnspan=2, padx=5, pady=5)      
popup.mainloop()
#~~~~TKINTER-PROFIL-ENTRY~~~~

browser = webdriver.Firefox(executable_path="D:\\Maxence\\Documents\\GitHub\\actualisation-pole-emploi\\selenium-firefox-driver") #Don't forget to change the path

#~~~~OPEN-PAGE~~~~
browser.get("https://www.pole-emploi.fr/accueil/")
browser.maximize_window()
browser.implicitly_wait(1000)
button = browser.find_element_by_id("footer_tc_privacy_button_2")
button.click()
#~~~~OPEN-PAGE~~~~

#~~~~FORWARD-TO-AUTHENTIFICATION-PAGE~~~~#
browser.get("https://authentification-candidat.pole-emploi.fr/connexion/XUI/?realm=%2Findividu&goto=https%3A%2F%2Fauthentification-candidat.pole-emploi.fr%3A443%2Fconnexion%2Foauth2%2Frealms%2Froot%2Frealms%2Findividu%2Fauthorize%3Frealm%3D%252Findividu%26response_type%3Did_token%2520token%26scope%3Dopenid%2520compteUsager%2520profile%2520contexteAuthentification%2520email%2520courrier%2520notifications%2520etatcivil%2520logW%2520individu%2520pilote%2520nomenclature%2520coordonnees%2520navigation%2520reclamation%2520prdvl%2520idIdentiteExterne%2520pole_emploi%2520suggestions%2520actu%2520application_USG_PN073-tdbcandidat_6408B42F17FC872440D4FF01BA6BAB16999CD903772C528808D1E6FA2B585CF2%26client_id%3DUSG_PN073-tdbcandidat_6408B42F17FC872440D4FF01BA6BAB16999CD903772C528808D1E6FA2B585CF2%26state%3Dj7b8AU3pPsqyBIDS%26nonce%3DZcYCzQvnLHtRRp2C%26redirect_uri%3Dhttps%253A%252F%252Fcandidat.pole-emploi.fr%252Fespacepersonnel%252F#login/")
time.sleep(1)
username = browser.find_element_by_id("identifiant")
username.send_keys(usernametEntry.get())
button2 = browser.find_element_by_id("submit")
button2.click()
password = browser.find_element_by_id("password")
password.send_keys(passwordEntry.get())
button3 = browser.find_element_by_id("submit")
button3.click()
#~~~~FORWARD-TO-AUTHENTIFICATION-PAGE~~~~#