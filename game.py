import pygame
import random
import help
pygame.init()


size = width, height = 800, 310
screen = pygame.display.set_mode(size)
pygame.display.set_caption('animation sprite')

class obj:  # class for obstacles
    def __init__(self, x):
        self.x = x
        self.y = 220
        self.speed = 10
        self.clock = pygame.time.Clock()

    def run(self):
        self.clock.tick(300)
        if self.x > 0:
            self.x -= self.speed
            return False
        else:
            return True

    def draw(self, screen):
        screen.blit(pygame.image.load('data/obstacle_1.png'), (self.x, self.y))
        if self.run():
            return True

class Hero:
    def __init_(self):
        self.x = 10
        self.y = 240
        self.speed = 10
        self.clock = pygame.time.Clock()
        self.jump = 10
        self.isJump = False
        self.move = False
        self.anim_count = 0
        self.hero_sprite = {'move':[pygame.image.load(f'data/hero_run_1.png'),
                            pygame.image.load(f'data/hero_run_2.png')],
                            'jump':pygame.image.load(f'data/hero.png'),
                            'die':pygame.image.load(f'data/hero_die.png'),
                            'score':pygame.image.load(f'data/hero_get_score.png'),
                            'secret move': pygame.image.load(f'data/hero_move_eyes.png')}

    def jumps(self):  # move, IsJump - bool; jump = 10, y = <any number>
        if self.IsJump:
            self.y -= self.jump
            self.jump -= 1
        if self.jump <= -16:
            self.move = True
            self.IsJump = False
            self.jump = 15

    def draw_animation(self, screen):  # anim_count - 0, for count sprite:
        screen.blit(background, (0, 0))
        if self.anim_count + 1 >= 15:
            self.anim_count = 0
        if self.move:
            screen.blit(hero_sprite['move'][anim_count // 8], (x, y))
            self.anim_count += 1
        else:
            screen.blit(hero_sprite['jump'], (x, y))

class Sound:
    def __init__(self):
        self.sound = {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
                      'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
                      'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}


move = True
IsJump = False
jump = 15
anim_count = 0
White = (0, 0, 0)

x, y = 10, 240
x_rect = 850
y_rect = 300

rects = []


def random_for_move_obstacles(x):  # function for spawn random obstacles
    n = random.randint(2, 6)
    if n == 2:
        for i in range(2):
            rects.append(obj(x))
            x += 300
    elif n == 3:
        for i in range(4):
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
    elif n == 6:
        for i in range(6):
            rects.append(obj(x))
            x += 200


flag = True
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
    if flag:
        random_for_move_obstacles(x_rect)
        flag = False
        print(rects)
    for i in rects:
        if i.draw(screen):
            del rects[rects.index(i)]
            if len(rects) == 0:
                random_for_move_obstacles(x_rect)
    pygame.display.update()
pygame.quit()
