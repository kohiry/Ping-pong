import pygame
import classes
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)

bol = False
start = False
anim_count = 0

ball = classes.Ball((400, 560), screen)
background = classes.DrawBackground()

def menu_sprite():  # download sprite: list with sprite menu
    sprites = []
    for i in range(1, 12):
        sprites.append(pygame.image.load(str(f'data/menu_{str(i)}.png')))
    return sprites

sprite_menu = menu_sprite()

def draw():
    global anim_count
    if anim_count + 1 >= 55:
        anim_count = 0
    screen.blit(sprite_menu[anim_count // 5], (0, 0))
    anim_count += 1



running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass
    elif keys[pygame.K_DOWN]:
        pass
    elif keys[pygame.K_w]:
        pass
    elif keys[pygame.K_s]:
        pass
    elif keys[pygame.K_SPACE]:
        start = True

    if start:  # сменить список, на просто объект
        bol = True
    else:
        draw()
    screen.fill(Black)
    if bol:
        ball.draw(width, height)
    background.draw(width//2, height, screen)
    pygame.display.flip()

pygame.quit()
