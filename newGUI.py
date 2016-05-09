from Tkinter import *
from tkFileDialog import *
from tkColorChooser import *

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
            "  This project was made by the minds of Coleman Johnston, "
            "Kailey Sarmiento, and Matthew Langley.  The intent of this program is "
            "to demonstrate some of the various libraries we have learned about in "
            "the Spring 2016 semester of CST 205.")

   delta=110
   delay=0

   for i in range(len(string) + 1):
      s = string[:i]
      update = lambda s=s: canvas.itemconfigure(text, text=s)
      canvas.after(delay, update)
      delay += delta

def getColor():
   color = askcolor()
   pick = 20
   print(color[0])

def bgImagePicker():
   name = askopenfilename(title = "Custom Background Image")
   pick = 10
   print(name)
   
def filePicker():
   name = askopenfilename(title = "Choose a file")
   root = Tk()
   root.title("Options")
   root.resizable(FALSE,FALSE)
   root.geometry("700x500")
   
   w = Text ( root, padx="30", pady="20", font = ("Helvetica", 12),
             wrap="word", bg="lightblue", width="700", height="300", spacing2="7"
              )

   w.insert(INSERT, "You chose the file...\n\n" + name + "\n\nPlease "
            "select a background color or image to continue:")
   w.pack()
   
   c = Button (root, text="Select Background Color", bg="lightblue",
               command=getColor, activebackground="#B4EEB4")
   c.place(relx=0.15, rely=.32, anchor=CENTER)

   d = Button (root, text="Select Background Image", bg="lightblue",
               command=bgImagePicker, activebackground="#B4EEB4")
   d.place(relx=.39, rely=.32, anchor=CENTER)

def controls():
   root = Tk()
   root.title("How to move")
   root.resizable(FALSE,FALSE)
   root.geometry("300x300")
   
   w = Text ( root, padx="30", pady="60", font = ("Helvetica", 12),
             wrap="word", bg="lightblue", width="300", height="300", spacing2="7"
              )
   w.insert(INSERT, "To control your character utilize the arrow keys to move around."
                     "  Press space to jump your character and click the mouse to give "
                     "him/her a good poke.  Have fun!")
   w.config(state=DISABLED)
   t = Button ( root, text="Close Window", bg="lightblue", cursor="x_cursor",
                width="300", command=lambda: close(root),
                activebackground="#B4EEB4")
   t.pack()
   w.pack()

def openInstructions():
   root = Tk()
   root.title("Instructions")
   root.resizable(FALSE,FALSE)
   root.geometry("300x300")
   
   w = Text ( root, padx="30", pady="60", font = ("Helvetica", 12),
             wrap="word", bg="lightblue", width="300", height="300", spacing2="7")
   w.insert(INSERT, "To use this program is simple.  To start, please click 'Pick-A-File'"
                     "and then select an image that you would like to process into"
                     " an 8-bit character.  From there, sit back and let the magic "
                     "happen!")
   w.config(state=DISABLED)
   t = Button ( root, text="Close Window", bg="lightblue", cursor="x_cursor",
                width="300", command=lambda: close(root),
                activebackground="#B4EEB4")
   t.pack()
   w.pack()

def main():
   root = Tk()
   root.title("8-bit sprite creator/animator")
   root.configure(background="lightblue")
   root.resizable(FALSE,FALSE)
   root.geometry("600x600")

   label = Text( root, cursor="gumby", wrap="word", width="300",
            font = ("Helvetica", 36),
             height="150", padx="50", pady="50", bg="lightblue")
   label.insert(INSERT, "Welcome to our project, please select an option to continue")
   label.config(state=DISABLED)
   
   x = Button ( root, text="How to upload a file", bg="lightblue",
                cursor="question_arrow", width="100",
                height="3", command=openInstructions,
                activebackground="#B4EEB4")

   xx = Button ( root, text="How to control your sprite",
                 bg="lightblue", cursor="man", width="100",
                height="3", command=controls,
                 activebackground="#B4EEB4")

   y = Button ( root, text = "Pick-A-File", bg="lightblue",
                cursor="rtl_logo", width="100",
                height="3", command=filePicker,
                activebackground="#B4EEB4")

   z = Button ( root, text = "Exit", bg="lightblue", cursor="X_cursor",
                width="100",
                height="3", command=lambda: close(root),
                activebackground="#B4EEB4")

   zz = Button ( root, text = "Credits", bg="lightblue", cursor="heart",
                 width="100", height="3", command=creditss,
                 activebackground="#B4EEB4")

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
