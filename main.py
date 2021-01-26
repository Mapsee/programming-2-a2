# Running Game

# Make a game that user controls an object on a track, track moves, dodge scenery items, see how far user can go

import pygame

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (134, 136, 138)
RED = (255, 0, 0)

# Screen framework
WIDTH = 1280
HEIGHT = 720
TITLE = "RUN RUN!"

GROUND_HEIGHT = HEIGHT - 70

pygame.init()
dimensions = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(dimensions)


# User controlled block

class Track(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = WIDTH
        height = 70

        self.image = pygame.Surface([width, height])
        self.image.fill(GRAY)

        self.rect = self.image.get_rect()

        if self.rect.y < HEIGHT - 70:
            self.rect.y = HEIGHT - 70

class Obstacles:
    def __init__(self, speed=10):
        self.colour = RED
        self.rect.bottom = GROUND_HEIGHT - 11
        self.rect.left = SCREEN_WIDTH
        
        self.speed = speed
        
        self.range = 240
    
        
            
        
        
        
class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        width = 125
        height = 125
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Rect
        self.rect = self.image.get_rect()
        
        # Jump
        self.rect.bottom = GROUND_HEIGHT
        self.rect.left = 70
        
        self.jump_limit = GROUND_HEIGHT - 290
        self.jump_speed = 50
        self.gravity_up = 4
        self.gravity_down = 2
        
        # Set booleans
        self.idle = True
        self.running = False
        self.jumping = False
        self.falling = False
        
        self.call_count = 0
    
    # Move the block
    def update(self):
        
        if self.jumping:

            if not self.falling:
                self.rect.bottom -= self.jump_speed

                if self.jump_speed >= self.gravity_up:
                    self.jump_speed -= self.gravity_up

                if self.rect.bottom < self.jump_limit:

                    self.jump_speed = 0

                    self.falling = True

            else:
                self.rect.bottom += self.jump_speed
                self.jump_speed += self.gravity_down

                if self.rect.bottom > GROUND_HEIGHT:

                    self.rect.bottom = GROUND_HEIGHT

                    self.jump_speed = 50

                    self.jumping = False
                    self.falling = False
                    self.running = True

        self.call_count = self.call_count + 1  
        
def main():
    # ----- SCREEN PROPERTIES
    pygame.display.set_caption(TITLE)

    # Create
    active_sprite_list = pygame.sprite.Group()

    player = Player()
    track = Track()

    active_sprite_list.add(player)
    active_sprite_list.add(track)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
            if event.type == pygame.key.get_pressed():
                if event.key == pygame.K_SPACE or pygame.K_UP:
                    if not player.jumping:
                        player.jumping = True
                        player.running = False

                    if player.idle:
                        player.idle = False
  

        # Update the player
        active_sprite_list.update()

        # ----- LOGIC

        # ----- DRAW
        screen.fill(WHITE)
        active_sprite_list.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
