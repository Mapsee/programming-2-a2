# Running Game

# Make a game that user controls an object on a track, track moves, dodge scenery items, see how far user can go

import pygame
import random

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
MAX_OBSTACLES = 5

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


class Obstacle (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        width = random.randrange(20, 50)
        height = random.randrange(40, 100)

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        # Rect
        self.rect = self.image.get_rect()

        self.rect.bottom = GROUND_HEIGHT
        self.rect.left = WIDTH
        self.x_vel = random.randrange(-7, -3)

    def update(self):
        self.rect.x += self.x_vel

        if self.rect.right < 0:
            self.rect.left = WIDTH


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        width = 90
        height = 125
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Rect
        self.rect = self.image.get_rect()
        
        # Jump
        self.rect.bottom = GROUND_HEIGHT
        self.rect.left = 70
        
        self.jump_limit = GROUND_HEIGHT - 340
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
    all_sprites = pygame.sprite.Group()
    enemy_sprite_list = pygame.sprite.Group()
    player_sprite = pygame.sprite.Group()

    obstacle = Obstacle()
    player = Player()
    track = Track()

    all_sprites.add(player)
    all_sprites.add(track)
    all_sprites.add(obstacle)
    player_sprite.add(player)
    enemy_sprite_list.add(obstacle)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    for i in range(MAX_OBSTACLES):
        obstacle = Obstacle()
        enemy_sprite_list.add(obstacle)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            if not player.jumping:
                player.jumping = True
                player.running = False

            if player.idle:
                player.idle = False

        # Update the player
        all_sprites.update()

        # ----- LOGIC

        # ----- DRAW
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
