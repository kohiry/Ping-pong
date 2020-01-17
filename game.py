import pygame
import random
import help
pygame.init()


size = width, height = 800, 310
screen = pygame.display.set_mode(size)
pygame.display.set_caption('animation sprite')



move = True
IsJump = False
jump = 10
anim_count = 0

x, y = 10, 240

def random_for_move_obstacles(x):  # function for spawn random obstacles
    n = random.randint(2, 5)
    if n == 2:
        for i in range(n):
            rects.append(obj(x))
            x += 300
    elif n == 3:
        for i in range(n):
            rects.append(obj(x))
            x += 200
    elif n == 4:
        for i in range(2):
            rects.append(obj(x))
            x += 50
    elif n == 5:
        for i in range(3):
            rects.append(obj(x))
            x += 50

def draw_animation():  # anim_count - 0, for count sprite:
    global anim_count
    screen.blit(background, (0, 0))
    if anim_count + 1 >= 15:
        anim_count = 0
    if move:
        screen.blit(hero_sprite['move'][anim_count // 8], (x, y))
        anim_count += 1
    else:
        screen.blit(hero_sprite['jump'], (x, y))

def jumps():  # move, IsJump - bool; jump = 10, y = <any number>
    global jump, y, IsJump, move
    if IsJump:
        y -= jump
        jump -= 1
    if jump <= -11:
        move = True
        IsJump = False
        jump = 10

sound = help.download_sound()
hero_sprite, background = help.hero_sprites()

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        move = False
        IsJump = True
        anim_count = 0
    jumps()
    draw_animation()
    pygame.display.update()
pygame.quit()
