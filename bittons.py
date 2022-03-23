from tkinter import *

#Grid System

root = Tk()

def myClick():
    myLabel = Label(root, text=  "You clicked me!!")
    myLabel.pack()

myButton = Button (root, text = "Click Me!!", padx= 45, pady= 45, command = myClick, 
                    fg = "blue", bg = "#000000") # !- witout () !- 

#padx , pady καθοριζει την σδιασταση στον x και y αντίστοιχα
# satus = ENABLE / DISABLE
# command τι θέλουμε να κάνει το κουμπί
# Στα κουμπιά όταν καλούμε συναρτήσεις ΔΕν βάζουμε ()
# fg = foreground color
# bg = background color

myButton.pack()

root.mainloop()