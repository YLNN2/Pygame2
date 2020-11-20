import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

def draw():
    pass



while pygame.event.wait().type != pygame.QUIT:
    draw()
    pygame.display.flip()

pygame.quit()

