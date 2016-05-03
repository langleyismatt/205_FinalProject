from tkinter import *
from tkinter.filedialog import askopenfilename

def close(root):
   root.destroy()

def creditss():
   root = Tk()
   root.title("Credits")
   root.resizable(FALSE,FALSE)
   canvas = Canvas(root, width="300", height="300",
              bg="lightblue")
   canvas.pack()

   text = canvas.create_text(300,100, text='', font = ("Helvetica", 32))

   string=("Thank you for giving our project a try!"
            "  This project was made by the brilliant minds of Coleman Johnson, "
            "Kailey Sarmiento, and Matthew Langley.  The intent of this program is "
            "to demonstrate some of the various libraries we have learned about in "
            "to Spring 2016 semester of CST 205.")

   delta=150
   delay=0

   for i in range(len(string) + 1):
      s = string[:i]
      update = lambda s=s: canvas.itemconfigure(text, text=s)
      canvas.after(delay, update)
      delay += delta

def filePicker():
   name = askopenfilename(title = "Choose a file")
   return name

def controls():
   root = Tk()
   root.title("How to move")
   root.resizable(FALSE,FALSE)
   root.geometry("300x300")
   
   w = Text ( root, padx="30", pady="60", font = ("Helvetica", 12),
             wrap="word", bg="lightblue", width="300", height="300")
   w.insert(INSERT, "To control your character utilize the arrow keys to move around."
                     "  Press space to jump your character and click the mouse to give "
                     "him/her a good poke.  Have fun!")
   w.config(state=DISABLED)
   t = Button ( root, text="Close Window", bg="lightblue", cursor="x_cursor", width="300",
                command=lambda: close(root), activebackground="#B4EEB4")
   t.pack()
   w.pack()

def openInstructions():
   root = Tk()
   root.title("Instructions")
   root.resizable(FALSE,FALSE)
   root.geometry("300x300")
   
   w = Text ( root, padx="30", pady="60", font = ("Helvetica", 12),
             wrap="word", bg="lightblue", width="300", height="300")
   w.insert(INSERT, "To use this program is simple.  To start, please click 'Pick-A-File'"
                     "and then select an image that you would like to process into"
                     " an 8-bit character.  From there, sit back and let the magic "
                     "happen!")
   w.config(state=DISABLED)
   t = Button ( root, text="Close Window", bg="lightblue", cursor="x_cursor", width="300",
                command=lambda: close(root), activebackground="#B4EEB4")
   t.pack()
   w.pack()

def main():
   root = Tk()
   root.title("8-bit sprite creator/animator")
   root.configure(background="lightblue")
   root.resizable(FALSE,FALSE)
   root.geometry("600x600")

##   menubar = Menu(root, cursor="heart", bg="lightblue", fg="lightblue", activeforeground="lightblue", activebackground="blue")
##   instructionsmenu = Menu(menubar, tearoff=0)
##   instructionsmenu.add_command(label="How to use", command=openInstructions)
##   instructionsmenu.add_separator()
##   instructionsmenu.add_command(label="Exit", command=lambda: close(root))
##   menubar.add_cascade(label="Instructions", menu=instructionsmenu)
##   startmenu = Menu(menubar, tearoff=0)
##   startmenu.add_command(label="Pick a file", command=filePicker)
##   menubar.add_cascade(label="Start", menu=startmenu)
##   root.config(menu=menubar)

   label = Text( root, cursor="gumby", wrap="word", width="300", font = ("Helvetica", 36),
             height="150", padx="50", pady="50", bg="lightblue", justify="CENTER")
   label.insert(INSERT, "Welcome to our project, please select an option to continue")
   label.config(state=DISABLED)
   
   x = Button ( root, text="How to upload a file", bg="lightblue", cursor="question_arrow", width="100",
                height="3", command=openInstructions, activebackground="#B4EEB4")

   xx = Button ( root, text="How to control your sprite", bg="lightblue", cursor="man", width="100",
                height="3", command=controls, activebackground="#B4EEB4")

   y = Button ( root, text = "Pick-A-File", bg="lightblue", cursor="rtl_logo", width="100",
                height="3", command=filePicker, activebackground="#B4EEB4")

   z = Button ( root, text = "Exit", bg="lightblue", cursor="X_cursor", width="100",
                height="3", command=lambda: close(root), activebackground="#B4EEB4")

   zz = Button ( root, text = "Credits", bg="lightblue", cursor="heart", width="100",
                height="3", command=creditss, activebackground="#B4EEB4")

   frame = Frame(width=600, height=10, bg="lightblue", colormap="new")
   frame1 = Frame(width=600, height=10, bg="lightblue", colormap="new")
   frame2 = Frame(width=600, height=10, bg="lightblue", colormap="new")
   frame3 = Frame(width=600, height=10, bg="lightblue", colormap="new")
   frame4 = Frame(width=600, height=10, bg="lightblue", colormap="new")
   
   frame.pack()
   x.pack()
   frame1.pack()
   xx.pack()
   frame3.pack()
   y.pack()
   frame2.pack()
   zz.pack()
   frame4.pack()
   z.pack()
   label.pack()
   root.mainloop()

main()
