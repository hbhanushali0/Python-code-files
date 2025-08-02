

import pygame
from pygame import *



pygame.init()


width = 1200

height = 600

border = 20

screen = pygame.display.set_mode((width,height))


pygame.draw.rect(screen, pygame.color("white"), pygame.rect((0,0),(width)))

pygame.draw.rect(screen, pygame.color("white"), pygame.rect((0,0),(height))

pygame.draw.rect(screen, pygame.color("white"), pygame.rect(0,height-border,width-border))

pygame.display.flip()

while True:
	e = pygame.event.poll()
	if e.type == pygame.quit:
		break
pygame.quit()




