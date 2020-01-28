import pygame
import classes
pygame.init()
from screeninfo import get_monitors


size = width, height = get_monitors()[0].width, get_monitors()[0].height
# screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((0, 0),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
pygame.display.set_caption('Classic game')

White = (255, 255, 255)
Black = (0, 0, 0)

bol = False
start = False
anim_count = 0

ball = classes.Ball((400, 560), screen, 25)

background = classes.DrawBackground()
sprite_menu = classes.menu_sprite()
classes.transforms(sprite_menu, width, height)

def draw():
    global anim_count
    if anim_count + 1 >= 20:
        anim_count = 0
    screen.blit(sprite_menu[anim_count // 5], (0, 0))
    anim_count += 1


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # события клавишей
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass
    if keys[pygame.K_w]:
        pass
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_SPACE]:
        start = True
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill(Black)

    if start:
        bol = True
    else:
        draw()
    if bol:
        ball.draw(width, height)
        background.draw(width//2, height, screen)
    pygame.display.flip()

pygame.quit()

# добавить отрисовку и движение врага и героя
