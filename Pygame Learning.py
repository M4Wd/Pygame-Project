import pygame
import os
import sys

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)

pygame.init()

clock = pygame.time.Clock
game_state = "start_menu"


class Button(pygame.sprite.Sprite):
    def __init__(self):
        super(Button, self).__init__()
        self.surf = pygame.Surface((100, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect().move(100, 200)


def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button_font = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, 50))
    screen.blit(start_button_font, (100, 200))
    pygame.display.update()

def draw_help_menu():
    screen.fill(0, 0)

def draw_game_over_screen():
    global next, again, leave, map_drawn
    for platform in platforms:
        platform.kill()
    for door in doors:
        door.kill()
    for spike in spikes:
        spike.kill()
    map_drawn = 0
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
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
    pygame.display.update()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


def Gravity(Character, inverted=0):
    global touching_left, touching_right, jumping_left, jumping_right, jumping_rn, falling, can_jump_right, can_jump_left
    if touching_right == 1 or touching_left == 1:
        if touching_right == 1:
            can_jump_left = 1
        elif touching_left == 1:
            can_jump_right = 1
        falling = 1
    else:
        falling = 5
        can_jump_right = 0
        can_jump_left = 0
    if Character.rect.bottom < SCREEN_HEIGHT and inverted == 0 and jumping_left == 0 and jumping_right == 0:
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
        self.surf = pygame.Surface((20, 50))
        self.surf.fill((255, 255, 255))
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
        self.surf = pygame.image.load("data/idle.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = pygame.rect.Rect(0, 0, 30, 45)
        self.rect = self.rect.move(30, 500)

    def update(self, pressed_keys):
        global touching_left, touching_right, standing, jumping_right, jumping_left, game_state, map_drawn, last_level
        if touching_right == 0 and touching_left == 0 or self.rect.bottom == SCREEN_HEIGHT:
            if jumping_right == 0 and jumping_left == 0:
                if pressed_keys[pygame.key.key_code("a")]:
                    x = self.rect.x
                    y = self.rect.y
                    self.rect.move_ip(-5, 0)
                    for platform in platforms:
                        if pygame.sprite.collide_rect(self, platform):
                            self.rect.x = x
                            self.rect.y = y
                if pressed_keys[pygame.key.key_code("d")]:
                    x = self.rect.x
                    y = self.rect.y
                    self.rect.move_ip(5, 0)
                    for platform in platforms:
                        if pygame.sprite.collide_rect(self, platform):
                            self.rect.x = x
                            self.rect.y = y
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
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect().move(300, 500)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

running = True
ready_to_start = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == pygame.key.key_code("space"):
                if player.rect.bottom == SCREEN_HEIGHT or standing == 1 or touching_right == 1 or touching_left == 1:
                    if can_jump_right == 1:
                        jumping_right = 15
                    elif can_jump_left == 1:
                        jumping_left = 15
                    else:
                        jumping_rn = 40
            if event.key == pygame.key.key_code("p"):
                last_level = game_state
                game_state = "game_over"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ready_to_start == 1:
                game_state = "level 1"
                ready_to_start = 0
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
        if start_button.rect.collidepoint(pygame.mouse.get_pos()):
            ready_to_start = 1
        else:
            ready_to_start = 0

    if game_state == "game_over":
        draw_game_over_screen()

    if game_state == "level 1":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((186, 140, 99))
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
            door.rect = door.surf.get_rect().move(750, 400)
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
    if game_state == "level 2":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((186, 140, 99))
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
            door.rect = door.surf.get_rect().move(530, 270)
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
        print(player.rect.left, player.rect.right)
    if game_state == "level 3":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((186, 140, 99))
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
            door.rect = door.surf.get_rect().move(80, 100)
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
    if game_state == "level 4":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((186, 140, 99))
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
            door.rect = door.surf.get_rect().move(750, 50)
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
    if game_state == "level 5":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((186, 140, 99))
        if map_drawn == 0:
            level_5_map = [(250, 550), (300, 550), (350, 550), (400, 550), (500, 500), (550, 500), (600, 500),
                           (650, 500)]
            for i in range(len(level_5_map)):
                new_platform = Platform()
                new_platform.rect = new_platform.surf.get_rect().move(level_5_map[i])
                level_5.add(new_platform)
                platforms.add(new_platform)
            door = Door()
            door.rect = door.surf.get_rect().move(620, 450)
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
    if game_state == "level 6":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((186, 140, 99))
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
            door.rect = door.surf.get_rect().move(60, 150)
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
    if game_state == "level 7":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((186, 140, 99))
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
            door.rect = door.surf.get_rect().move(710, 50)
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
    if game_state == "level 8":
        clock = pygame.time.Clock()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((186, 140, 99))
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
            door.rect = door.surf.get_rect().move(720, 150)
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
