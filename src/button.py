import pygame


class Button:
    def __init__(self, surf, x, y, width, height, text, text_size, sp_x, sp_y):
        self.x = x
        self.y = y
        self.surf = surf
        self.width = width
        self.height = height
        self.counter = 0
        self.text = text
        self.text_size = text_size
        self.sp_x = sp_x
        self.sp_y = sp_y

    def draw(self, colour1=(250, 128, 114), colour2=(205, 92, 92)):
        pygame.draw.rect(self.surf, colour1, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.surf, colour2, (self.x, self.y, self.width, self.height), 10)
        font = pygame.font.Font(pygame.font.match_font('optima'), self.text_size)
        text_surface = font.render(self.text, False, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.left = self.x + self.sp_x
        text_rect.top = self.y + self.sp_y
        self.surf.blit(text_surface, text_rect)

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            self.draw((0, 255, 0), (50, 205, 50))
            if click[0] == 1:
                self.counter += 1
            else:
                self.draw((250, 128, 114), (220, 20, 60))

        else:
            self.draw()
