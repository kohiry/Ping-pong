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

ismenu = False
start = False
anim_count = 0

# данные, нужные для более универсального
# представления персонажей на разных мониторах
width_mob = x_mobs = width // 45
y_mobs = height // 2
height_mob = height // 5

speed_mob = 360

# объекты движующиеся
ball = classes.Ball((400, 560), screen, 35)
enemy = classes.Enemy(x_mobs, y_mobs, width_mob, height_mob, speed_mob)
hero = classes.Hero(width - x_mobs * 2, y_mobs, width_mob, height_mob, speed_mob)

# объекты дисплейные
background = classes.DrawBackground()
sprite_menu = classes.menu_sprite()

# подравнивание меню под экран
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
    pygame.mouse.set_visible
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and event.pos[1] <= height - height_mob//2 :
            hero.y = event.pos[1]
            clock.tick(60)

    # события клавишей
    keys = pygame.key.get_pressed()

    # управление стрелками или клавиатурой
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and hero.y >= 0:
        hero.move(True)
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and hero.y <= height - height_mob:
        hero.move(False)
    # another act
    if keys[pygame.K_SPACE]:
        start = True
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill(Black)
    if start:
        ismenu = True
    else:
        draw()
    if ismenu:
        # движение моба
        if ball.pos[0] <= width // 2:
            enemy.AI(ball.pos[1], height)
        # отрисовки
        ball.draw(width, height)
        enemy.draw(screen)
        hero.draw(screen)
        ball.collide(enemy.rects(), width, height, False)
        ball.collide(hero.rects(), width, height, True)

        background.draw(width // 2, height, screen)

    pygame.display.flip()

pygame.quit()

# добавить отрисовку и движение врага и героя
