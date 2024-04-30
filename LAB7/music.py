import pygame

# Инициализируем Pygame и модуль mixer
pygame.init()
pygame.mixer.init()

# Загрузка треков
tracks = [
    'C:/Users/ASUS TUF Gaming F15/Downloads/Fabrizio_Paterlini_-_Snow_(musmore.com) (7).mp3',
    'C:/Users/ASUS TUF Gaming F15/Downloads/lab 7_music_Peter_Sandberg_-_Dismantle_(musmore.com).mp3',
    'C:/Users/ASUS TUF Gaming F15/Downloads/Lindsey_Stirling_-_Heist_(musmore.com).mp3'
]
current_track = 0

# Функция для воспроизведения текущего трека
def play_track():
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.play()

# Создаем окно программы
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Music Player')

# Главный цикл программы
running = True
play_track()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Воспроизведение или пауза музыки
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                # Следующий трек
                current_track = (current_track + 1) % len(tracks)
                play_track()
            elif event.key == pygame.K_LEFT:
                # Предыдущий трек
                current_track = (current_track - 1) % len(tracks)
                play_track()


    # Здесь может быть код для отрисовки интерфейса или других элементов
    # ...

    pygame.display.flip()

pygame.quit()
