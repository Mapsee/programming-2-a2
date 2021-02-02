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

MAX_CLOUDS = 3
GROUND_HEIGHT = HEIGHT - 70

pygame.init()
dimensions = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(dimensions)


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = pygame.image.load("./main_images/cloudx.png")
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.width = 100
        self.rect = self.image.get_rect()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


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

    def update(self):
        self.rect.x -= game_speed
        if self.rect.right < 0:
            self.rect.left = WIDTH


class BiggerObstacle (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = random.randrange(40, 80)
        height = random.randrange(70, 160)
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        # Rect
        self.rect = self.image.get_rect()
        self.rect.bottom = GROUND_HEIGHT
        self.rect.left = WIDTH + 760

    def update(self):
        self.rect.x -= game_speed
        if self.rect.right < 0:
            self.rect.left = WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Image
        width = 80
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
    cloud_sprite_list = pygame.sprite.Group()

    cloud = Cloud()
    bigger_obstacle = BiggerObstacle()
    obstacle = Obstacle()
    player = Player()
    track = Track()

    cloud_sprite_list.add(cloud)
    all_sprites.add(bigger_obstacle)
    all_sprites.add(player)
    all_sprites.add(track)
    all_sprites.add(obstacle)
    player_sprite.add(player)
    enemy_sprite_list.add(bigger_obstacle)
    enemy_sprite_list.add(obstacle)

    global game_speed, points

    points = 0
    game_speed = 3
    death_count = 0

    font = pygame.font.Font('freesansbold.ttf', 20)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1200, 40)
        screen.blit(text, text_rect)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Create more clouds
    cloud_list = []
    for i in range(MAX_CLOUDS):
        cloud = Cloud()
        cloud_list.append(cloud)

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
        cloud.update()
        for cloud in cloud_list:
            cloud.update()

        # ----- LOGIC
        death_list = pygame.sprite.spritecollide(player, enemy_sprite_list, False)
        for enemies in death_list:
            death_count += 1
            if death_count == 1:
                pygame.time.delay(2000)
                menu(death_count)

        # ----- DRAW
        screen.fill(WHITE)
        all_sprites.draw(screen)
        cloud.draw(screen)
        for cloud in cloud_list:
            cloud.draw(screen)
        score()

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)


def menu(death_count):
    global points
    run = True
    while run:
        screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)
        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            score_rect = score.get_rect()
            score_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)
            screen.blit(score, score_rect)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)