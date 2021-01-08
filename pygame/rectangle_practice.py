# rectangle_practice.py
# apply objects/classes

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Rectangle Practice"


class Rectangle():
    def __init__(self):
        self.x = 0
        self.y = 0

        self.width = 10
        self.height = 10

        self.colour = (0, 255, 0)

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    rectangle = Rectangle()
    # TODO: CREATE ANOTHER RECTANGLE
    rectangle_two = Rectangle()
    rectangle_two.width, rectangle_two.height = (150, 200)
    rectangle_two.x, rectangle_two.y = (300, 400)
    rectangle_two.colour = WHITE
    #   CHANGE ITS PROPERTIES
    #   reminder use.notation to change properties
    #   i.e. rectangle_two.x = 100

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        pygame.draw.rect(screen, rectangle_two.colour, (rectangle_two.x, rectangle_two.y, rectangle_two.width, rectangle_two.height))
        pygame.draw.rect(screen, rectangle.colour, (rectangle.x, rectangle.y, rectangle.width, rectangle.height))

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()