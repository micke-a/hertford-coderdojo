from typing import Union, List

import pygame
from pygame.surface import SurfaceType, Surface

draw_bounding_box = True
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0, 0, 0)
white = (255, 255, 255)

display_width = 800
display_height = 600
crashed = False

class GameObject:
    def __init__(self, x_loc, y_loc, x_speed = 0, y_speed = 0):
        self.destroyed = False
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update_location(self):
        self.x_loc = self.x_loc + self.x_speed
        self.y_loc = self.y_loc + self.y_speed

    def draw(self, display: Union[Surface,SurfaceType]):
        if draw_bounding_box:
            pygame.draw.rect(display, green, self.get_bounding_box(),  2)

    def get_bounding_box(self) -> pygame.Rect:
        return pygame.Rect(-1,-1,-1,-1)

    def touches(self, box: pygame.Rect):
        return self.get_bounding_box().colliderect(box)
    



class Car(GameObject):
    def __init__(self, x_loc, y_loc, x_speed = 0, y_speed = 0):
        super().__init__(x_loc, y_loc)
        self.image = carImg = pygame.image.load('racecar.png')

    def draw(self, display: Union[Surface,SurfaceType]):
        super().draw(display)
        display.blit(self.image, (self.x_loc, self.y_loc))

    def get_bounding_box(self) -> pygame.Rect:
        return pygame.Rect(self.x_loc,self.y_loc, self.image.get_width(), self.image.get_height())


class Obstacle(GameObject):
    def __init__(self, x_loc, y_loc, x_speed = 0, y_speed = 0):
        super().__init__(x_loc, y_loc, x_speed, y_speed)
        self.width = 80
        self.height = 40

    def update_location(self):
        super().update_location()
        if self.y_loc > display_height:
            self.y_loc = 0

    def draw(self, display: Union[Surface,SurfaceType]):
        super().draw(display)
        display.fill(red, (self.x_loc, self.y_loc, self.width, self.height))

    def get_bounding_box(self) -> pygame.Rect:
        return pygame.Rect(self.x_loc,self.y_loc, self.width, self.height)


class GameMode:
    def __init__(self, display: Union[Surface,SurfaceType], clock) -> None:
        self.display = display
        self.clock = clock

    def handle_event(self):
        pass

    def update_game_objects(self):
        pass
    
    def draw_game_objects(self):
        pass
    
    def process_frame(self):
        self.handle_event()
        self.update_game_objects()
        self.draw_game_objects()
        pygame.display.update()
        self.clock.tick(60)


class RacingGameMode(GameMode):
    def __init__(self, display: Union[Surface, SurfaceType], clock) -> None:
        super().__init__(display, clock)
        self.car: Car = Car(display_width * 0.45, display_height * 0.8)

        self.obstacles: List[Obstacle] = [
            Obstacle(100, 300, 0, 1),
            Obstacle(400, 100, 0, 1),
            Obstacle(500, 400, 0, 1),
            Obstacle(600, 500, 0, 1)
        ]
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.car.x_speed = -5
                elif event.key == pygame.K_RIGHT:
                    self.car.x_speed = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.car.x_speed = 0
            ######################
    
    def update_game_objects(self):
        # Update location
        self.car.update_location()
        for obstacle in self.obstacles:
            obstacle.update_location()

        # Check obstacle collision
        for obstacle in self.obstacles:
            if obstacle.touches(self.car.get_bounding_box()):
                print(f"Car touches {obstacle}")

    def draw_game_objects(self):
        # Draw all game objects
        self.display.fill(white)
        self.car.draw(self.display)
        for obstacle in self.obstacles:
            obstacle.draw(self.display)

pygame.init()
gameDisplay: Union[Surface, SurfaceType]  = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hertford CoderDojo Racer')

clock = pygame.time.Clock()


racing_game_mode = RacingGameMode(gameDisplay, clock)

if __name__ == '__main__':
    while not crashed:
        racing_game_mode.process_frame()

    pygame.quit()
    quit()
