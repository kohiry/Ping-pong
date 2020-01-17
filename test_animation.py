import pygame
pygame.init()


size = width, height = 800, 310
screen = pygame.display.set_mode(size)
pygame.display.set_caption('animation sprite')

hero_sprite = {'move':[pygame.image.load(f'data/hero_run_1.png'),
               pygame.image.load(f'data/hero_run_2.png')],
               'jump':pygame.image.load(f'data/hero.png'),
               'die':pygame.image.load(f'data/hero_die.png'),
               'score':pygame.image.load(f'data/hero_get_score.png'),
               'secret move': pygame.image.load(f'data/hero_move_eyes.png')}

image_surf = pygame.image.load('data/background1.bmp')

move = True
IsJump = False
jump = 10
anim_count = 0

x, y = 10, 240

def draw():
    global anim_count
    screen.blit(image_surf, (0, 0))
    if anim_count + 1 >= 15:
        anim_count = 0
    if move:
        screen.blit(hero_sprite['move'][anim_count // 8], (x, y))
        anim_count += 1
    else:
        screen.blit(hero_sprite['jump'], (x, y))

def jumps():
    global jump, y, IsJump, move
    if IsJump:
        y -= jump
        jump -= 1
    if jump <= -11:
        move = True
        IsJump = False
        jump = 10


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
    draw()
    pygame.display.update()
pygame.quit()
