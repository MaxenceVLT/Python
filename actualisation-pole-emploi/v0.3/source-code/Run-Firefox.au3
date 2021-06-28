#include <Date.au3>
$alert = MsgBox(4,"Alert - Pole Emploi ","Nous sommes le "& _NowDate()& ", voulez-vous le lancer Script ?")

if $alert = 6 then
MsgBox(0,"Validation","Le Script va se lancer",3)
Run("python D:\Maxence\Documents\GitHub\Actualisation-Pole-Emploi\source-code\actualisation-firefox.py")
EndIf
if $alert = 7 then
MsgBox(0,"Annulation","Le Script ne va pas se lancer",3)
EndIf