import pygame
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('white'))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, SCREEN_WIDTH - width),
                             random.randint(0, SCREEN_HEIGHT - height))

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)

all_sprites = pygame.sprite.Group()

sprite_1 = Sprite(pygame.Color('blue'), 30, 30)
all_sprites.add(sprite_1)

sprite_2 = Sprite(pygame.Color('red'), 30, 40)
all_sprites.add(sprite_2)

running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite_1.move(x_change, y_change)

        if sprite_1.rect.colliderect(sprite_2.rect):
            all_sprites.remove(sprite_2)
            won = True

    screen.fill(pygame.Color('black')) 
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You Won!", True, pygame.Color("black"))
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, 
                                SCREEN_HEIGHT // 2 - win_text.get_height() // 2))

pygame.display.flip()
clock.tick(60) 

pygame.quit()