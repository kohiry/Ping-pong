import pygame
import classes
pygame.init()


size = width, height = 800, 600
screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)
list_balls = []
bol = False
start = False
anim_count = 0

sprite_menu = classes.menu_sprite()

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
    if keys[pygame.K_LEFT]:
        pass
    elif keys[pygame.K_RIGHT]:
        pass
    elif keys[pygame.K_a]:
        pass
    elif keys[pygame.K_d]:
        pass
    elif keys[pygame.K_d]:
        pass
    elif keys[pygame.K_SPACE]:
        start = True

    if start:  # сменить список, на просто объект
        list_balls.append(classes.Ball((400, 560), screen))
        bol = True
    else:
        # draw()
        pass
    screen.fill(Black)
    if bol:

        for i in list_balls:
            i.draw(width, height)
        pygame.display.flip()
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
