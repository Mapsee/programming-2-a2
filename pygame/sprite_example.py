# sprite_examply.py
# Introduction to sprites

# Goals:
#   * introduce the Sprite class
#   * subclass the Sprite class

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
RED = (255, 0, 0)
WIDTH = 1024
HEIGHT = 768
TITLE = "Sprite Example"
NUM_BLOCKS = 75
NUM_ENEMIES = 2


class Block(pygame.sprite.Sprite):
    def __init__(self):
        # call the superclass constructor
        super().__init__()

        # Image
        self.image = pygame.Surface((35, 20))
        self.image.fill((0, 255, 0))

        # Rect (x, y, width, height)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image
        self.image = pygame.image.load("./images/link.png")

        # rect
        self.rect = self.image.get_rect()

    def update(self):
        """Move the player with the mouse"""
        # pygame.mouse.get_pos() -> (x, y)
        self.rect.center = pygame.mouse.get_pos()

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

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    score = 0
    lives = 5

    # Create a group of sprites for ALL SPRITES
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # Make lots of blocks on the screen
    for i in range(NUM_BLOCKS):
        block = Block()
        block.rect.x = random.randrange(WIDTH-block.rect.width)
        block.rect.y = random.randrange(HEIGHT-block.rect.height)
        all_sprites.add(block)
        block_sprites.add(block)

    player = Player()
    all_sprites.add(player)

    # Spawn two enemies
    for i in range(NUM_ENEMIES):
        enemies = Enemies()
        enemies.rect.x = random.randrange(WIDTH-enemies.rect.width)
        enemies.rect.y = random.randrange(HEIGHT-enemies.rect.height)
        all_sprites.add(enemies)
        enemy_sprites.add(enemies)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites.update()

        # Sprite group that has the sprites collided with
        blocks_hit_list = pygame.sprite.spritecollide(player, block_sprites, True)
        for block in blocks_hit_list:
            score += 1
            print(score)
            if score == 75:
                print("You win!")
                exit()

        death_list = pygame.sprite.spritecollide(player, enemy_sprites, False)
        for enemies in death_list:
            lives -= 1
            if lives == 0:
                pygame.time.wait(1000)
                print("You died")
                exit()

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
