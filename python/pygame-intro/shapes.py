from typing import Union, List

import pygame
import random
from pygame.surface import SurfaceType, Surface

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0, 0, 0)
white = (255, 255, 255)

display_width = 800
display_height = 800
exit_game = False

pygame.init()
surface: Union[Surface, SurfaceType]  = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hertford CoderDojo - Shape')
clock = pygame.time.Clock()

if __name__ == '__main__':
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
        surface.fill(black)

        # See here for more information https://ryanstutorials.net/pygame-tutorial/pygame-shapes.php
        pygame.draw.rect(surface, green, pygame.Rect(10,10,50,100))
        pygame.draw.rect(surface=surface, color=red, rect=pygame.Rect(40,40,50,100), width=3)

        pygame.draw.circle(surface, blue, (300,300), 50)
        pygame.draw.circle(surface, red, (400,400), 50, 3)

        pygame.draw.polygon(surface=surface, color=green, points=((100, 500), (200, 400), (400, 400), (500, 500), (400, 600), (200,600)))
        pygame.draw.polygon(surface=surface, color=blue, points=((100, 500), (200, 400), (400, 400), (500, 500), (400, 600), (200,600)), width=5)
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
