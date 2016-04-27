from tkinter import *
##
##def menuBars():
##   menubar = Menu(root, cursor="pirate", bg="navy")
##   instructionsmenu = Menu(menubar, tearoff=0)
##   instructionsmenu.add_command(label="How to use", command=openInstructions)
##   instructionsmenu.add_separator()
##   instructionsmenu.add_command(label="Exit", command=root.quit)
##   menubar.add_cascade(label="Instructions", menu=instructionsmenu)
##   startmenu = Menu(menubar, tearoff=0)
##   startmenu.add_command(label="Pick a file", command=donothing)
##   menubar.add_cascade(label="Start", menu=startmenu)
##   root.config(menu=menubar)

def test():
   print("hello")

def close(root):
   root.destroy()

def openInstructions():
   root = Tk()
   root.resizable(FALSE,FALSE)
   root.geometry("300x300")
   
   w = Text ( root, padx="30", pady="60",
             wrap="word", bg="lightblue", width="300", height="300")
   w.insert(INSERT, "To use this program is simple.  To start, please click 'start'"
                     "and then select an image that you would like to process into"
                     " an 8-bit character.  From there, sit back and let the magic "
                     "happen")

   t = Button ( root, text="Close Window", bg="lightblue", cursor="x_cursor", width="300",
                command=lambda: close(root))
   t.pack()
   w.pack()

def main():
   root = Tk()
   root.resizable(FALSE,FALSE)
   root.geometry("600x600")

   menubar = Menu(root, cursor="pirate", bg="navy")
   instructionsmenu = Menu(menubar, tearoff=0)
   instructionsmenu.add_command(label="How to use", command=openInstructions)
   instructionsmenu.add_separator()
   instructionsmenu.add_command(label="Exit", command=root.quit)
   menubar.add_cascade(label="Instructions", menu=instructionsmenu)
   startmenu = Menu(menubar, tearoff=0)
   startmenu.add_command(label="Pick a file", command=test)
   menubar.add_cascade(label="Start", menu=startmenu)
   root.config(menu=menubar)

   label= Text( root, cursor="heart", wrap="word", width="300",
             height="300", padx="50", pady="50", bg="lightblue")
   label.insert(INSERT, "Hello and welcome to our proect! Please select from the above menu to get started!")
   label.pack()
   root.mainloop()

main()
