import smtplib
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

popup = Tk()
popup.title("Email")
popup.geometry("520x140")
popup.resizable(0,0)

label1=Label(popup,text="Email de l'expediteur")
label1.grid(row=0, column=0)
sender_email_entry=Entry(popup,width=25)
sender_email_entry.grid(row=0, column=1)

label2=Label(popup,text="Mot de passe")
label2.grid(row=0, column=2)
password_sender_email_entry=Entry(popup,width=25)
password_sender_email_entry.grid(row=0, column=3)

label2=Label(popup,text="Email du destinataire")
label2.grid(row=2, column=0)
receiver_email_entry=Entry(popup,width=25)
receiver_email_entry.grid(row=2, column=1)

label3=Label(popup,text="Sujet")
label3.grid(row=3, column=0)
subject_message_entry=Entry(popup,width=25)
subject_message_entry.grid(row=3, column=1)

label4=Label(popup,text="Message")
label4.grid(row=4, column=0)
message_entry=Entry(popup,width=25)
message_entry.grid(row=4, column=1)

def send():
    gmail = smtplib.SMTP('smtp.gmail.com', 587) 
    gmail.starttls() 
    gmail.login(sender_email_entry.get(), password_sender_email_entry.get())
    msg = MIMEMultipart()
    msg['From'] = sender_email_entry.get()
    msg['To'] = receiver_email_entry.get()
    msg['Subject'] = subject_message_entry.get()
    message = message_entry.get()
    msg.attach(MIMEText(message))
    gmail.send_message(msg)
    gmail.quit()
    label4=Label(popup,text="Message correctement envoyé")
    label4.grid(row=6, column=1) 

buttonGenerate=Button(popup,text="Envoyer",width=7,command=send)
buttonGenerate.grid(row=5, column=1)

popup.mainloop()