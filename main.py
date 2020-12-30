import pygame
import sys
import text

blue = (0, 255, 255)
WIDTH = 360  # ширина игрового окна
HEIGHT = 480  # высота игрового окна

# создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
img = pygame.image.load('tic-tac-toe.jpg')
pygame.display.set_icon(img)

# цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.fill(blue)
    pygame.display.flip()

    name = text.ask(screen, 'Введите имя')
    num_strok = int(text.ask(screen, 'Укажите количество строк'))
    num_stolbets = int(text.ask(screen, 'Укажите количество столбцов'))
    count_pobeda = int(text.ask(screen, 'Кол-во символов для победы'))
    break


def check_win(mas, sign):
    # проверка по столбцу
    for col in range(num_stolbets):
        count_symbol = 0
        for row in range(num_strok):
            if mas[row][col] == sign:
                count_symbol += 1
                if count_symbol == count_pobeda:
                    return sign
            else:
                count_symbol = 0

    # проверка по строке
    for row in range(num_strok):
        count_symbol = 0
        for col in range(num_stolbets):
            if mas[row][col] == sign:
                count_symbol += 1
                if count_symbol == count_pobeda:
                    return sign
            else:
                count_symbol = 0

    # главная диагональ
    for line in range(num_strok - count_pobeda + 1):
        for k in range(num_stolbets - count_pobeda + 1):
            count_symbol1 = 0
            count_symbol2 = 0
            for row in range(num_strok - line):
                if row + k == num_stolbets:
                    break
                else:
                    if mas[line + row][row + k] == sign:
                        count_symbol1 += 1
                        if count_symbol1 == count_pobeda:
                            return sign
                    else:
                        count_symbol1 = 0
                    # побочная диагональ
                    if mas[line + row][num_stolbets - row - k - 1] == sign:
                        count_symbol2 += 1
                        if count_symbol2 == count_pobeda:
                            return sign
                    else:
                        count_symbol2 = 0
    return False


pygame.init()

size_block = 100
otstup = 5
width = size_block * num_stolbets + otstup * num_stolbets + 1
height = size_block * num_strok + otstup * num_strok + 1

size_window = (width, height)
screen = pygame.display.set_mode(size_window)

pygame.display.set_caption('Крестики-нолики')
img = pygame.image.load('tic-tac-toe.jpg')
pygame.display.set_icon(img)

black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * num_stolbets for i in range(num_strok)]
query = 0
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (otstup + size_block)
            row = y_mouse // (otstup + size_block)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * num_stolbets for i in range(num_strok)]
            query = 0
            screen.fill(black)

    if not game_over:
        for row in range(num_strok):
            for col in range(num_stolbets):
                if mas[row][col] == 'x':
                    color = blue
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * otstup
                y = row * size_block + (row + 1) * otstup
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == blue:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       3)
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('stxingkai', 80)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()
