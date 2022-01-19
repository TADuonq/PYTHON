import pygame, sys 
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()
# Set up the window
DISPLAYSURE = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Game")

# Set up the color
WHITE = (255, 255, 255)
girlImg = pygame.image.load('C:/Users/Administrator/Duong/Python/Dlib/gaixinh.jpg')
girlx = 10
girly = 10
direction = 'right'

# run the game loop
while True:
    DISPLAYSURE.fill(WHITE)
    
    if direction == 'right':
        girlx += 500
        if girlx == 220:
            direction = 'down'
            
    elif direction == 'down':
        girly += 5
        if girly == 220:
            direction = 'right'
            
    elif direction == 'left':
        girlx -= 5
        if girlx == 10:
            direction = 'up'
            
    elif direction == 'up':
        girly -= 5
        if girly == 10:
            direction = 'right'
    
    DISPLAYSURE.blit(girlImg, (girlx, girly))
                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)