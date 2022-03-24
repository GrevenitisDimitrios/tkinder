from tkinter import *

#Grid System

root = Tk()
# input boxes are Entry widgets

e = Entry(root, width=50, bg="pink", fg="black", borderwidth=5) # input boxes are Entry widgets
e.insert(0, "Enter your name") # Information inside inbox in 0 position
e.pack()

def myClick():
    hello = "Hello\t"+e.get()
    myLabel = Label(root, text= hello)
    myLabel.pack()

myButton = Button (root, text = "Enter your name", padx= 45, pady= 45, command = myClick, 
                    fg = "blue", bg = "#000000") # !- witout () !- 

#padx , pady καθοριζει την σδιασταση στον x και y αντίστοιχα
# satus = ENABLE / DISABLE
# command τι θέλουμε να κάνει το κουμπί
# Στα κουμπιά όταν καλούμε συναρτήσεις ΔΕν βάζουμε ()
# fg = foreground color
# bg = background color

myButton.pack()

root.mainloop()