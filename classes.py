import pygame
pygame.init()

size = width, height = 800, 600


class Ball:
    def __init__(self, coord, screen, width, obj_1, obj_2, obj_3):
        self.x_rest = 700
        self.y_rest = 500
        self.speed_start = 700
        self.angle_start = 700
        self.game = '1 player'
        self.obj = [obj_1, obj_2, obj_3]  # hero, enemy, hero_2
        self.pos = coord
        self.speed = 700
        self.angle = 700
        self.x, self.y = self.speed, self.angle
        self.screen = screen
        self.width = width
        self.clock = pygame.time.Clock()
        self.rect = pygame.Rect(*coord, width, width)
        self.sound = Sound()
        self.start = True
        self.score = Score()
        self.rewrite_speed_all()

    def game_mode(self, mode):
        self.game = mode

    def rewrite_speed_all(self):
        self.speeds_all = [(-abs(self.speed), -abs(self.angle)), (abs(self.speed), abs(self.angle)),
                            (abs(self.speed), -abs(self.angle)), (-abs(self.speed), abs(self.angle))]
        self.speed, self.angle = abs(self.x), abs(self.y)

    def run(self, x, y, coord, width, height, start, flag):
        self.speed_old = (x, y)
        self.rewrite_speed_all()

        def positive_or_negative(number, speed):
            if number < 0:
                return -speed
            else:
                return speed

        def help(speeds, side):  #возникли проблемы со скоростью, она меняется, из-за чего все привязанные
            # к self.speed вещи начинают барахлить, чсто по итогу приводит к return Non-type
            if flag:
                self.sound.play_jump()
                a = self.update_speed()
                speed_old = list(self.speed_old)
                speed_old[0] += positive_or_negative(speed_old[1], a)
                speed_old[1] += positive_or_negative(speed_old[1], a)
                self.speed_old = tuple(speed_old)
                self.rewrite_speed_all()
                speeds_beta = list(speeds)
                speeds_beta[0] += positive_or_negative(speeds_beta[0], a)
                speeds_beta[1] += positive_or_negative(speeds_beta[1], a)
                return tuple(speeds_beta)
            else:
                self.sound.play_die()
                self.rewrite_speed_all()
                if side == 'right':
                    self.restart_speed()
                    return 1, 1
                elif side == 'left':
                    self.restart_speed()
                    return 2, 2

        if self.speed_old == self.speeds_all[0]:
            if coord[0] <= start:
                return help(self.speeds_all[2], 'left')

            if coord[1] <= 0:
                self.sound.play_jump()
                return self.speeds_all[3]
            else:
                return self.speed_old

        elif self.speed_old == self.speeds_all[1]:
            if coord[0] >= width:
                return help(self.speeds_all[3], 'right')

            if coord[1] >= height:
                self.sound.play_jump()
                return self.speeds_all[2]
            else:
                return self.speed_old

        elif self.speed_old == self.speeds_all[2]:  # туть
            if coord[0] >= width:
                a = help(self.speeds_all[0], 'right')
                return a

            if coord[1] <= 0:
                self.sound.play_jump()
                return self.speeds_all[1]
            else:
                return self.speed_old

        elif self.speed_old == self.speeds_all[3]:
            if coord[0] <= start:
                return help(self.speeds_all[1], 'left')

            if coord[1] >= height:
                # звук отпрыгивания
                return self.speeds_all[0]
            else:
                return self.speed_old
        else:
            return self.speed_old
        print(self.speed_old, self.speeds_all)

    def where_you_stand(self, height, side):  # вспомогательная функция для who_start
        # чтобы определять скорость которую давать мячу, разделяя поле на 2 части
        # смотреть в какой находится юнит
        def check(y):  # вспомогательная функция с проверками
            middle = height // 2
            if y >= middle:  # если выше середины
                return True
            elif y < middle:  # если ниже
                return False

        if side:
            return check(self.obj[0].y)
        else:
            if self.game == '1 player':
                return check(self.obj[1].y)
            elif self.game == '2 player':
                return check(self.obj[2].y)

    def who_start(self, width, height, side):  # куда спавнить мяч в случае пройгрыша
        if side:
            self.score.update_enemy()
            if self.where_you_stand(height, side):  # если выше середины
                self.x, self.y = self.speed, self.angle
            else:  # если ниже
                self.x, self.y = self.speed, -self.angle

        else:
            self.score.update_hero()
            if self.where_you_stand(height, side):  # если выше середины
                self.x, self.y = -self.speed, self.angle
            else:  # если ниже
                self.x, self.y = -self.speed, -self.angle

        self.pos = width // 2, height // 2
        self.update_speed()
        def clear_score():
            self.score.score_clear()
            self.sound.play_score()
        # проверки, если кто-то получил 15 очков, всё обнуляется
        if self.score.score_enemy == 15:
            clear_score()
            if self.game == '1 player':
                return '1 player lose'
            elif self.game == '2 player':
                return '2 player lose'
        elif self.score.score_hero == 15:
            clear_score()
            if self.game == '1 player':
                return '1 player win'
            elif self.game == '2 player':
                return '2 player win'

    def get_score(self):
        return self.score.get_score()

    def rects(self):
        return pygame.Rect(*self.pos, self.width, self.width)

    def update_speed(self):
        speed = 50
        # обновление скоростей для всех объектов
        self.obj[0].speed += speed
        self.speed += speed
        if self.game == '1 player':
            self.obj[1].speed += speed - (speed // 2)
        elif self.game == '2 player':
            self.obj[2].speed += speed
        return speed

    def restart_speed(self):
        self.obj[0].speed = self.obj[0].speed_start
        self.obj[1].speed = self.obj[1].speed_start
        self.obj[2].speed = self.obj[2].speed_start
        self.speed = self.speed_start
        self.angle = self.angle_start

    def collide(self, rect, width, height, flag):

        def positive_or_negative(number):  # функция чтобы проверять число больше или меньше нуля
            if number < 0:
                return False
            elif number >= 0:
                return True

        def find_dot(obj, y):  # не тот y
            jump = obj.height // 5
            middle = obj.height // 2
            if obj.y - self.width // 2 <= y < obj.y + jump:
                return '1'  # 1/5
            elif obj.y + jump <= y <= obj.y + middle:  # 2/5
                return '4'
            elif obj.y + middle <= y <= obj.y + middle + jump:  # 3/5
                return '2'  # от до середина - прыжок до середины + прыжок
            elif obj.y + middle + jump <= y <= obj.y + obj.height - jump:  # 4/5
                return '5'
            elif obj.y + obj.height - jump < y <= obj.y + obj.height + self.width // 2:  # 5/5
                return '3'  # от середины + прыжок до конца
            else:
                return '2'

        def big_check(x, y):  # функция проверки обеих координат
            if positive_or_negative(x):
                if positive_or_negative(y):
                    return 'full'
                else:
                    return 'y < 0'
            else:
                if positive_or_negative(y):
                    return 'x < 0'
                else:
                    return 'y < 0; x < 0'

        def speed(x, y, dot, player):  # player=True игрок с права, player=False, слева
            answer = big_check(x, y)
            module_x = abs(x)
            module_y = abs(y)
            if dot == '1':  # от верхней точки до середина - прыжок
                if player:
                    return -module_x, -module_x
                else:
                    return module_x, -module_x
            elif dot == '2':  # от до середина - прыжок до середины + прыжок
                # все большие расчёты с игреком, это 10, 10 - 5 - 3, для умвеличения угла
                if answer == 'full':
                    if player:
                        return -module_x, abs(module_y - module_y // 2)
                    return module_x, abs(module_y - module_y // 2)
                elif answer == 'y < 0; x < 0':
                    if player:
                        return module_x, abs(module_y - module_y // 2)
                    return module_x, abs(module_y - module_y // 2)
                elif answer == 'x < 0':
                        return -module_x, abs(module_y - module_y // 2)
                if answer == 'y < 0':
                    return module_x, -abs(module_y - module_y // 2)
                print('пропустил big_check')
            elif dot == '3':  # от середины + прыжок до конца
                if player:
                    return -module_x, module_x
                else:
                    return module_x, module_x
            elif dot == '4' or dot == '5':
                if player:
                    return self.run(x, y, self.pos, rect.x - rect.width, height, 0, True)
                else:
                    return self.run(x, y, self.pos, width, height, rect.x + rect.width, True)


        if self.rects().colliderect(rect):
            if flag:
                x, y = self.run(self.x, self.y, self.pos, rect.x - rect.width, height, 0, True)
                self.x, self.y = speed(x, y, find_dot(self.obj[0], int(self.pos[1])), True)
            else:
                x, y = self.run(self.x, self.y, self.pos,  width, height, rect.x + rect.width, True)
                if self.game == '1 player':
                    self.x, self.y = speed(x, y, find_dot(self.obj[1], self.pos[1]), False)
                elif self.game == '2 player':
                    self.x, self.y = speed(x, y, find_dot(self.obj[2], self.pos[1]), False)
                else:
                    print('Ошибка self.game, 195 строка classes')
            self.rewrite_speed_all()

        else:
            self.x, self.y = self.run(self.x, self.y, self.pos, width + 200, height, 0, False)
        if self.x == 1:
            answer = self.who_start(width, height, True)
            if answer != None:
                return answer
        elif self.x == 2:
            answer = self.who_start(width, height, False)
            if answer != None:
                return answer
        if -50 < self.y < 50:
            if positive_or_negative(self.y):
                self.y = -100
            else:
                self.y = 100

    def draw(self, width, height):
        x, y = self.pos
        x += self.x // 60
        y += self.y // 60
        self.clock.tick(60)
        self.pos = (int(x), int(y))
        pygame.draw.rect(self.screen, (255, 255, 255), (*self.pos, self.width, self.width))


def transforms(sprite, width, height):
    for i in range(len(sprite)):
        sprite[i] = pygame.transform.scale(sprite[i], (width, height))

def tutorial_sprite():  # download sprite: list with sprite tutorial
    sprites = []
    for i in range(1, 16):
        sprites.append(pygame.image.load(f'data/tutorial_{str(i)}.png'))
    return sprites

def menu_sprite(): # download sprite: list with sprite menu
    sprites = []
    for i in range(1, 5):
        sprites.append(pygame.image.load(f'data/menu_{str(i)}.png'))
    return sprites

def restart_sprite(): # download sprite: list with sprite menu
    sprites = {}
    sprites['1 player win'] = [pygame.image.load(f'data/restart_bar_{str(i)}.png') for i in range(1, 3)]
    sprites['1 player lose'] = [pygame.image.load(f'data/restart_bar_{str(i)}.png') for i in range(3, 5)]
    sprites['2 player lose'] = [pygame.image.load(f'data/restart_bar_{str(i)}.png') for i in range(5, 7)]
    sprites['2 player win'] = [pygame.image.load(f'data/restart_bar_{str(i)}.png') for i in range(7, 9)]
    return sprites


class Hero:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.speed_start = speed
        self.color = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, flag):  # flag - bool, True = вправо, False = влево
        if flag:
            self.y -= self.speed // 60
        else:
            self.y += self.speed // 60
        self.clock.tick(60)

    def rects(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.ball = []
        self.size = ''
        self.height = height
        self.width = width
        self.speed = speed
        self.speed_start = speed
        self.color = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.rect = pygame.Rect(x, y, width, height)

    def add_ball(self, ball):
        self.ball.append(ball)

    def AI(self, y, display_height):  # y - координата объекта ball
        # дбоавить объект класса ball чтобы следить за его скоростью, если летит плоско
        # то берём другую скоростью
        if self.y + (self.height // 4) <= self.ball[0].pos[1] <= self.y + self.height - (self.height // 4):
            self.y += 0
        elif self.y + (self.height // 2) > y and self.y >= 0:
            self.y -= self.speed // 60
        elif self.y + (self.height // 2) < y and self.y <= display_height - self.height:
            self.y += self.speed // 60
        self.clock.tick(60)

    def rects(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class DrawBackground:
    def __init__(self):
        self.jump = 120
        self.width = 5
        self.height = 100
        self.text_y = 10
        self.score = {'enemy':'0', 'hero':'0'}

    def change_score(self, who, score):
        if who == 'enemy' or who == 'hero':
            self.score[who] = str(score)
        else:
            print('Неверные даны данные')

    def draw(self, x, Dheight, screen):
        font = pygame.font.Font('pixle_font.ttf', 70)
        White = (255, 255, 255)
        enemy_txt = font.render(self.score['enemy'], 1, (255, 255, 255))
        hero_txt = font.render(self.score['hero'], 1, (255, 255, 255))
        # отрисовка поля
        for i in range(0, Dheight, self.jump):  # отрисовка разграничивающих полос на поле
            pygame.draw.rect(screen, (255, 255, 255), (x - self.width//2, i,\
                             self.width, self.height))

        # отрисовка счёта
        screen.blit(enemy_txt, (x // 2 - enemy_txt.get_width() // 2, self.text_y))  # 1/4 ширины
        screen.blit(hero_txt, ((x + x // 2) - hero_txt.get_width() // 2, self.text_y))  # 3/4


class Sound:  # class for downlod and play sound
    def __init__(self):
        self.sound = {'die_sound': pygame.mixer.Sound(r'Sound\die.ogg'),
                      'jump_sound': pygame.mixer.Sound(r'Sound\jump.ogg'),
                      'score_sound': pygame.mixer.Sound(r'Sound\score.ogg')}

    def play_die(self):
        self.sound['die_sound'].play()

    def play_jump(self):
        self.sound['jump_sound'].play()

    def play_score(self):
        self.sound['score_sound'].play()


class Score:
    def __init__(self):
        self.score_enemy = 0
        self.score_hero = 0

    def update_hero(self):
        self.score_hero += 1

    def update_enemy(self):
        self.score_enemy += 1

    def score_clear(self):
        self.score_hero = 0
        self.score_enemy = 0

    def get_score(self):
        return (self.score_hero, self.score_enemy)
