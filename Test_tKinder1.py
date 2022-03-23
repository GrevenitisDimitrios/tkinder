from tkinter import* 

'''In tKinter EVERYTHING is a widget'''

root = Tk()

'''The main widget is "root" widget - The main Window
 In tKinter to create a thing is a 2 step process 
 1) define it 
 2) put it on screen
Create a Label Widget'''

myLabel = Label(root, text="Hello World")

'''Then we "pack" it. It packs it in a screen that barerly fits it. If we want fixed size we can fix it
Put label into the screen '''
myLabel.pack()
# We create an Event Loop
root.mainloop()