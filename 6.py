import pygame

size = width, height = 301, 301
screen = pygame.display.set_mode(size)

MYEVENTTYPE = 30

pygame.time.set_timer(MYEVENTTYPE, 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MYEVENTTYPE:
            print("Мое событие сработало")

    pygame.display.flip()


pygame.quit()