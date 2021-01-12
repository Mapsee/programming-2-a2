# Snowscape.py

# Create a relaxing snowscape

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Snowscape"
MAX_SNOW = 150


class Snow:
    def __init__(self, size=2):
        self.colour = WHITE
        self.size = size

        # randomize location
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)

        self.y_vel = random.randrange(1, 3)

    def update(self):
        """Move snow downwards. """
        self.y += self.y_vel

        # if the snow reaches the bottom
        # reset its position
        if self.y > HEIGHT:
            self.y = random.randrange(-15, 0)
            self.x = random.randrange(0, WIDTH)

    def draw(self, screen):
        """Draw snow on screen.

        Arguments:
            screen - surface to draw on

        Returns:
            None
        """
        pygame.draw.circle(
            screen,
            self.size,
            self.colour,
            (self.x, self.y)
        )


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Create snow
    snow_list = []
    for i in range(MAX_SNOW):
        snow = Snow()
        snow_list.append(snow)

    # Create snow list with 150 bigger snow that travels faster
    anothersnow_list = []
    for i in range(MAX_SNOW):
        snow = Snow()
        snow.size = random.randrange(2, 5)
        snow.y_vel = random.randrange(3, 5)
        anothersnow_list.append(snow)
        anothersnow_list.append(snow)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        for snow in snow_list:
            snow.update()
            for snow in anothersnow_list:
                snow.update()

        # ----- DRAW
        screen.fill(BLACK)
        for snow in snow_list:
            snow.draw(screen)
        for snow in anothersnow_list:
            snow.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
