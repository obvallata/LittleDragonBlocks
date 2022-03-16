import pygame
from field import Field


# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
screen.fill((255, 204, 255))
x_pos = 0
v = 20  # пикселей в секунду clock = pygame.time.Clock()
fps = 60
clock = pygame.time.Clock()
dragon_field = Field(4, 4)
dragon_field.set_view(200, 200, 95)
# Да, этот импорт должен быть тут! Да, костыль! Да, потом исправим!
from dragon import Dragon
all_sprites = pygame.sprite.Group()
player = Dragon()
all_sprites.add(player)


running = True
while running:
    # ТУТ МБ ВМЕСТО get wait!!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dragon_field.render(screen)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()


