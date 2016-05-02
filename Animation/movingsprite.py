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
###Poke
poke = pygame.image.load("poke.jpg")
poke = pygame.transform.scale(poke, (wnew,hnew))


##Speech bubbles
###Hey!
hey = pygame.image.load("Heybub.jpg")
wb,hb = standing.get_size()
wbnew = int(wb*1)
hbnew = int(hb*.6)
hey = pygame.transform.scale(hey, (wbnew, hbnew))
cut = pygame.image.load("cutitout.jpg")
cut = pygame.transform.scale(cut, (wbnew, hbnew))
seriously = pygame.image.load("seriously.jpg")
seriously = pygame.transform.scale(seriously, (wbnew, hbnew))
wtf = pygame.image.load("wtf.jpg")
wtf = pygame.transform.scale(wtf, (wbnew, hbnew))
silence = pygame.image.load("silenttreatment.jpg")
silence = pygame.transform.scale(silence, (wbnew, hbnew))
dots = pygame.image.load("dots.jpg")
dots = pygame.transform.scale(dots, (wbnew, hbnew))
easter = pygame.image.load("easter.jpg")
easter = pygame.transform.scale(easter, (wbnew,hbnew))

bubble = hey


##Setting starting coordinates of sprite
plycoorx = 10
plycoory = 260

t = 0
p = 0
pk = 0

##While the program is running... the following will happen
while True:

    ##Checking for errors before program begins
    for event in pygame.event.get():
        spriterect = pygame.Rect((plycoorx, plycoory),((plycoorx + wnew), (plycoory + hnew)))
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if spriterect.collidepoint(mx,my):
                spritemain = poke
                p = 100
                pk += 1
            
    if t > 0:
        t = t - 0.5
        spritemain = jump

    if spritemain == jump and t < 1:
        spritemain = standing
        
    plycoory = (260 - ((t * t) / 2))

    if p > 0:
        p = p - 0.5

    if pk == 1: bubble = hey
    elif pk == 2: bubble = cut
    elif pk == 3: bubble = seriously
    elif pk == 4: bubble = wtf
    elif pk == 5: bubble = silence
    elif pk > 5 and pk < 1000: bubble = dots
    elif pk >= 1000: bubble = easter
        
    if spritemain == poke and p < 1:
        spritemain = down

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

            
    screen.fill(black) ##background color
    screen.blit(spritemain, (plycoorx, plycoory)) ##updating the screen images according to previous commands
    if p > 0:
        screen.blit(bubble, (plycoorx, plycoory - 150))
            
    pygame.display.update() ##updating screen display according to previous commands
    fpsClock.tick(FPS)
