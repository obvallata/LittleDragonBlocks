import pygame
from field import Field


# инициализация Pygame:
pygame.init()
# размеры окна:
WIDTH = 1024
HEIGHT = 768
FPS = 60
AMOUNT_OF_CELLS = 4
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
# x_pos = 0
# v = 20
# пикселей в секунду clock = pygame.time.Clock()
clock = pygame.time.Clock()
# Дальше клетчатое поле
dragon_field = Field(AMOUNT_OF_CELLS, AMOUNT_OF_CELLS)
dragon_field.set_view(200, 200, 95)
# Да, этот импорт должен быть тут! Да, костыль! Да, потом исправим!
# Драконы в общем
from dragon import Dragon
all_sprites = pygame.sprite.Group()
dragon_one = Dragon('img_1.png', dragon_field.cell_size, dragon_field.cell_size)
all_sprites.add(dragon_one)


running = True
while running:
    # ТУТ МБ ВМЕСТО get wait!!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Poped', event.button)
        elif event.type == pygame.MOUSEMOTION:
            print("Move", event.pos)

    all_sprites.update()

    screen.fill((255, 204, 255))
    dragon_field.render(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


