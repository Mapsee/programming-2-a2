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


# TODO: Create menu to start game
def draw_text(text, font_name, size, text_color, position_x, position_y, position):
    # Load fonts
    font = pygame.font.Font(font_name, size)

    text_plane = font.render(text, True, text_color)
    text_rect = text_plane.get_rect()

    # Text position
    if position == "midtop":
        text_rect.midtop = (int(position_x), int(position_y))
    elif position == "topright":
        text_rect.topright = (int(position_x), int(position_y))

    screen.blit(text_plane, text_rect)


# Enemies
class Spikes (pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super().__init__()

        # Image
        width = 70
        height = 70
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        # Rect
        self.rect = self.image.get_rect()

        self.rect.bottom = height-11
        self.rect.left = width

        self.speed = speed

        self.range = 350


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

        # TODO: Check if we collided with something
        #block_hit_list = pygame.sprite.spritecollide(self, self.enemy_list, False)
        #for block in block_hit_list:
        #    quit()

    def calc_grav(self):
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += .35

        # See if we are on the ground.
        if self.rect.y >= HEIGHT - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
            self.vel_y = -10

# TODO: Add the track
# TODO: Add the background scenery (clouds)
# TODO: Add enemies


def main():
    # ----- SCREEN PROPERTIES
    pygame.display.set_caption(TITLE)

    # Create the objects
    active_sprite_list = pygame.sprite.Group()

    player = Player()
    player.rect.x = 340
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