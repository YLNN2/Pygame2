import pygame

size = width, height = 300, 300
screen = pygame.display.set_mode(size)

running = True

while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    events = pygame.event.get()
    for event in events:

        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    # ...

    # обновление экрана
    pygame.display.flip()

pygame.quit()