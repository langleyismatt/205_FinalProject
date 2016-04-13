import sys, pygame, time
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

size = width, height = 1000, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)
##DISPLAYSURF = pygame.display.set_mode((width,height,0,32)

ball = pygame.image.load("ball.gif")
ballx = 200
bally = 130
##ballrect = ball.get_rect()

while True:

    ##DISPLAYSURF.blit(ball,(ballx,bally))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ##key_pressed = pygame.key.get_pressed()

    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        ballx -= 5

    if pygame.key.get_pressed()[pygame.K_RIGHT]!= 0:
        ballx += 5

    if pygame.key.get_pressed()[pygame.K_UP]!= 0:
        bally -= 5

    if pygame.key.get_pressed()[pygame.K_DOWN]!= 0:
        bally += 5
        

    ##ballrect = ballrect.move(speed)
    ##if ballrect.left < 0 or ballrect.right > width:
    ##    speed[0] = -speed[0]
    ##if ballrect.top < 0 or ballrect.bottom > height:
    ##    speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball,(ballx,bally)) ##removed , ballrect
    pygame.display.update()
    fpsClock.tick(FPS)

