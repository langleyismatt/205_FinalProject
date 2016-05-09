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

##Importing necessary libraries
import sys, pygame, time

##Command needed to use pygame library
pygame.init()

##FPS = Frames/Sec = Determines how fast the sprite will move
FPS = 500
fpsClock = pygame.time.Clock()

##Initial window set up
size = width, height = 1000, 500
screen = pygame.display.set_mode(size)

##Background set up
color = 0,0,0
pick = 10
if (pick == 10):
    background = pygame.image.load("windows.jpg")
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
standing = pygame.image.load("Standing.png")
w,h = standing.get_size()
wnew = int(w*.6) ##Scaling images so that the sprite will remain the same size
hnew = int(h*.6) ##Scaling images so that the sprite will remain the same size
standing = pygame.transform.scale(standing, (wnew, hnew)) ##Scaling images so that the sprite will remain the same size

##Down
down = pygame.image.load("Down.png")
down = pygame.transform.scale(down, (wnew, hnew)) ##Scaling images so that the sprite will remain the same size

##Jump
jump = pygame.image.load("JumpUp.png")
jump = pygame.transform.scale(jump, (wnew,hnew)) ##Scaling images so that the sprite will remain the same size

##Poke
poke = pygame.image.load("poke.png")
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
