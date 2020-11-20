import pygame

size = width, height = 301, 301
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    #...

    # обновление экрана
    pygame.display.flip()

pygame.quit()