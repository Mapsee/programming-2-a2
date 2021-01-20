# reach the end game

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
SKY_BLUE = (95, 165, 228)
GRAY = (134, 136, 138)

WIDTH = 800
HEIGHT = 800
TITLE = "Reach the Green"


# User controlled block
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image of block, fill with colour
        width = 40
        height = 40
        self.image = pygame.Surface([width, height])
        self.image.fill(SKY_BLUE)

        # Rect
        self.rect = self.image.get_rect()

        # Speed of block
        self.vel_x = 0
        self.vel_y = 0

        # List of sprites we can collide with
        self.level = None

    def update(self):
        """Move the player"""
        # Move left/right
        self.rect.x += self.vel_x

        # Move up/down
        self.rect.y += self.vel_y

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.vel_x > 0:
                self.rect.right = block.rect.left
            elif self.vel_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            self.vel_y = 0

    # Player movement
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.vel_x = -3

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.vel_x = 3

    def go_up(self):
        self.vel_y = 3

    def go_down(self):
        self.vel_y = -3

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0
        self.vel_y = 0


class Platform(pygame.sprite.Sprite):
    """Block that user cannot go through"""
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GRAY)

        self.rect = self.image.get_rect()

class Level(object):
    """Super-class used to define a level. Create a child class for level-specific info"""
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = Player

        # Background image
        self.background = None

    # Update everything on this level
    def update(self):
        """ Update everything in this level"""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """Draw everything on this level"""
        screen.fill(BLACK)

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


# Create platforms for each level
class Level_01(Level):
    """Define level 1"""
    def __init__(self, player):
        Level.__init__(self, player)

        # TODO: List the platforms here
        level = [[210, 70, 500, 500]]

        # Go through array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # Create the player
    player = Player()

    # Create the levels
    level_list = []
    level_list.append(Level_01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    # ----- LOCAL VARIABLES
    all_sprites = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = 100
    all_sprites.add(player)

    done = False
    clock = pygame.time.Clock()

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.go_up()
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_s:
                    player.go_down()
                if event.key == pygame.K_d:
                    player.go_right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.vel_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.vel_x > 0:
                    player.stop()
                if event.key == pygame.K_w and player.vel_y < 0:
                    player.stop()
                if event.key == pygame.K_s and player.vel_y > 0:
                    player.stop()

        # Update
        all_sprites.update()
        current_level.update()

        # ----- DRAW
        all_sprites.draw(screen)
        screen.fill(BLACK)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()





