import pygame
import random

if __name__ == '__main__':
    f = open("Результаты.txt", mode="a")
    pygame.init()
    pygame.display.set_caption('Тренажёр клавиатуры')
    size = width, height = 600, 470
    screen = pygame.display.set_mode(size)

    running = True
    y_pos = 0
    v = 20
    clock = pygame.time.Clock()
    possible_coords = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 50, 100, 150, 200, 250, 300, 350, 400,
                       450, 500, 550]
    x_pos = random.choice(possible_coords)
    pygame.font.init()
    my_font = pygame.font.SysFont('Roboto', 40, False)
    top_row = ["й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ"]
    middle_row = ["ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э"]
    bottom_row = ["я", "ч", "с", "м", "и", "т", "ь", "б", "ю"]
    current_letter = "1"
    points = 0
    lives = 3


    def change_letter():
        global current_letter, x_pos, y_pos, v
        y_pos = 0
        x_pos = random.choice(possible_coords)
        if points <= 50:
            v += 1
        elif 50 <= points <= 100:
            v += 2
        elif 100 <= points <= 150:
            v += 3
        elif 150 <= points:
            v += 5
        if x_pos == 25:
            current_letter = "й"
        elif x_pos == 75:
            current_letter = random.choice(("ц", "я"))
        elif x_pos == 125:
            current_letter = random.choice(("у", "ч"))
        elif x_pos == 175:
            current_letter = random.choice(("к", "с"))
        elif x_pos == 225:
            current_letter = random.choice(("е", "м"))
        elif x_pos == 275:
            current_letter = random.choice(("н", "и"))
        elif x_pos == 325:
            current_letter = random.choice(("г", "т"))
        elif x_pos == 375:
            current_letter = random.choice(("ш", "ь"))
        elif x_pos == 425:
            current_letter = random.choice(("щ", "б"))
        elif x_pos == 475:
            current_letter = random.choice(("з", "ю"))
        elif x_pos == 525:
            current_letter = "х"
        elif x_pos == 575:
            current_letter = "ъ"
        elif x_pos == 50:
            current_letter = "ф"
        elif x_pos == 100:
            current_letter = "ы"
        elif x_pos == 150:
            current_letter = "в"
        elif x_pos == 200:
            current_letter = "а"
        elif x_pos == 250:
            current_letter = "п"
        elif x_pos == 300:
            current_letter = "р"
        elif x_pos == 350:
            current_letter = "о"
        elif x_pos == 400:
            current_letter = "л"
        elif x_pos == 450:
            current_letter = "д"
        elif x_pos == 500:
            current_letter = "ж"
        elif x_pos == 550:
            current_letter = "э"


    change_letter()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if current_letter == "й" and event.key == pygame.key.key_code("Q"):
                    change_letter()
                    points += 1
                elif current_letter == "ц" and event.key == pygame.key.key_code("W"):
                    change_letter()
                    points += 1
                elif current_letter == "у" and event.key == pygame.key.key_code("E"):
                    change_letter()
                    points += 1
                elif current_letter == "к" and event.key == pygame.key.key_code("R"):
                    change_letter()
                    points += 1
                elif current_letter == "е" and event.key == pygame.key.key_code("T"):
                    change_letter()
                    points += 1
                elif current_letter == "н" and event.key == pygame.key.key_code("Y"):
                    change_letter()
                    points += 1
                elif current_letter == "г" and event.key == pygame.key.key_code("U"):
                    change_letter()
                    points += 1
                elif current_letter == "ш" and event.key == pygame.key.key_code("I"):
                    change_letter()
                    points += 1
                elif current_letter == "щ" and event.key == pygame.key.key_code("O"):
                    change_letter()
                    points += 1
                elif current_letter == "з" and event.key == pygame.key.key_code("P"):
                    change_letter()
                    points += 1
                elif current_letter == "х" and event.key == pygame.key.key_code("["):
                    change_letter()
                    points += 1
                elif current_letter == "ъ" and event.key == pygame.key.key_code("]"):
                    change_letter()
                    points += 1
                elif current_letter == "ф" and event.key == pygame.key.key_code("A"):
                    change_letter()
                    points += 1
                elif current_letter == "ы" and event.key == pygame.key.key_code("S"):
                    change_letter()
                    points += 1
                elif current_letter == "в" and event.key == pygame.key.key_code("D"):
                    change_letter()
                    points += 1
                elif current_letter == "а" and event.key == pygame.key.key_code("F"):
                    change_letter()
                    points += 1
                elif current_letter == "п" and event.key == pygame.key.key_code("G"):
                    change_letter()
                    points += 1
                elif current_letter == "р" and event.key == pygame.key.key_code("H"):
                    change_letter()
                    points += 1
                elif current_letter == "о" and event.key == pygame.key.key_code("J"):
                    change_letter()
                    points += 1
                elif current_letter == "л" and event.key == pygame.key.key_code("K"):
                    change_letter()
                    points += 1
                elif current_letter == "д" and event.key == pygame.key.key_code("L"):
                    change_letter()
                    points += 1
                elif current_letter == "ж" and event.key == pygame.key.key_code(";"):
                    change_letter()
                    points += 1
                elif current_letter == "э" and event.key == pygame.key.key_code("'"):
                    change_letter()
                    points += 1
                elif current_letter == "я" and event.key == pygame.key.key_code("Z"):
                    change_letter()
                    points += 1
                elif current_letter == "ч" and event.key == pygame.key.key_code("X"):
                    change_letter()
                    points += 1
                elif current_letter == "с" and event.key == pygame.key.key_code("C"):
                    change_letter()
                    points += 1
                elif current_letter == "м" and event.key == pygame.key.key_code("V"):
                    change_letter()
                    points += 1
                elif current_letter == "и" and event.key == pygame.key.key_code("B"):
                    change_letter()
                    points += 1
                elif current_letter == "т" and event.key == pygame.key.key_code("N"):
                    change_letter()
                    points += 1
                elif current_letter == "ь" and event.key == pygame.key.key_code("M"):
                    change_letter()
                    points += 1
                elif current_letter == "б" and event.key == pygame.key.key_code(","):
                    change_letter()
                    points += 1
                elif current_letter == "ю" and event.key == pygame.key.key_code("."):
                    change_letter()
                    points += 1
        if lives == 0:
            running = False
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (100, 100, 100), (0, 290, width, height))
        for i in range(12):
            if current_letter == top_row[i]:
                pygame.draw.rect(screen, (255, 255, 255), (50 * i, 300, 50, 50))
                pygame.draw.rect(screen, (0, 0, 0), (50 * i, 300, 50, 50), 2)
                text_surface = my_font.render(top_row[i], False, (0, 0, 0))
                screen.blit(text_surface, (17 + 50 * i, 310))
            else:
                pygame.draw.rect(screen, (200, 200, 200), (50 * i, 300, 50, 50))
                pygame.draw.rect(screen, (0, 0, 0), (50 * i, 300, 50, 50), 2)
                text_surface = my_font.render(top_row[i], False, (0, 0, 0))
                screen.blit(text_surface, (17 + 50 * i, 310))
        for i in range(11):
            if current_letter == middle_row[i]:
                pygame.draw.rect(screen, (255, 255, 255), (25 + 50 * i, 355, 50, 50))
                pygame.draw.rect(screen, (0, 0, 0), (25 + 50 * i, 355, 50, 50), 2)
                text_surface = my_font.render(middle_row[i], False, (0, 0, 0))
                screen.blit(text_surface, (42 + 50 * i, 365))
            else:
                pygame.draw.rect(screen, (200, 200, 200), (25 + 50 * i, 355, 50, 50))
                pygame.draw.rect(screen, (0, 0, 0), (25 + 50 * i, 355, 50, 50), 2)
                text_surface = my_font.render(middle_row[i], False, (0, 0, 0))
                screen.blit(text_surface, (42 + 50 * i, 365))
        for i in range(9):
            if current_letter == bottom_row[i]:
                pygame.draw.rect(screen, (255, 255, 255), (50 + 50 * i, 410, 50, 50))
                pygame.draw.rect(screen, (0, 0, 0), (50 + 50 * i, 410, 50, 50), 2)
                text_surface = my_font.render(bottom_row[i], False, (0, 0, 0))
                screen.blit(text_surface, (67 + 50 * i, 420))
            else:
                pygame.draw.rect(screen, (200, 200, 200), (50 + 50 * i, 410, 50, 50))
                pygame.draw.rect(screen, (0, 0, 0), (50 + 50 * i, 410, 50, 50), 2)
                text_surface = my_font.render(bottom_row[i], False, (0, 0, 0))
                screen.blit(text_surface, (67 + 50 * i, 420))
        pygame.draw.circle(screen, "yellow", (x_pos, int(y_pos)), 20, 2)
        text_surface = my_font.render(current_letter, False, "yellow")
        screen.blit(text_surface, (x_pos - 10, y_pos - 15))
        text_surface1 = my_font.render(f"Очки: {points}", False, "red")
        screen.blit(text_surface1, (450, 0))
        text_surface2 = my_font.render(f"Жизни: {lives}", False, "red")
        screen.blit(text_surface2, (0, 0))
        y_pos += v * clock.tick() / 1000  # v * t в секундах
        if y_pos >= 270:
            change_letter()
            lives -= 1
        pygame.display.flip()
    f.write(f"Новая попытка. Очки - {points} \n")
