from easygui import *
import tkinter as tk
from tkinter import *
import sys

title = "Image to 8-bit sprite converter!"
image = "welcome.png"

var = ccbox ( "Welcome to our image to 8-bit sprite converter by Matthew Langley"
              ", Coleman Johnston, and Kailey Sarmiento!  Instructions are very simple"
              "- select an image, then watch the magic happen!                         "
              "Are you ready?!?", image = image, title = title )

if var == 1:
    msgbox ( msg = "Please select a file to continue...", title = title )
    path = fileopenbox()
        
    
elif var == 0:
    msgbox ( msg = "Maybe next time!", title = title )
    sys.exit(0)


print (path)
