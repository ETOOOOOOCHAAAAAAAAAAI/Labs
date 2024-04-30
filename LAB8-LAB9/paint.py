import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Paint")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Настройка фона
screen.fill(WHITE)

# Переменные инструментов
current_tool = 'pencil'
current_color = BLACK
drawing = False
start_pos = (0, 0)
last_pos = (0, 0)  # Для инструмента "карандаш"

# Цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатий мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if current_tool == 'rectangle':
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                rect.normalize()
                pygame.draw.rect(screen, current_color, rect)
            elif current_tool == 'circle':
                radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.circle(screen, current_color, start_pos, radius)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if current_tool == 'pencil':
                pygame.draw.line(screen, current_color, last_pos, event.pos, 1)
                last_pos = event.pos
            elif current_tool in ['rectangle', 'circle']:  # Обновлять превью рисунка, если требуется
                last_pos = event.pos

        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_tool = 'rectangle'      #рисовка прямоугольника на кнопку r
            elif event.key == pygame.K_c:
                current_tool = 'circle'     #рисовка круга на кнопку c
            elif event.key == pygame.K_p:
                current_tool = 'pencil'     #переход на карандаш на кнопку p
            elif event.key == pygame.K_e:
                current_color = WHITE  # Использовать белый цвет для стирания
            # измена цветов карандаша
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE

    # Обновление экрана
    pygame.display.flip()

# Закрытие Pygame
pygame.quit()
sys.exit()
