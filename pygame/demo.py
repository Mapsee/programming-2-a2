# reach the end game

# TODO: Make it so player can move diagonally without choppiness
# TODO: Collision with block forces player to not move smoothly (Line 48)

# testing the repository for VSC

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
SKY_BLUE = (95, 165, 228)
GRAY = (134, 136, 138)
GREEN = (65, 169, 76)
RED = (255, 0, 0)

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
            # Restrict the block from moving upwards if it hits the bottom of platform
            if self.vel_y > 0:
                self.rect.bottom = block.rect.top
            elif self.vel_y < 0:
                self.rect.top = block.rect.bottom
            elif self.vel_x > 0:
                self.rect.right = block.rect.left
            elif self.vel_x < 0:
                self.rect.left = block.rect.right


    # Player movement
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.vel_x = -3

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.vel_x = 3

    def go_up(self):
        self.vel_y = -3

    def go_down(self):
        self.vel_y = 3

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0
        self.vel_y = 0

class Goal(pygame.sprite.Sprite):
    """End goal that the user must reach"""
    def __init__(self):
        super().__init__()

        width = 40
        height = 40
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

class Platform(pygame.sprite.Sprite):
    """Block that user cannot go through"""
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GRAY)

        self.rect = self.image.get_rect()

class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)

        # rect
        self.rect = self.image.get_rect()
        self.x_vel = 3
        self.y_vel = -3
    def update(self):
        """Move at random"""
        # update x- and y- location of block based on x_vel and y_vel
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # bounce when it reaches the end of the screen
        if self.rect.x < 0 or self.rect.x + self.rect.width > WIDTH:
            self.x_vel *= -1

        if self.rect.y < 0 or self.rect.y + self.rect.height > HEIGHT:
            self.y_vel *= -1

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
        level = [[50, 1600, 500, 500],
                 [50, 1600, 200, 400],
                 [210, 70, 600, 300],
                 [100, 70, 1000, 100],
                 [150, 70, 1000, 300]
                 ]

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

    # Create the player and goal
    player = Player()
    goal = Goal()
    enemy = Enemies()

    # Create the levels
    level_list = []
    level_list.append(Level_01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    # ----- LOCAL VARIABLES
    enemy_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = 100
    all_sprites.add(player)
    all_sprites.add(goal)

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
        current_level.draw(screen)
        enemy_sprites.draw(screen)
        all_sprites.draw(screen)


        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()