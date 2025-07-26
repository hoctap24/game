import pygame, sys
from pygame.locals import *

pygame.init()
#Màn hình
DISPLAY = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Free Fire")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()