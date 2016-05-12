from Tkinter import *
from tkFileDialog import *
from tkColorChooser import *
import sys, pygame, time
import make_sprite
from PIL import Image

pick = None #global variable so that everybody's can fit togeather
color = None#global variable so that everybody's code can fit

def close(root):
   root.destroy()

def creditss():
   root = Tk()
   root.title("Credits")
   root.resizable(FALSE,FALSE)
   canvas = Canvas(root, width="300", height="300",bg="lightblue")
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
   global pick
   global color
   color = askcolor()
   color = color[0]#get rgb version instead of hex 
   pick = 20

def bgImagePicker():
   global pick
   name = askopenfilename(title = "Custom Background Image")
   image = Image.open(name)
   image.save("background.jpg",'png')
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
      
      #create sprites
   make_sprite.makeSprite(name,"Standing.png","Standing2.png") 
   make_sprite.makeSprite(name,"Down.png","Down2.png")  
   make_sprite.makeSprite(name,"JumpUp.png","JumpUp2.png") 
   make_sprite.makeSprite(name,"poke.png","poke2.png")
   



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
   root.resizable(FAL+SE,FALSE)
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


###########
##CREDITS##
###########

##CST 205
##FINAL PROJECT
##TEAM: 102

##MATTHEW LANGLEY - GUI & TKINTER DIRECTOR
##COLEMAN JOHNSTON - OPEN CV DIRECTOR
##KAILEY SARMIENTO - PYGAME DIRECTOR

##########################################################################################################################################################################
##########################################################################################################################################################################

#################
##INITIAL SETUP##
#################

##Command needed to use pygame library
pygame.init()

##FPS = Frames/Sec = Determines how fast the sprite will move
FPS = 500
fpsClock = pygame.time.Clock()

##Initial window set up
size = width, height = 1000, 500
screen = pygame.display.set_mode(size)

if(color == None):
    color = 0,0,0

if(pick == None):
    pick = 20

if (pick == 10):
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background, (size))
    background = background.convert()
elif (pick == 20):
    background = color

##########################################################################################################################################################################
##########################################################################################################################################################################

####################
##ANIMATION IMAGES##
####################

##Standing
standing = pygame.image.load("Standing2.png")
w,h = standing.get_size()
wnew = int(w*.6) ##Scaling images so that the sprite will remain the same size
hnew = int(h*.6) ##Scaling images so that the sprite will remain the same size
standing = pygame.transform.scale(standing, (wnew, hnew)) ##Scaling images so that the sprite will remain the same size

##Down
down = pygame.image.load("Down2.png")
down = pygame.transform.scale(down, (wnew, hnew)) ##Scaling images so that the sprite will remain the same size

##Jump
jump = pygame.image.load("JumpUp2.png")
jump = pygame.transform.scale(jump, (wnew,hnew)) ##Scaling images so that the sprite will remain the same size

##Poke
poke = pygame.image.load("poke2.png")
poke = pygame.transform.scale(poke, (wnew,hnew)) ##Scaling images so that the sprite will remain the same size

##Sprite image that will appear first
spritemain = down

########################
##Speech bubble images##
########################

##Hey!
hey = pygame.image.load("Heybub.jpg")
wb,hb = standing.get_size()
wbnew = int(wb*1)
hbnew = int(hb*.6)
hey = pygame.transform.scale(hey, (wbnew, hbnew))

##Cut it out!
cut = pygame.image.load("cutitout.jpg")
cut = pygame.transform.scale(cut, (wbnew, hbnew))

##Seriously?!
seriously = pygame.image.load("seriously.jpg")
seriously = pygame.transform.scale(seriously, (wbnew, hbnew))

##WTF?!
wtf = pygame.image.load("wtf.jpg")
wtf = pygame.transform.scale(wtf, (wbnew, hbnew))

##Initiating silent treatment...
silence = pygame.image.load("silenttreatment.jpg")
silence = pygame.transform.scale(silence, (wbnew, hbnew))

##. . .
dots = pygame.image.load("dots.jpg")
dots = pygame.transform.scale(dots, (wbnew, hbnew))

##Easter egg
easter = pygame.image.load("easter.jpg")
easter = pygame.transform.scale(easter, (wbnew,hbnew))

##Speech bubble that will appear first
bubble = hey

##Setting starting coordinates of sprite image
plycoorx = 10
plycoory = 260

##Flags that help with animation later on
t = 0
p = 0
pk = 0

##########################################################################################################################################################################
##########################################################################################################################################################################

############################
##WHILE PROGRAM IS RUNNING##
############################

##...the following will happen
while True:
    

    ##Continusouly checking for these events as the program is running
    for event in pygame.event.get():

        ##Making the sprite image a rectangle object
        spriterect = pygame.Rect((plycoorx, plycoory),((plycoorx + wnew), (plycoory + hnew)))

        ##Checking for errors before program begins
        if event.type == pygame.QUIT: sys.exit()

        ##If the mouse is clicked on the sprite image, the poke animation will occur
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if spriterect.collidepoint(mx,my):
                spritemain = poke
                p = 100
                pk += 1

    ##############
    ##JUMP FLAGS##
    ##############
                
    ##This is used for the jumping animation
    ##This makes sure that the sprite jumps up and comes down at a reasonable rate
    if t > 0:
        t = t - 0.5
        spritemain = jump

    ##This changes the sprite animation image from the jump image to the standing image
    if spritemain == jump and t < 1:
        spritemain = standing

    ##The y coordinate of the image depends on the flag t. Therefore, the y coordinate will only change when the jump animation is triggered with the space bar    
    plycoory = (260 - ((t * t) / 2))

    ##############
    ##POKE FLAGS##
    ##############
    
    ##The p flag determines if a speech bubble will pop up or not.
    ##It also determines how long the sprite will remain the poke image
    ##It is only initiated by the poke animation with the event type MOUSEBUTTONDOWN
    if p > 0:
        p = p - 0.5
    ##The following if-else statements determines which speech bubble image will be shown.
    ##Every time the mouse is clicked, pk increases in value by one. So, different amounts of clicks will produce different speech bubbles.
    if pk == 1: bubble = hey
    elif pk == 2: bubble = cut
    elif pk == 3: bubble = seriously
    elif pk == 4: bubble = wtf
    elif pk == 5: bubble = silence
    elif pk > 5 and pk < 1000: bubble = dots
    elif pk >= 1000: bubble = easter

    ##Here is where the sprite changes from the poke image to the standing image    
    if spritemain == poke and p < 1:
        spritemain = down

    #######################
    ##MOVEMENT/ANIMATIONS##
    #######################
        
    ##When the left key is pressed, the sprite will move left
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        plycoorx -= 1   
        ##The animation frame image will change when the following conditions are met
        if plycoorx % 150 == 0: ##every x-coordinate that is divisible by 150, the following situation will occur
            if spritemain == standing: ##if the image "standing" is already shown, it'll change to the "down" image
                spritemain = down
            else: spritemain = standing ##Otherwise, the down image will switch to the standing image

    ##When the right key is pressed, the sprite will move right
    if pygame.key.get_pressed()[pygame.K_RIGHT]!= 0:
        plycoorx += 1
        if plycoorx % 150 == 0: ##every x-coordinate that is divisible by 150, the following situation will occur
            if spritemain == standing: ##if the image "standing" is already shown, it'll change to the "down" image
                spritemain = down
            else: spritemain = standing ##Otherwise, the down image will switch to the standing image

    ##Sprite jumps when space key is pressed
    if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
        ##The flag that changes the height of the sprite is changed here to allow for the jump animation to occur
        t = 15
        
    ########################
    ##UPDATINGT THE SCREEN##
    ########################

    ##Background (color or image)
    if (pick == 20):
        screen.fill(background)
    elif (pick == 10):
        screen.blit(background, (0,0))

    ##Updating the sprite image
    screen.blit(spritemain, (plycoorx, plycoory))

    ##Adds the speech bubble to the screen if the flag is used
    if p > 0:
        screen.blit(bubble, (plycoorx, plycoory - 150))

    ##Screen update based on the previous       
    pygame.display.update()

    ##The program will continue after FPS (which in this case is 500)
    fpsClock.tick(FPS)

##########################################################################################################################################################################
##########################################################################################################################################################################
