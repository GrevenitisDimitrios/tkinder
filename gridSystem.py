from tkinter import *

#Grid System

root = Tk()
mylabel1 = Label(root, text ="Hello World").grid(row =0, column=0) # Λέμε που να στοιχήσει το label
myLabel2 = Label(root, text = " Hello Woeld 2")
mylabel3= Label(root, text ="===============")



myLabel2.grid(row =2, column = 3)# Η θέση των labels είναι σχετική και ΟΧΙ απόλυτη 
mylabel3.grid(row =1, column=3) # Λέμε που να στοιχήσει το label

root.mainloop()