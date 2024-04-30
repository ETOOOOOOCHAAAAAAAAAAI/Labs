import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
white = (255, 255, 255)
red = (255, 0, 0)
x, y = 300, 300
radius = 25
velocity = 20
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x > 0:
                x -= velocity
            elif event.key == pygame.K_RIGHT and x < 50:
                x += velocity
            elif event.key == pygame.K_UP and y > 0:
                y -= velocity
            elif event.key == pygame.K_DOWN:
                y += velocity
    screen.fill(white)
    pygame.draw.circle(screen, red, (x,y), radius)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()