import pygame
from src.common_data import LVL_INFO_FOR_USER
from src.field import Field
from src.dragon import Dragon
from src.border import Border
from src.button import Button


class Interface:
    def __init__(self):
        self.screen = None
        self.clock = None

    def set_screen(self, screen):
        self.screen = screen

    def set_clock(self, clock):
        self.clock = clock

    def refresh_menu(self, game_info):
        self.screen.fill((130, 130, 255))
        font = pygame.font.Font(pygame.font.match_font('optima'), 48)
        text_surface = font.render('Little Dragon Blocks', False, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (game_info.WIDTH / 2, 100)
        self.screen.blit(text_surface, text_rect)

    def refresh_text(self, game_info, lvl_num):
        font = pygame.font.Font(pygame.font.match_font('optima'), 28)
        for i in range(game_info.INFO_AMOUNT_LINES[lvl_num]):
            text_surface = font.render(LVL_INFO_FOR_USER[lvl_num][i], False, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.center = (100, 50 * (i + 1))
            self.screen.blit(text_surface, text_rect)

    def render(self, field):
        y_pos = field.top
        for i in range(field.height):
            x_pos = field.left
            for j in range(field.width):
                pygame.draw.rect(self.screen, (255, 255, 153), pygame.Rect(x_pos, y_pos, field.cell_size, field.cell_size))
                pygame.draw.rect(self.screen, (0, 204, 0), pygame.Rect(x_pos, y_pos, field.cell_size, field.cell_size), 2)
                x_pos += field.cell_size
            y_pos += field.cell_size
        pygame.draw.rect(self.screen, (0, 204, 0), pygame.Rect(field.left, field.top, field.cell_size * field.height,
                                                          field.cell_size * field.width), 4)

    def create(self, game_info, lvl, running):
        dragon_field = Field(game_info)
        dragon_field.set_view(lvl.field_left, lvl.field_top)
        all_sprites = pygame.sprite.Group()
        borders = pygame.sprite.Group()
        dragons_status = []
        for i in range(lvl.amount_of_dragons):
            dragons_status.append(Dragon(game_info, lvl.num, lvl.shapes[i], i + 1,
                                         lvl.dragon_sizes[i][0] * game_info.CELL_SIZE,
                                         lvl.dragon_sizes[i][1] * game_info.CELL_SIZE))
            all_sprites.add(dragons_status[i])
        for i in range(lvl.amount_of_borders):
            borders.add(Border(game_info, lvl.borders_places, i))
        dragon_field.set_borders(game_info, lvl.borders_places)
        next_run = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    next_run = False
            all_sprites.update(game_info, dragon_field, game_info.CELL_SIZE * game_info.AMOUNT_OF_CELLS)
            self.screen.fill((255, 204, 255))
            self.refresh_text(game_info, lvl.num)
            self.render(dragon_field)
            all_sprites.draw(self.screen)
            borders.draw(self.screen)
            can_we_go_next_lvl = True
            for i in range(lvl.amount_of_dragons):
                if not dragons_status[i].ready:
                    can_we_go_next_lvl = False
                    break
            if can_we_go_next_lvl:
                next_run = True
                running = False
            pygame.display.flip()
            self.clock.tick(game_info.FPS)
        return next_run

    def menu_run(self, game_info, running):
        start_button = Button(self.screen, game_info.WIDTH / 2 - 160, game_info.HEIGHT / 2 - 100, 300, 100,
                              "START", 32, 85, 27)
        quit_button = Button(self.screen, game_info.WIDTH / 2 - 160, game_info.HEIGHT / 2, 300, 100, "EXIT", 32,
                             85, 27)
        start_button.draw()
        next_run = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.refresh_menu(game_info)
            start_button.update()
            quit_button.update()
            if start_button.counter >= 1:
                running = False
                next_run = True
            if quit_button.counter >= 1:
                running = False
            pygame.display.flip()
            self.clock.tick(game_info.FPS)
        return next_run

