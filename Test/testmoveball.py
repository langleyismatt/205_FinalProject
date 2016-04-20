import sys, pygame, time
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock() ##check to see what this does...

##Initial setup
size = width, height = 1000, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

##object ball creation
ball = pygame.image.load("8bitbod.jpg")
ballx = 200
bally = 130

##while the program is running... 
while True:

##Checking for errors before running program
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

##Moving the ball around the screen

    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        ballx -= 5

    if pygame.key.get_pressed()[pygame.K_RIGHT]!= 0:
        ballx += 5

    if pygame.key.get_pressed()[pygame.K_UP]!= 0:
        bally -= 5

    if pygame.key.get_pressed()[pygame.K_DOWN]!= 0:
        bally += 5

    screen.fill(black) ##backgroundcolor
    screen.blit(ball,(ballx,bally)) ##updating the screen as the ball moves
    pygame.display.update()
    fpsClock.tick(FPS)

