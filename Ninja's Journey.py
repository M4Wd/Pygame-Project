import pygame
import random

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)

pygame.init()

clock = pygame.time.Clock
game_state = "start_menu"

pygame.mixer.init()


class Button(pygame.sprite.Sprite):
    def __init__(self):
        super(Button, self).__init__()
        self.surf = pygame.Surface((100, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect().move(100, 200)


def draw_start_menu():
    screen.blit(title_screen, (0, 0))
    font = pygame.font.Font('data/HanaleiFill-Regular.ttf', 45)
    font2 = pygame.font.Font('data/Hanalei-Regular.ttf', 45)
    font3 = pygame.font.Font('data/Hanalei-Regular.ttf', 40)
    font4 = pygame.font.Font('data/HanaleiFill-Regular.ttf', 40)
    title = font.render("Ninja's journey", True, "#D6B450")
    title2 = font2.render("Ninja's journey", True, "#775f1b")
    start_button_font = font.render('Start', True, "#D6B450")
    start_button_font2 = font2.render('Start', True, "#775f1b")
    help_text = font4.render("Help", True, "#D6B450")
    help_text2 = font3.render("Help", True, "#775f1b")
    screen.blit(title, (70, 135))
    screen.blit(title2, (70, 135))
    screen.blit(start_button_font, (95, 325))
    screen.blit(start_button_font2, (95, 325))
    screen.blit(help_text, (272, 330))
    screen.blit(help_text2, (272, 330))
    pygame.display.update()


def draw_help_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render("Инструкция к управлению", True, "white")
    screen.blit(title, (SCREEN_WIDTH - title.get_width() // 2, 50))


def draw_level_selection():
    bg = pygame.image.load("data/background.jpeg")
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(bg, (0, 0))
    font = pygame.font.SysFont('arial', 50, True)
    selection_text = font.render("Выберите уровень:", True, (255, 255, 255))
    screen.blit(selection_text, (SCREEN_WIDTH / 2 - selection_text.get_width() / 2, 50))
    pygame.draw.rect(screen, (150, 150, 150), (50, 200, 100, 100), border_radius=10)
    level_1_text = font.render("1", True, ("black"))
    screen.blit(level_1_text, (100 - level_1_text.get_width() // 2, 225))
    pygame.draw.rect(screen, (150, 150, 150), (250, 200, 100, 100), border_radius=10)
    level_2_text = font.render("2", True, ("black"))
    screen.blit(level_2_text, (300 - level_2_text.get_width() // 2, 225))
    pygame.draw.rect(screen, (150, 150, 150), (450, 200, 100, 100), border_radius=10)
    level_3_text = font.render("3", True, ("black"))
    screen.blit(level_3_text, (500 - level_3_text.get_width() // 2, 225))
    pygame.draw.rect(screen, (150, 150, 150), (650, 200, 100, 100), border_radius=10)
    level_4_text = font.render("4", True, ("black"))
    screen.blit(level_4_text, (700 - level_4_text.get_width() // 2, 225))
    pygame.draw.rect(screen, (150, 150, 150), (50, 400, 100, 100), border_radius=10)
    level_5_text = font.render("5", True, ("black"))
    screen.blit(level_5_text, (100 - level_5_text.get_width() // 2, 425))
    pygame.draw.rect(screen, (150, 150, 150), (250, 400, 100, 100), border_radius=10)
    level_6_text = font.render("6", True, ("black"))
    screen.blit(level_6_text, (300 - level_6_text.get_width() // 2, 425))
    pygame.draw.rect(screen, (150, 150, 150), (450, 400, 100, 100), border_radius=10)
    level_7_text = font.render("7", True, ("black"))
    screen.blit(level_7_text, (500 - level_7_text.get_width() // 2, 425))
    pygame.draw.rect(screen, (150, 150, 150), (650, 400, 100, 100), border_radius=10)
    level_8_text = font.render("8", True, ("black"))
    screen.blit(level_8_text, (700 - level_8_text.get_width() // 2, 425))
    if blocked == 1:
        blocked_text = font.render("Заблокировано", True, ("white"))
        screen.blit(blocked_text, (SCREEN_WIDTH / 2 - blocked_text.get_width() / 2, 500))
    pygame.display.update()


def draw_game_over_screen():
    global next, again, leave, map_drawn, lvl_2_unlocked, lvl_3_unlocked, lvl_4_unlocked, lvl_5_unlocked, lvl_6_unlocked, lvl_7_unlocked, lvl_8_unlocked
    for platform in platforms:
        platform.kill()
    for door in doors:
        door.kill()
    for spike in spikes:
        spike.kill()
    map_drawn = 0
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    if last_level == "level 1":
        lvl_2_unlocked = 1
    elif last_level == "level 2":
        lvl_3_unlocked = 1
    elif last_level == "level 3":
        lvl_4_unlocked = 1
    elif last_level == "level 4":
        lvl_5_unlocked = 1
    elif last_level == "level 5":
        lvl_6_unlocked = 1
    elif last_level == "level 6":
        lvl_7_unlocked = 1
    elif last_level == "level 7":
        lvl_8_unlocked = 1
    if last_level != "level 8":
        title = font.render('Уровень пройден!', True, (255, 255, 255))
        next_level = font.render('Следующий уровень', True, (255, 255, 255))
        next_level_button = Button()
        next_level_button.surf = pygame.surface.Surface((320, 50))
        next_level_button.rect = next_level_button.surf.get_rect().move(100, 400)
        if next_level_button.rect.collidepoint(pygame.mouse.get_pos()):
            next = 1
        else:
            next = 0
        restart = font.render('Заново', True, (255, 255, 255))
        restart_button = Button()
        restart_button.rect = restart_button.surf.get_rect().move(450, 400)
        if restart_button.rect.collidepoint(pygame.mouse.get_pos()):
            again = 1
        else:
            again = 0
        quit_text = font.render('Меню', True, (255, 255, 255))
        quit_button = Button()
        quit_button.rect = quit_button.surf.get_rect().move(600, 400)
        if quit_button.rect.collidepoint(pygame.mouse.get_pos()):
            leave = 1
        else:
            leave = 0
        screen.blit(title, (275, 200))
        screen.blit(next_level, (100, 400))
        screen.blit(restart, (450, 400))
        screen.blit(quit_text, (600, 400))
    else:
        title = font.render('Уровень пройден!', True, (255, 255, 255))
        restart = font.render('Заново', True, (255, 255, 255))
        restart_button = Button()
        restart_button.rect = restart_button.surf.get_rect().move(250, 400)
        if restart_button.rect.collidepoint(pygame.mouse.get_pos()):
            again = 1
        else:
            again = 0
        quit_text = font.render('Меню', True, (255, 255, 255))
        quit_button = Button()
        quit_button.rect = quit_button.surf.get_rect().move(475, 400)
        if quit_button.rect.collidepoint(pygame.mouse.get_pos()):
            leave = 1
        else:
            leave = 0
        screen.blit(title, (275, 200))
        screen.blit(restart, (250, 400))
        screen.blit(quit_text, (475, 400))
    pygame.display.update()


def Gravity(Character, inverted=0):
    global touching_left, touching_right, jumping_left, jumping_right, jumping_rn, falling, can_jump_right, can_jump_left, jump_to_the_right, jump_to_the_left
    if touching_right == 1 or touching_left == 1:
        if touching_right == 1:
            Character.surf = pygame.image.load("data/wall_right.png").convert()
            Character.surf.set_colorkey((255, 255, 255))
            can_jump_left = 1
        elif touching_left == 1:
            can_jump_right = 1
            Character.surf = pygame.image.load("data/wall_left.png").convert()
            Character.surf.set_colorkey((255, 255, 255))
        falling = 1
    else:
        falling = 5
        can_jump_right = 0
        can_jump_left = 0
    if Character.rect.bottom < SCREEN_HEIGHT and inverted == 0 and jumping_left == 0 and jumping_right == 0:
        if touching_right == 0 and touching_left == 0 and standing == 0:
            if Character.last_key == "right":
                Character.surf = pygame.image.load("data/jumping_right8.png").convert()
                Character.surf.set_colorkey((255, 255, 255))
            else:
                Character.surf = pygame.image.load("data/jumping_left8.png").convert()
                Character.surf.set_colorkey((255, 255, 255))
        Character.rect.move_ip(0, falling)
        for platform in platforms:
            if pygame.sprite.collide_rect(Character, platform):
                Character.rect.bottom = platform.rect.top
        Character.rect.move_ip(0, falling)
        for platform in platforms:
            if pygame.sprite.collide_rect(Character, platform):
                Character.rect.bottom = platform.rect.top

    elif inverted == 0 and (jumping_left > 0 or jumping_right > 0):
        if jumping_left > 0:
            Character.surf = pygame.image.load(left_jump[int(jump_to_the_left) % 7]).convert()
            Character.surf.set_colorkey((255, 255, 255))
            jump_to_the_left += 0.3
            Character.last_key = "left"
            x = Character.rect.x
            y = Character.rect.y
            Character.rect.move_ip(-5, -5)
            for platform in platforms:
                if pygame.sprite.collide_rect(Character, platform):
                    Character.rect.x = x
                    Character.rect.y = y
                    jumping_left = 1
            jumping_left -= 1
        elif jumping_right > 0:
            Character.surf = pygame.image.load(right_jump[int(jump_to_the_right) % 7]).convert()
            Character.surf.set_colorkey((255, 255, 255))
            jump_to_the_right += 0.3
            Character.last_key = "right"
            x = Character.rect.x
            y = Character.rect.y
            Character.rect.move_ip(5, -5)
            for platform in platforms:
                if pygame.sprite.collide_rect(Character, platform):
                    Character.rect.x = x
                    Character.rect.y = y
                    jumping_right = 1
            jumping_right -= 1
        else:
            Character.rect.move_ip(0, falling)
            for platform in platforms:
                if pygame.sprite.collide_rect(Character, platform):
                    Character.rect.bottom = platform.rect.top
            Character.rect.move_ip(0, falling)
            for platform in platforms:
                if pygame.sprite.collide_rect(Character, platform):
                    Character.rect.bottom = platform.rect.top
    elif inverted > 0:
        if Character.last_key == "right":
            Character.surf = pygame.image.load("data/jumping_right2.png").convert()
            Character.surf.set_colorkey((255, 255, 255))
            jump_to_the_right += 0.3
        else:
            Character.surf = pygame.image.load("data/jumping_left2.png").convert()
            Character.surf.set_colorkey((255, 255, 255))
            jump_to_the_left += 0.3
        x = Character.rect.x
        y = Character.rect.y
        Character.rect.move_ip(0, -5)
        for platform in platforms:
            if pygame.sprite.collide_rect(Character, platform):
                Character.rect.x = x
                Character.rect.y = y
                jumping_rn = 0


class Door(pygame.sprite.Sprite):
    def __init__(self):
        super(Door, self).__init__()
        self.surf = pygame.image.load("data/door.png").convert()
        self.surf = pygame.transform.scale(self.surf, (80, 60))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()


class Spike(pygame.sprite.Sprite):
    def __init__(self):
        super(Spike, self).__init__()
        self.surf = pygame.image.load("data/images.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.rect = self.surf.get_rect()
        self.mask = pygame.mask.from_surface(self.surf)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("data/idle_right.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = pygame.rect.Rect(0, 0, 30, 45)
        self.rect = self.rect.move(30, 500)
        self.last_key = "right"

    def update(self, pressed_keys):
        global touching_left, touching_right, standing, jumping_right, jumping_left, game_state, map_drawn, last_level, right, left, jumping_rn
        if touching_right == 0 and touching_left == 0 or self.rect.bottom == SCREEN_HEIGHT:
            if jumping_right == 0 and jumping_left == 0:
                if pressed_keys[pygame.key.key_code("a")]:
                    if self.rect.bottom == SCREEN_HEIGHT or standing == 1:
                        self.surf = pygame.image.load(left_run[int(left) % 6]).convert()
                        self.surf.set_colorkey((255, 255, 255))
                        left += 0.2
                    x = self.rect.x
                    y = self.rect.y
                    self.last_key = "left"
                    self.rect.move_ip(-5, 0)
                    for platform in platforms:
                        if pygame.sprite.collide_rect(self, platform):
                            self.rect.x = x
                            self.rect.y = y
                            self.surf = pygame.image.load("data/idle_left.png").convert()
                            self.surf.set_colorkey((255, 255, 255))
                            jumping_rn = 0
                elif pressed_keys[pygame.key.key_code("d")]:
                    if self.rect.bottom == SCREEN_HEIGHT or standing == 1:
                        self.surf = pygame.image.load(right_run[int(right) % 6]).convert()
                        self.surf.set_colorkey((255, 255, 255))
                        right += 0.2
                    x = self.rect.x
                    y = self.rect.y
                    self.last_key = "right"
                    self.rect.move_ip(5, 0)
                    for platform in platforms:
                        if pygame.sprite.collide_rect(self, platform):
                            self.rect.x = x
                            self.rect.y = y
                            self.surf = pygame.image.load("data/idle_right.png").convert()
                            self.surf.set_colorkey((255, 255, 255))
                            jumping_rn = 0
                else:
                    if self.rect.bottom == SCREEN_HEIGHT or standing == 1:
                        if self.last_key == "left":
                            self.surf = pygame.image.load("data/idle_left.png").convert()
                            self.surf.set_colorkey((255, 255, 255))
                        else:
                            self.surf = pygame.image.load("data/idle_right.png").convert()
                            self.surf.set_colorkey((255, 255, 255))

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        for platform in platforms:
            if self.rect.right == platform.rect.left and (
                    platform.rect.bottom > self.rect.bottom > platform.rect.top or platform.rect.top < self.rect.top < platform.rect.bottom):
                touching_right = 1
                break
            else:
                touching_right = 0
            if self.rect.left == platform.rect.right and (
                    platform.rect.bottom > self.rect.bottom > platform.rect.top or platform.rect.top < self.rect.top < platform.rect.bottom):
                touching_left = 1
                break
            else:
                touching_left = 0
            if self.rect.bottom == platform.rect.top and (
                    (platform.rect.left - 5 < player.rect.left < platform.rect.right + 5) or (
                    platform.rect.left - 5 < player.rect.right < platform.rect.right + 5)):
                standing = 1
                break
            else:
                standing = 0
        for door in doors:
            if pygame.sprite.collide_rect(self, door):
                if game_state != "game_over":
                    last_level = game_state
                    game_state = "game_over"
                    self.rect = self.surf.get_rect().move(30, 500)
        if pygame.sprite.spritecollide(self, spikes, False):
            self.rect = self.surf.get_rect().move(30, 500)


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.surf = pygame.image.load("data/bamboo.jpg").convert()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.rect = pygame.rect.Rect(0, 0, 50, 50)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("data/background1.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
title_screen = pygame.image.load("data/title_screen.jpg")
title_screen = pygame.transform.scale(title_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
platforms = pygame.sprite.Group()
doors = pygame.sprite.Group()
spikes = pygame.sprite.Group()
level_1 = pygame.sprite.Group()
level_2 = pygame.sprite.Group()
level_3 = pygame.sprite.Group()
level_4 = pygame.sprite.Group()
level_5 = pygame.sprite.Group()
level_6 = pygame.sprite.Group()
level_7 = pygame.sprite.Group()
level_8 = pygame.sprite.Group()

left_run = ["data/running_left1.png", "data/running_left2.png", "data/running_left3.png", "data/running_left4.png",
            "data/running_left5.png", "data/running_left6.png"]
right_run = ["data/running_right1.png", "data/running_right2.png", "data/running_right3.png", "data/running_right4.png",
             "data/running_right5.png", "data/running_right6.png"]
right_jump = ["data/jumping_right1.png", "data/jumping_right2.png", "data/jumping_right3.png",
              "data/jumping_right4.png", "data/jumping_right5.png", "data/jumping_right6.png",
              "data/jumping_right7.png"]
left_jump = ["data/jumping_left1.png", "data/jumping_left2.png", "data/jumping_left3.png", "data/jumping_left4.png",
             "data/jumping_left5.png", "data/jumping_left6.png", "data/jumping_left7.png"]

right = 0
left = 0
jump_to_the_right = 0
jump_to_the_left = 0
can_jump_left = 0
can_jump_right = 0
jumping_left = 0
jumping_right = 0
touching_right = 0
touching_left = 0
standing = 0
falling = 5
jumping_rn = 0
next = 0
leave = 0
again = 0
fps = 60
map_drawn = 0
last_level = ""
blocked = 0
lvl_2_unlocked = 0
lvl_3_unlocked = 0
lvl_4_unlocked = 0
lvl_5_unlocked = 0
lvl_6_unlocked = 0
lvl_7_unlocked = 0
lvl_8_unlocked = 0

jump_sound = pygame.mixer.Sound("data/jump.wav")
jump_sound2 = pygame.mixer.Sound("data/jump_hp.wav")
jump_sound3 = pygame.mixer.Sound("data/jump_lp.wav")
flip_sound = pygame.mixer.Sound("data/flip.wav")
flip_sound2 = pygame.mixer.Sound("data/flip_hp.wav")
flip_sound3 = pygame.mixer.Sound("data/flip_lp.wav")

running = True
ready_to_start = 0
choosing_level_1 = 0
choosing_level_2 = 0
choosing_level_3 = 0
choosing_level_4 = 0
choosing_level_5 = 0
choosing_level_6 = 0
choosing_level_7 = 0
choosing_level_8 = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if game_state == "help_screen" or game_state == "select_level":
                    game_state = "start_menu"
            if event.key == pygame.key.key_code("space"):
                if player.rect.bottom == SCREEN_HEIGHT or standing == 1 or touching_right == 1 or touching_left == 1:
                    if can_jump_right == 1:
                        flip_sound.play()
                        jumping_right = 15
                    elif can_jump_left == 1:
                        x = random.choice([flip_sound, flip_sound2, flip_sound3])
                        x.play()
                        jumping_left = 15
                    else:
                        x = random.choice([jump_sound, jump_sound2, jump_sound3])
                        x.play()
                        jumping_rn = 40
            if event.key == pygame.key.key_code("p"):
                last_level = game_state
                game_state = "game_over"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ready_to_start == 1:
                game_state = "select_level"
                ready_to_start = 0
            elif choosing_level_1 == 1:
                game_state = "level 1"
                choosing_level_1 = 0
                blocked = 0
            elif choosing_level_2 == 1:
                if lvl_2_unlocked == 1:
                    game_state = "level 2"
                    choosing_level_2 = 0
                    blocked = 0
                else:
                    blocked = 1
            elif choosing_level_3 == 1:
                if lvl_2_unlocked == 1:
                    game_state = "level 2"
                    choosing_level_2 = 0
                    blocked = 0
                else:
                    blocked = 1
            elif choosing_level_3 == 1:
                if lvl_3_unlocked == 1:
                    game_state = "level 3"
                    choosing_level_3 = 0
                    blocked = 0
                else:
                    blocked = 1
            elif choosing_level_4 == 1:
                if lvl_4_unlocked == 1:
                    game_state = "level 4"
                    choosing_level_4 = 0
                    blocked = 0
                else:
                    blocked = 1
            elif choosing_level_5 == 1:
                if lvl_5_unlocked == 1:
                    game_state = "level 5"
                    choosing_level_5 = 0
                    blocked = 0
                else:
                    blocked = 1
            elif choosing_level_6 == 1:
                if lvl_6_unlocked == 1:
                    game_state = "level 6"
                    choosing_level_6 = 0
                    blocked = 0
                else:
                    blocked = 1
            elif choosing_level_7 == 1:
                if lvl_7_unlocked == 1:
                    game_state = "level 7"
                    choosing_level_7 = 0
                    blocked = 0
                else:
                    blocked = 1
            elif choosing_level_8 == 1:
                if lvl_8_unlocked == 1:
                    game_state = "level 8"
                    choosing_level_8 = 0
                    blocked = 0
                else:
                    blocked = 1
            elif next == 1:
                if last_level == "level 1":
                    game_state = "level 2"
                    next = 0
                elif last_level == "level 2":
                    game_state = "level 3"
                    next = 0
                elif last_level == "level 3":
                    game_state = "level 4"
                    next = 0
                elif last_level == "level 4":
                    game_state = "level 5"
                    next = 0
                elif last_level == "level 5":
                    game_state = "level 6"
                    next = 0
                elif last_level == "level 6":
                    game_state = "level 7"
                    next = 0
                elif last_level == "level 7":
                    game_state = "level 8"
                    next = 0
            elif again == 1:
                print(last_level)
                game_state = last_level
                again = 0
            elif leave == 1:
                game_state = "start_menu"
                leave = 0

    if game_state == "start_menu":
        draw_start_menu()
        start_button = Button()
        start_button.rect = start_button.surf.get_rect().move(100, 330)
        if start_button.rect.collidepoint(pygame.mouse.get_pos()):
            ready_to_start = 1
        else:
            ready_to_start = 0

    elif game_state == "game_over":
        draw_game_over_screen()

    elif game_state == "select_level":
        draw_level_selection()
        level_1_button = Button()
        level_1_button.surf = pygame.surface.Surface((100, 100))
        level_1_button.rect = level_1_button.surf.get_rect().move(50, 200)
        if level_1_button.rect.collidepoint(pygame.mouse.get_pos()):
            choosing_level_1 = 1
        else:
            choosing_level_1 = 0
        level_2_button = Button()
        level_2_button.surf = pygame.surface.Surface((100, 100))
        level_2_button.rect = level_2_button.surf.get_rect().move(250, 200)
        if level_2_button.rect.collidepoint(pygame.mouse.get_pos()):
            choosing_level_2 = 1
        else:
            choosing_level_2 = 0
        level_3_button = Button()
        level_3_button.surf = pygame.surface.Surface((100, 100))
        level_3_button.rect = level_3_button.surf.get_rect().move(450, 200)
        if level_3_button.rect.collidepoint(pygame.mouse.get_pos()):
            choosing_level_3 = 1
        else:
            choosing_level_3 = 0
        level_4_button = Button()
        level_4_button.surf = pygame.surface.Surface((100, 100))
        level_4_button.rect = level_4_button.surf.get_rect().move(650, 200)
        if level_4_button.rect.collidepoint(pygame.mouse.get_pos()):
            choosing_level_4 = 1
        else:
            choosing_level_4 = 0
        level_5_button = Button()
        level_5_button.surf = pygame.surface.Surface((100, 100))
        level_5_button.rect = level_5_button.surf.get_rect().move(50, 400)
        if level_5_button.rect.collidepoint(pygame.mouse.get_pos()):
            choosing_level_5 = 1
        else:
            choosing_level_5 = 0
        level_6_button = Button()
        level_6_button.surf = pygame.surface.Surface((100, 100))
        level_6_button.rect = level_6_button.surf.get_rect().move(250, 400)
        if level_6_button.rect.collidepoint(pygame.mouse.get_pos()):
            choosing_level_6 = 1
        else:
            choosing_level_6 = 0
        level_7_button = Button()
        level_7_button.surf = pygame.surface.Surface((100, 100))
        level_7_button.rect = level_7_button.surf.get_rect().move(450, 400)
        if level_7_button.rect.collidepoint(pygame.mouse.get_pos()):
            choosing_level_7 = 1
        else:
            choosing_level_7 = 0
        level_8_button = Button()
        level_8_button.surf = pygame.surface.Surface((100, 100))
        level_8_button.rect = level_8_button.surf.get_rect().move(650, 400)
        if level_8_button.rect.collidepoint(pygame.mouse.get_pos()):
            choosing_level_8 = 1
        else:
            choosing_level_8 = 0

    elif game_state == "level 1":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(background, (0, 0))
        if map_drawn == 0:
            level_1_map = [(200, 550), (250, 550), (300, 550), (450, 500), (500, 500), (550, 500), (700, 450),
                           (750, 450)]
            location = 0
            for i in range(len(level_1_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_1_map[location])
                level_1.add(new_platform)
                platforms.add(new_platform)
                location += 1
            door = Door()
            door.rect = door.surf.get_rect().move(750, 393)
            level_1.add(door)
            doors.add(door)
            map_drawn = 1

        for entity in all_sprites:
            Gravity(player, jumping_rn)
            screen.blit(entity.surf, entity.rect)
        for platform in level_1:
            screen.blit(platform.surf, platform.rect)

        pygame.display.flip()
        if jumping_rn > 0:
            jumping_rn -= 2
        clock.tick(fps)
    elif game_state == "level 2":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(background, (0, 0))
        if map_drawn == 0:
            level_2_map = [(250, 550), (300, 550), (350, 550), (450, 500), (500, 500), (600, 450), (650, 450),
                           (750, 450), (750, 400), (750, 350), (750, 300), (610, 320), (560, 320), (510, 320)]
            location = 0
            for i in range(len(level_2_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_2_map[location])
                level_2.add(new_platform)
                platforms.add(new_platform)
                location += 1
            door = Door()
            door.rect = door.surf.get_rect().move(530, 263)
            level_2.add(door)
            doors.add(door)
            map_drawn = 1

        for entity in all_sprites:
            Gravity(player, jumping_rn)
            screen.blit(entity.surf, entity.rect)
        for platform in level_2:
            screen.blit(platform.surf, platform.rect)

        pygame.display.flip()

        if jumping_rn > 0:
            jumping_rn -= 2
        clock.tick(fps)
    elif game_state == "level 3":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(background, (0, 0))
        if map_drawn == 0:
            level_3_map = [(200, 550), (250, 550), (350, 500), (400, 500), (450, 500), (550, 450), (600, 450),
                           (750, 450), (750, 400), (750, 350), (750, 300), (750, 250), (600, 300),
                           (550, 300), (450, 250), (400, 250), (350, 250), (250, 200), (200, 200), (100, 150),
                           (50, 150), (0, 150)]
            location = 0
            for i in range(len(level_3_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_3_map[location])
                level_3.add(new_platform)
                platforms.add(new_platform)
                location += 1
            door = Door()
            door.rect = door.surf.get_rect().move(80, 93)
            level_3.add(door)
            doors.add(door)
            map_drawn = 1

        for entity in all_sprites:
            Gravity(player, jumping_rn)
            screen.blit(entity.surf, entity.rect)
        for platform in level_3:
            screen.blit(platform.surf, platform.rect)

        pygame.display.flip()

        if jumping_rn > 0:
            jumping_rn -= 2
        clock.tick(fps)
    elif game_state == "level 4":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(background, (0, 0))
        if map_drawn == 0:
            level_4_map = [(250, 550), (300, 550), (350, 550), (500, 500), (550, 500), (600, 500), (750, 500),
                           (750, 250),
                           (750, 300), (750, 350), (750, 400), (750, 450), (600, 350), (550, 350), (450, 300),
                           (400, 300), (300, 250), (250, 250),
                           (100, 300), (100, 250), (100, 200), (100, 150), (100, 100), (100, 50), (100, 0), (250, 100),
                           (300, 100),
                           (350, 100), (400, 100), (450, 100), (500, 100), (550, 100), (600, 100), (650, 100),
                           (700, 100), (750, 100), (800, 100)]
            location = 0
            for i in range(len(level_4_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_4_map[location])
                level_4.add(new_platform)
                platforms.add(new_platform)
                location += 1
            door = Door()
            door.rect = door.surf.get_rect().move(750, 43)
            level_4.add(door)
            doors.add(door)
            map_drawn = 1

        for entity in all_sprites:
            Gravity(player, jumping_rn)
            screen.blit(entity.surf, entity.rect)
        for platform in level_4:
            screen.blit(platform.surf, platform.rect)

        pygame.display.flip()

        if jumping_rn > 0:
            jumping_rn -= 2
        clock.tick(fps)
    elif game_state == "level 5":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(background, (0, 0))
        if map_drawn == 0:
            level_5_map = [(250, 550), (300, 550), (350, 550), (400, 550), (500, 500), (550, 500), (600, 500),
                           (650, 500)]
            for i in range(len(level_5_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_5_map[i])
                level_5.add(new_platform)
                platforms.add(new_platform)
            door = Door()
            door.rect = door.surf.get_rect().move(620, 443)
            level_5.add(door)
            doors.add(door)
            all_spikes = [(330, 520)]
            for i in range(len(all_spikes)):
                new_spike = Spike()
                new_spike.rect = new_spike.surf.get_rect().move(all_spikes[i])
                spikes.add(new_spike)
                level_5.add(new_spike)
            map_drawn = 1

        for entity in all_sprites:
            Gravity(player, jumping_rn)
            screen.blit(entity.surf, entity.rect)
        for platform in level_5:
            screen.blit(platform.surf, platform.rect)

        pygame.display.flip()

        if jumping_rn > 0:
            jumping_rn -= 2
        clock.tick(fps)
    elif game_state == "level 6":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(background, (0, 0))
        if map_drawn == 0:
            level_6_map = [(300, 550), (350, 550), (400, 550), (500, 500), (550, 500), (600, 500), (650, 500),
                           (750, 450), (750, 400), (750, 350), (750, 300), (750, 250), (600, 350),
                           (550, 350), (450, 300), (400, 300), (300, 250), (250, 250), (150, 200), (100, 200),
                           (50, 200), (0, 200)]
            location = 0
            for i in range(len(level_6_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_6_map[location])
                level_6.add(new_platform)
                platforms.add(new_platform)
                location += 1
            door = Door()
            door.rect = door.surf.get_rect().move(60, 143)
            level_6.add(door)
            doors.add(door)
            all_spikes = [(420, 520), (400, 270)]
            for i in range(len(all_spikes)):
                new_spike = Spike()
                new_spike.rect = new_spike.surf.get_rect().move(all_spikes[i])
                spikes.add(new_spike)
                level_6.add(new_spike)
            new_spike = Spike()
            new_spike.surf = pygame.transform.rotate(new_spike.surf, 90)
            new_spike.rect = new_spike.surf.get_rect().move(720, 300)
            spikes.add(new_spike)
            level_6.add(new_spike)
            new_spike = Spike()
            new_spike.surf = pygame.transform.rotate(new_spike.surf, (-90))
            new_spike.rect = new_spike.surf.get_rect().move(200, 210)
            spikes.add(new_spike)
            level_6.add(new_spike)
            map_drawn = 1

        for entity in all_sprites:
            Gravity(player, jumping_rn)
            screen.blit(entity.surf, entity.rect)
        for platform in level_6:
            screen.blit(platform.surf, platform.rect)

        pygame.display.flip()

        if jumping_rn > 0:
            jumping_rn -= 2
        clock.tick(fps)
    elif game_state == "level 7":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(background, (0, 0))
        if map_drawn == 0:
            level_7_map = [(200, 550), (250, 550), (350, 500), (400, 500), (500, 450), (500, 400), (500, 350),
                           (500, 300), (350, 350), (300, 350), (200, 300), (150, 300), (50, 250), (0, 250), (200, 200),
                           (250, 200), (400, 150), (450, 150), (600, 100), (650, 100), (700, 100), (750, 100)]
            for i in range(len(level_7_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_7_map[i])
                level_7.add(new_platform)
                platforms.add(new_platform)
            door = Door()
            door.rect = door.surf.get_rect().move(710, 43)
            level_7.add(door)
            doors.add(door)
            all_spikes = [(370, 400), (170, 210), (370, 160), (570, 110)]
            for i in range(len(all_spikes)):
                new_spike = Spike()
                if i == 0:
                    new_spike.surf = pygame.transform.rotate(new_spike.surf, 180)
                else:
                    new_spike.surf = pygame.transform.rotate(new_spike.surf, 90)
                new_spike.rect = new_spike.surf.get_rect().move(all_spikes[i])
                spikes.add(new_spike)
                level_7.add(new_spike)
            map_drawn = 1

        for entity in all_sprites:
            Gravity(player, jumping_rn)
            screen.blit(entity.surf, entity.rect)
        for platform in level_7:
            screen.blit(platform.surf, platform.rect)

        pygame.display.flip()

        if jumping_rn > 0:
            jumping_rn -= 2
        clock.tick(fps)
    elif game_state == "level 8":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(background, (0, 0))
        if map_drawn == 0:
            level_8_map = [(250, 550), (300, 550), (450, 500), (500, 500), (600, 450), (600, 400), (600, 350),
                           (600, 300), (450, 350), (400, 350), (300, 350), (250, 350), (150, 350), (100, 350), (0, 300),
                           (0, 250), (0, 200), (0, 150), (150, 200), (200, 200), (300, 200), (400, 200), (450, 200),
                           (550, 200), (650, 200), (700, 200), (750, 200)]
            for i in range(len(level_8_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_8_map[i])
                level_8.add(new_platform)
                platforms.add(new_platform)
            door = Door()
            door.rect = door.surf.get_rect().move(720, 143)
            level_8.add(door)
            doors.add(door)
            all_spikes = [(310, 170), (560, 170), (150, 250), (460, 250), (460, 400)]
            for i in range(len(all_spikes)):
                new_spike = Spike()
                if i > 1:
                    new_spike.surf = pygame.transform.rotate(new_spike.surf, 180)
                new_spike.rect = new_spike.surf.get_rect().move(all_spikes[i])
                spikes.add(new_spike)
                level_8.add(new_spike)
            map_drawn = 1

        for entity in all_sprites:
            Gravity(player, jumping_rn)
            screen.blit(entity.surf, entity.rect)
        for platform in level_8:
            screen.blit(platform.surf, platform.rect)

        pygame.display.flip()

        if jumping_rn > 0:
            jumping_rn -= 2
        clock.tick(fps)
