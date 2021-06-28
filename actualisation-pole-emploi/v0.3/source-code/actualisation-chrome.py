import time
import tkinter as tk
from tkinter import *
from pickle import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

#~~~~↓[TKINTER]↓~~~~
popup = Tk()
popup.title("Identifiant- Pole Emploi")
popup.geometry("400x180")   
popup.resizable(0, 0)  
#~~~~{SEE-PICKLE-MODULE-DOCUMENTATION}~~~~#
RestoreFile = open("D:\\Maxence\\Documents\\GitHub\\Actualisation-Pole-Emploi\\source-code\\AccountInfos","rb")
UserName = load(RestoreFile)
PassWord = load(RestoreFile)
#~~~~{END-OF-THE-PROCESS}~~~~#
username = tk.Label(popup, text="Nom d'Utilisateur")
usernametEntry = tk.Entry(popup)
usernametEntry.insert(tk.END,UserName)
username.grid(row=0, column=0, ipadx=20, padx=5, pady=5)
usernametEntry.grid(row=0, column=1, ipadx=20, padx=5, pady=5)
password = tk.Label(popup, text="Mot de Passe")
passwordEntry = tk.Entry(popup)
passwordEntry.insert(tk.END,PassWord)
password.grid(row=1, column=0, ipadx=20, padx=5, pady=5)
passwordEntry.grid(row=1, column=1, ipadx=20, padx=5, pady=5)
buttonapply = tk.Button(popup, text="VALIDER", command=lambda:[popup.quit()])
#~~~~{SEE-PICKLE-MODULE-DOCUMENTATION}~~~~#
def SaveInfos():
    UserName = usernametEntry.get()
    PassWord = passwordEntry.get()
    savefile = open("D:\\Maxence\\Documents\\GitHub\\Actualisation-Pole-Emploi\\source-code\\AccountInfos","rb")
    dump(UserName,savefile)
    dump(PassWord,savefile)
#~~~~{END-OF-THE-PROCESS}~~~~#
Save = Checkbutton(popup, text="Sauvegarder", height=2, width=0, command=SaveInfos)
Save.grid(columnspan=2, row=2)
indication = tk.Label(popup, text="⚠️Cocher que si les indentifiants ont été changés⚠️")
indication.grid(row=3, columnspan=2, sticky='ns' )
buttonapply = tk.Button(popup, text="VALIDER", command= lambda:[popup.quit()])
buttonapply.grid(columnspan=2, padx=5, pady=5)      
popup.mainloop()
#~~~~↑[TKINTER]↑~~~~#

browser = webdriver.Chrome(executable_path="D:\\Maxence\\Documents\\GitHub\\Actualisation-Pole-Emploi\\module\\selenium-chrome-driver")

#~~~~↓[OPEN-PAGE]↓~~~~
browser.get("https://www.pole-emploi.fr/accueil/")
browser.maximize_window()
browser.implicitly_wait(1000)
button = browser.find_element_by_id("footer_tc_privacy_button_2")
button.click()
#~~~~↑[OPEN-PAGE]↑~~~~

#~~~~↓[FORWARD-TO-AUTHENTIFICATION-PAGE]↓~~~~#
browser.get("https://authentification-candidat.pole-emploi.fr/connexion/XUI/?realm=%2Findividu&goto=https%3A%2F%2Fauthentification-candidat.pole-emploi.fr%3A443%2Fconnexion%2Foauth2%2Frealms%2Froot%2Frealms%2Findividu%2Fauthorize%3Frealm%3D%252Findividu%26response_type%3Did_token%2520token%26scope%3Dopenid%2520compteUsager%2520profile%2520contexteAuthentification%2520email%2520courrier%2520notifications%2520etatcivil%2520logW%2520individu%2520pilote%2520nomenclature%2520coordonnees%2520navigation%2520reclamation%2520prdvl%2520idIdentiteExterne%2520pole_emploi%2520suggestions%2520actu%2520application_USG_PN073-tdbcandidat_6408B42F17FC872440D4FF01BA6BAB16999CD903772C528808D1E6FA2B585CF2%26client_id%3DUSG_PN073-tdbcandidat_6408B42F17FC872440D4FF01BA6BAB16999CD903772C528808D1E6FA2B585CF2%26state%3Dj7b8AU3pPsqyBIDS%26nonce%3DZcYCzQvnLHtRRp2C%26redirect_uri%3Dhttps%253A%252F%252Fcandidat.pole-emploi.fr%252Fespacepersonnel%252F#login/")
time.sleep(5)
username = browser.find_element_by_id("identifiant")
username.send_keys(usernametEntry.get())
button2 = browser.find_element_by_id("submit")
button2.click()
time.sleep(2)
password = browser.find_element_by_id("password")
password.send_keys(passwordEntry.get())
button3 = browser.find_element_by_id("submit")
button3.click()
#~~~~↑[FORWARD-TO-AUTHENTIFICATION-PAGE]↑~~~~#
time.sleep(3)
#~~~~↓[ACTUTALISATION-PAGE]↓~~~~#
browser.get("https://authentification-candidat.pole-emploi.fr/compte/redirigervers?url=https://actualisation-authent.pole-emploi.fr/acces.htm&actu=true&actuCalculee=true")
time.sleep(3)
browser.get("https://actualisation-authent.pole-emploi.fr/WebUnidialog/AC/declareSituPage01.htm?flashLu=oui")
time.sleep(3)
button4 = browser.find_element_by_id("formationNon")
button4.click()
actions = ActionChains(browser) 
actions.send_keys(Keys.ENTER)
actions.perform()
button5 = browser.find_element_by_id("blocTravail-close")
button5.click()
button6 = browser.find_element_by_id("blocStage-close")
button6.click()
button7 = browser.find_element_by_id("blocMaladie-close")
button7.click()
button8 = browser.find_element_by_id("blocRetraite-close")
button8.click()
button9 = browser.find_element_by_id("blocInvalidite-close")
button9.click()
button10 = browser.find_element_by_id("blocRecherche-close")
button10.click()
time.sleep(2) 
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(3)
actions.send_keys(Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB)
actions.perform()
time.sleep(1)
actions.send_keys(Keys.ENTER)
actions.perform()
#~~~~↑[ACTUTALISATION-PAGE]↑~~~~#