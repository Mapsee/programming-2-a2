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

pygame.init()
dimensions = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(dimensions)


# User controlled block
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

        # Speed
        self.vel_y = 0

        # List of sprites we can collide with
        self.level = None

    # Move the block
    def update(self):
        self.calc_grav()
        self.rect.y += self.vel_y

        # Stop user from phasing into the track
        track_hit_list = pygame.sprite.spritecollide(self, self.track_list, False)
        for track in track_hit_list:
            if self.vel_y > 0:
                self.rect.bottom = track.rect.top
            self.rect.top = track.rect.bottom

    def calc_grav(self):
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += .35

        # See if we are on the ground.
        if self.rect.y >= HEIGHT - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = HEIGHT - self.rect.height


class Track (object):
    def __init__(self, player):
        self.track_list = pygame.sprite.Group()
        self.player = player
        super().__init__()

        width = WIDTH
        height = 125

        self.image = pygame.Surface([width, height])
        self.image.fill(GRAY)

        self.rect = self.image.get_rect()

        if self.rect.y < HEIGHT - 125:
            self.rect.y = HEIGHT - 125


def main():
    # ----- SCREEN PROPERTIES
    pygame.display.set_caption(TITLE)

    # Create the objects
    active_sprite_list = pygame.sprite.Group()

    player = Player()

    player.rect.x = 125

    active_sprite_list.add(player)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()

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