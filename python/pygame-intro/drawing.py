from typing import Tuple, Union, List

import pygame
from pygame.surface import SurfaceType, Surface

# Create some variables with RGB color values
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0, 0, 0)
white = (255, 255, 255)

# Width and height of the window to display
display_width = 800
display_height = 600


pygame.init()
surface: Union[Surface, SurfaceType]  = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hertford CoderDojo - Drawing')
clock = pygame.time.Clock()

exit_game = False
drawing: bool = False
mouse_last_coord: Tuple[int, int] = None

if __name__ == '__main__':
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                # A mouse button is pressed, check if it is the left (first) one and start drawing
                pressed_buttons: Tuple[bool, bool, bool] = pygame.mouse.get_pressed(num_buttons = 3)
                print(f"Muse button down, event={event}, buttons={pressed_buttons}")
                if pressed_buttons[0]:
                    drawing = True

                # Clear the screen, paint over with black on right button down
                if pressed_buttons[2]:
                    surface.fill(black)

            if event.type == pygame.MOUSEBUTTONUP:
                # A mouse button was released, check if it was the left (first) one stop drawing
                pressed_buttons: Tuple[bool, bool, bool] = pygame.mouse.get_pressed(num_buttons = 3)
                print(f"Muse button up, event={event}, buttons={pressed_buttons}")
                if pressed_buttons[0] == False:
                    drawing = False
                    mouse_last_coord = None
            

        if drawing:
            # Find out where on the surface the mouse is
            mouse_next_coord = pygame.mouse.get_pos()    
            if mouse_last_coord and mouse_last_coord != mouse_next_coord:
                # Only draw if we have a starting point. On first click we won't have one until the mouse moves a little
                # Also don't draw a line if we haven't moved the mouse
                pygame.draw.line(surface=surface, color= green, start_pos=mouse_last_coord, end_pos=mouse_next_coord, width=3)
            mouse_last_coord = mouse_next_coord

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
