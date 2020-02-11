import pygame
import classes
pygame.init()
from screeninfo import get_monitors


size = width, height = get_monitors()[0].width, get_monitors()[0].height
# screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
pygame.display.set_caption('Classic game')

White = (255, 255, 255)
Black = (0, 0, 0)

ismenu = False
start = False
game = False
game_2 = False
restart_menu = False

answer_enemy = None
answer_hero = None

count_tutorial = 0
count_menu = 0
count_rastart_mode = ''
count_rastart = 0

# данные, нужные для более универсального
# представления персонажей на разных мониторах
width_mob = x_mobs = width // 45
y_mobs = height // 2
height_mob = height // 5

speed_mob = 700

# объекты движующиеся
enemy = classes.Enemy(x_mobs, y_mobs, width_mob, height_mob, speed_mob)
hero = classes.Hero(width - x_mobs * 2, y_mobs, width_mob, height_mob, speed_mob)
hero_2 = classes.Hero(x_mobs, y_mobs, width_mob, height_mob, speed_mob)
ball = classes.Ball((400, 560), screen, 35, hero, enemy, hero_2)

enemy.add_ball(ball)
enemy.add_size(height)

# объекты дисплейные
background = classes.DrawBackground()
sprite_tutorial = classes.tutorial_sprite()
sprite_menu = classes.menu_sprite()
restart_sprite = classes.restart_sprite()

# подравнивание меню под экран
classes.transforms(sprite_tutorial, width, height)
classes.transforms(sprite_menu, width, height)
for i in restart_sprite:
    classes.transforms(restart_sprite[i], width, height)

def draw_tutorial():  # отрисовка туториала
    global count_tutorial
    clock = pygame.time.Clock()
    if count_tutorial + 1 >= 150:
        count_tutorial = 0
    screen.blit(sprite_tutorial[count_tutorial // 10], (0, 0))
    count_tutorial += 1
    clock.tick(10)

def draw_menu():  # отрисовка меню
    screen.blit(sprite_menu[count_menu], (0, 0))

def what_restart_menu(who):
    global count_rastart_mode
    count_rastart_mode = who

def draw_restart_menu():
    screen.blit(restart_sprite[count_rastart_mode][count_rastart], (0, 0))




running = True
clock = pygame.time.Clock()
sound = classes.Sound()
while running:
    pygame.mouse.set_visible(False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                ismenu = True
                game = False
                game_2 = False
                restart_menu = False
                ball.score.score_clear()
                ball.pos = width // 2, height // 2
            if not start:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    start = True

            if ismenu and not game and not game_2 and not restart_menu:
                sound.play_jump()
                clock.tick(60)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    count_menu -= 1
                    if count_menu <= 0:
                        count_menu = 3
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    count_menu += 1
                    if count_menu >= 4:
                        count_menu = 1
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if count_menu == 1:
                        ismenu = True
                        start = False
                        game = True
                        game_2 = False
                        restart_menu = False
                    if count_menu == 2:
                        ismenu = True
                        start = False
                        game = False
                        game_2 = True
                        restart_menu = False
                    if count_menu == 3:
                        running = False
                    pygame.time.wait(500)

            if restart_menu and not ismenu and not game and not game_2:
                sound.play_jump()

                clock.tick(60)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    count_rastart -= 1
                    if count_rastart < 0:
                        count_rastart = 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    count_rastart += 1
                    if count_rastart > 1:
                        count_rastart = 0
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if count_rastart == 0:
                        ismenu = True
                        start = False
                        game = False
                        game_2 = False
                        ball.score.score_clear()
                        ball.pos = width // 2, height // 2
                        restart_menu = False
                    if count_rastart == 1:
                        ismenu = False
                        start = False
                        if ball.game == '1 player':
                            game = True
                            game_2 = False
                        if ball.game == '2 player':
                            game = False
                            game_2 = True
                        restart_menu = False

    # события клавишей
    keys = pygame.key.get_pressed()
    if game:
        # управление стрелками или клавиатурой
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and hero.y >= 0:
            hero.move(True)
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and hero.y <= height - height_mob:
            hero.move(False)
    if game_2:
        # управление стрелками или клавиатурой
        if keys[pygame.K_UP] and hero.y >= 0:
            hero.move(True)
        if keys[pygame.K_DOWN] and hero.y <= height - height_mob:
            hero.move(False)
        if keys[pygame.K_w] and hero_2.y >= 0:
            hero_2.move(True)
        if keys[pygame.K_s] and hero_2.y <= height - height_mob:
            hero_2.move(False)

    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill(Black)
    if start:
        if not game and not game_2:
            ismenu = True
    elif not start and not game and not game_2:
        draw_tutorial()
    if ismenu and not game and not game_2:
        draw_menu()
    if game:
        ball.game_mode('1 player')
        # движение моба
        if ball.pos[0] <= width // 2:
            enemy.AI(ball.pos[1], height)
        # отрисовки
        background.draw(width // 2, height, screen)
        background.change_score('enemy', ball.get_score()[1])
        background.change_score('hero', ball.get_score()[0])
        ball.draw(width, height)
        enemy.draw(screen)
        hero.draw(screen)
        answer_enemy = ball.collide(enemy.rects(), width, height, False)
        answer_hero = ball.collide(hero.rects(), width, height, True)

    if game_2:
        ball.game_mode('2 player')
        background.draw(width // 2, height, screen)
        background.change_score('enemy', ball.get_score()[1])
        background.change_score('hero', ball.get_score()[0])
        ball.draw(width, height)
        hero_2.draw(screen)
        hero.draw(screen)
        answer_enemy = ball.collide(hero_2.rects(), width, height, False)
        answer_hero = ball.collide(hero.rects(), width, height, True)
    if answer_enemy != None:
        what_restart_menu(answer_enemy)
        restart_menu = True
    if answer_hero != None:
        what_restart_menu(answer_hero)
        restart_menu = True
    if restart_menu:  # появление рестарт меню
        draw_restart_menu()
        answer_enemy = None
        answer_hero = None
        ismenu = False
        start = False
        game = False
        game_2 = False

    pygame.display.flip()

pygame.quit()

# иногда реально ненавижу git hub, снова для нового коммита
