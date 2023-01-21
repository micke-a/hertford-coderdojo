import math
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

    square_x = 400
    square_y = 400
    speed = 200
    speed_x = 0
    speed_y = 0
    mouse_pos = None
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
        surface.fill(black)
        
        if pygame.mouse.get_focused():
            mouse_pos = pygame.mouse.get_pos() 
            # https://www.mathsisfun.com/algebra/trig-finding-angle-right-triangle.html
            # Tangent: tan(θ) = opposite / adjacent
            # angle = arctan(tan_value)
            opposite = mouse_pos[0] - square_x
            adjacent = mouse_pos[1] - square_y
            if opposite != 0 and adjacent != 0:
                angle =  math.atan(opposite/adjacent)

            s_x = math.sin(angle) * speed
            s_y = math.cos(angle) * speed
            print (f"square={(square_x, square_y)}, mouse={mouse_pos}, opp={opposite}, adj={adjacent}, speed={(s_x, s_y)}, angle={angle*(180/math.pi)}")

            pygame.draw.line(surface=surface, color=blue, start_pos=(square_x, square_y), end_pos=(square_x+s_x, square_y+s_y), width=4)

        pygame.draw.rect(surface, green, pygame.Rect(square_x + speed_x,square_y+speed_y,25,25))
        if mouse_pos:
            pygame.draw.line(surface=surface, color=blue, start_pos=(square_x, square_y), end_pos=mouse_pos)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
