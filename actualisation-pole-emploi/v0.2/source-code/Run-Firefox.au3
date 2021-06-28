#include <Date.au3>
$alert = MsgBox(4,"Nous sommes le "& _NowDate() ,"Voulez-vous le lancer Script ?")

if $alert = 6 then
MsgBox(0,"Validation","Le Script va se lancer",3)
Run("python D:\Maxence\Documents\GitHub\actualisation-pole-emploi\source-code\actualisation-firefox.py")
EndIf
if $alert = 7 then
MsgBox(0,"Annulation","Le Script ne va pas se lancer",3)
EndIf