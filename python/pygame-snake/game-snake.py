from typing import Union, List

import pygame
import random
from pygame.surface import SurfaceType, Surface

draw_bounding_box = True
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0, 0, 0)
white = (255, 255, 255)

grid_size_px = 20
grid_size_x = 30
gird_size_y = 30

display_width = grid_size_x * grid_size_px
display_height = gird_size_y * grid_size_px
exit_game = False

game_mode_started = 'STARTED'
game_mode_play = 'PLAY'
game_mode_gameover = 'GAME_OVER'
game_mode_current = game_mode_started


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
    


class Snake(GameObject):
    def __init__(self, x_loc, y_loc, x_speed = 0, y_speed = 0):
        super().__init__(x_loc, y_loc)
        self.body = list()
        self.body.append((self.x_loc, self.y_loc))
        for i in range(1,5):
            self.body.append((self.x_loc - i, self.y_loc))


    def draw(self, display: Union[Surface,SurfaceType]):
        super().draw(display)
        head = self.body[0]
        pygame.draw.rect(display, green, pygame.Rect(head[0]*grid_size_px, head[1]*grid_size_px, grid_size_px, grid_size_px))
        for body_part in self.body[1:-1]:
            pygame.draw.rect(display, blue, pygame.Rect(body_part[0]*grid_size_px, body_part[1]*grid_size_px, grid_size_px, grid_size_px))


    def get_bounding_box(self) -> pygame.Rect:
        return pygame.Rect(self.x_loc*grid_size_px,self.y_loc*grid_size_px, grid_size_px, grid_size_px)

    def update_location(self):
        super().update_location()
        del(self.body[-1])
        self.body.insert(0, (self.x_loc, self.y_loc))

    def grow(self):
        self.body.append(self.body[-1])
        print(len(self.body))
    
    def eats_itself(self):
        head = self.body[0]
        if head in self.body[1:-1]:
            print("Snake ate itself : (")
            global game_mode_current
            game_mode_current = game_mode_gameover

    def is_moving(self):
        if self.x_speed == 0 and self.y_speed == 0:
            return False
        else:
            return True

class Food(GameObject):
    def __init__(self):
        super().__init__(0, 0)
        self.width = grid_size_px
        self.height = grid_size_px
        self.move_random()

    def draw(self, display: Union[Surface,SurfaceType]):
        super().draw(display)
        display.fill(green, (self.x_loc*grid_size_px, self.y_loc*grid_size_px, self.width, self.height))

    def get_bounding_box(self) -> pygame.Rect:
        return pygame.Rect(self.x_loc*grid_size_px,self.y_loc*grid_size_px, self.width, self.height)

    def move_random(self):
        self.x_loc = random.randint(0, grid_size_x-1)
        self.y_loc = random.randint(0, gird_size_y-1)


class GameMode:
    def __init__(self, display: Union[Surface,SurfaceType], clock) -> None:
        self.surface = display
        self.clock = clock

    def handle_event(self, event):
        pass

    def update_game_objects(self):
        pass
    
    def draw_game_objects(self):
        pass
    
    def process_frame(self):
        self.update_game_objects()
        self.draw_game_objects()
        pygame.display.update()
        self.clock.tick(10)


class StartedGameMode(GameMode):
    def __init__(self, display: Union[Surface, SurfaceType], clock) -> None:
        super().__init__(display, clock)

    def handle_event(self, event):
        global game_mode_current
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_mode_current = game_mode_play

    
    def draw_game_objects(self):
        font = pygame.font.SysFont(None, 24)
        message = 'Snake - Hertford CoderDojo'
        img = font.render(message, True, blue)
        self.surface.blit(img, (display_height/2, display_width/2 -(len(message)*font.get_linesize()/2)))


class GameOverGameMode(GameMode):
    def __init__(self, display: Union[Surface, SurfaceType], clock) -> None:
        super().__init__(display, clock)

    def handle_event(self, event):
        global game_mode_current
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_mode_current = game_mode_started

    
    def draw_game_objects(self):
        font = pygame.font.SysFont(None, 24)
        message = "GAME OVER"
        
        img = font.render(message, True, red)
        self.surface.blit(img, (display_height/2, display_width/2 -(len(message)*font.get_linesize()/2)))

class TheGameMode(GameMode):
    def __init__(self, display: Union[Surface, SurfaceType], clock) -> None:
        super().__init__(display, clock)
        self.snake: Snake = Snake(grid_size_x * 0.5, gird_size_y * 0.5)

        self.food = Food()
        self.food.move_random()
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.snake.x_speed == 0:
                self.snake.x_speed = -1
                self.snake.y_speed = 0
            elif event.key == pygame.K_RIGHT and self.snake.x_speed == 0:
                self.snake.x_speed = 1
                self.snake.y_speed = 0
            elif event.key == pygame.K_UP and self.snake.y_speed == 0:
                self.snake.y_speed = -1
                self.snake.x_speed = 0
            elif event.key == pygame.K_DOWN and self.snake.y_speed == 0:
                self.snake.y_speed = 1
                self.snake.x_speed = 0
    
    def update_game_objects(self):
        # Update location
        if(self.snake.is_moving()):
            self.snake.update_location()
        self.food.update_location()

        # Check obstacle collision
        if self.food.touches(self.snake.get_bounding_box()):
            self.snake.grow()
            self.food.move_random()
        if self.snake.eats_itself():
            global game_mode_current
            game_mode_current = game_mode_gameover


    def draw_game_objects(self):
        # Draw all game objects
        self.surface.fill(white)
        self.snake.draw(self.surface)
        self.food.draw(self.surface)

pygame.init()
game_surface: Union[Surface, SurfaceType]  = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hertford CoderDojo Snake')

clock = pygame.time.Clock()


snake_game_mode = TheGameMode(game_surface, clock)

game_modes = {
    game_mode_started: StartedGameMode(game_surface, clock),
    game_mode_play: TheGameMode(game_surface, clock),
    game_mode_gameover: GameOverGameMode(game_surface, clock)
}


if __name__ == '__main__':
    while not exit_game:
        game_mode = game_modes[game_mode_current]
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
            if event.type == pygame.QUIT:
                exit_game = True
            
            game_mode.handle_event(event)
        game_mode.process_frame()

    pygame.quit()
    quit()
