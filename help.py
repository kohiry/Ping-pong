import pygame
import random
pygame.init()

class obj:  # class for obstacles
    def __init__(self, x):
        self.x = x
        self.y = 300
        self.speed = 1
        self.clock = pygame.time.Clock()

    def run(self):
        self.clock.tick(300)
        if self.x > 0:
            self.x -= self.speed
            return False
        else:
            return True

    def draw(self, screen):
        pygame.draw.rect(screen, White, (self.x - 25, self.y - 25, 50, 50))
        if self.run():
            return True

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

def download_sound():  # download sound for jump, die, or score
    return {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
            'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
            'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}

def hero_sprites():  # download sprite: dictionary with sprite hero and sprite background
    return ({'move':[pygame.image.load(f'data/hero_run_1.png'),
            pygame.image.load(f'data/hero_run_2.png')],
            'jump':pygame.image.load(f'data/hero.png'),
            'die':pygame.image.load(f'data/hero_die.png'),
            'score':pygame.image.load(f'data/hero_get_score.png'),
            'secret move': pygame.image.load(f'data/hero_move_eyes.png')},
            pygame.image.load('data/background1.bmp'))

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
