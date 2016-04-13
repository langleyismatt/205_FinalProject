from easygui import *
import tkinter as tk
from tkinter import *
import sys

version = "Image to 8-Bit Sprite Converter!"

var = ccbox ( "Welcome to our image to 8-bit sprite converter by Matthew Langley"
              ", Coleman Johnston, and Kailey Sarmiento!  Instructions are very simple"
              "- select an image, then watch the magic happen!                         "
              "Are you ready?!?", title = version )

if var == 1:
    msgbox ( msg = "Please select a file to continue...", title = version )
    path = fileopenbox()
        
    
elif var == 0:
    msgbox ( msg = "Maybe next time!", title = version )
    sys.exit(0)


print (path)
