import sys, pygame, time
pygame.init()

size = width, height = 1000, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

standing = pygame.image.load("Standing.jpg")
w,h = standing.get_size()
wnew = int(w*.6)
hnew = int(h*.6)
standing = pygame.transform.scale(standing, (wnew, hnew))
down = pygame.image.load("Down.jpg")
down = pygame.transform.scale(down, (wnew, hnew))
spritemain = down

plycoorx = 10
plycoory = 260

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        plycoorx -= 1
        if plycoorx % 200 == 0:
            if spritemain == standing:
                spritemain = down
            else: spritemain = standing

    if pygame.key.get_pressed()[pygame.K_RIGHT]!= 0:
        plycoorx += 1
        if plycoorx % 200 == 0:
            if spritemain == standing:
                spritemain = down
            else: spritemain = standing

    if pygame.key.get_pressed()[pygame.K_UP]!= 0:
        plycoory -= 1
        if plycoorx % 200 == 0:
            if spritemain == standing:
                spritemain = down
            else: spritemain = standing

    if pygame.key.get_pressed()[pygame.K_DOWN]!= 0:
        plycoory += 1
        if plycoorx % 200 == 0:
            if spritemain == standing:
                spritemain = down
            else: spritemain = standing
        
    ##if plycoorx % 5 == 0:
    ##    if spritemain == standing:
    ##        spritemain = down
    ##    else: spritemain = standing

    screen.fill(black)
    screen.blit(spritemain, (plycoorx, plycoory))
    pygame.display.update()
        
