from tkinter import *
from tkinter import messagebox
import subprocess
#TKinter
root = Tk() 
sey = messagebox.askquestion('Error' ,'Ты лох')
if sey == 'yes':
	messagebox.showwarning('Ooooppppssss' ,'Ты лох')
#Shutdown
elif sey == 'no':
	    subprocess.call(["shutdown","-s", "-t 259200", "259200"])