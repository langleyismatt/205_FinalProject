import sys, pygame, time
pygame.init()

FPS = 500
fpsClock = pygame.time.Clock()

##Initial window set up
size = width, height = 1000, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

##Animation frames = images
###Standing
standing = pygame.image.load("Standing.jpg")
w,h = standing.get_size()
wnew = int(w*.6)
hnew = int(h*.6)
standing = pygame.transform.scale(standing, (wnew, hnew))
###Down
down = pygame.image.load("Down.jpg")
down = pygame.transform.scale(down, (wnew, hnew))
spritemain = down
###Jump
jump = pygame.image.load("JumpUp.jpg")
jump = pygame.transform.scale(jump, (wnew,hnew))

##Setting starting coordinates of sprite
plycoorx = 10
plycoory = 260

t = 0

##While the program is running... the following will happen
while True:

    ##Checking for errors before program begins
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if t > 0:
        t = t - 0.5
        spritemain = jump

    if spritemain == jump and t < 1:
        spritemain = standing
        
    plycoory = (260 - ((t * t) / 2))

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
        if plycoorx % 150 == 0: ##see above explanation
            if spritemain == standing:
                spritemain = down
            else: spritemain = standing

    ##Sprite jumps when space key is pressed
    if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
        t = 15

##GETTING "POKE" TO WORK AAGGGHHH
##    if pygame.mouse.get_pressed()[0]:
##        x, y = pygame.mouse.get_pos()
##        pygame.surface.get_rect()
            
    screen.fill(black) ##background color
    screen.blit(spritemain, (plycoorx, plycoory)) ##updating the screen images according to previous commands
    pygame.display.update() ##updating screen display according to previous commands
    fpsClock.tick(FPS)
