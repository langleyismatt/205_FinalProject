from tkinter import *
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = Tk()
menubar = Menu(root)
instructionsmenu = Menu(menubar, tearoff=0)
instructionsmenu.add_command(label="How to use", command=donothing)

instructionsmenu.add_separator()

instructionsmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Instructions", menu=instructionsmenu)

startmenu = Menu(menubar, tearoff=0)

startmenu.add_command(label="Pick a file", command=donothing)

menubar.add_cascade(label="Start", menu=startmenu)

var= StringVar()
label= Message( root, textvariable=var )
var.set("Hello and welcome to our proect!dfgggggggggggggggggggggggggg")
label.pack()
root.config(menu=menubar)
root.mainloop()
