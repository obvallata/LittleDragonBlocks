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

    def refresh_score(self, game_info, x_coor=500, y_coor=600):
        font = pygame.font.Font(pygame.font.match_font('optima'), 32)
        score_surface = font.render("Score: " + str(game_info.points), False, (0, 0, 0))
        score_rect = score_surface.get_rect()
        score_rect.center = (x_coor, y_coor)
        self.screen.blit(score_surface, score_rect)

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

    def refresh_time(self, time, limit=10):
        font = pygame.font.Font(pygame.font.match_font('optima'), 28)
        text_surface_limit = font.render("Time limit: " + str(limit) + " sec", False, (0, 0, 0))
        text_surface = font.render(str(time), False, (0, 0, 0))
        text_limit_rect = text_surface_limit.get_rect()
        text_rect = text_surface.get_rect()
        text_rect.center = (400, 100)
        text_limit_rect.center = (400, 50)
        self.screen.blit(text_surface, text_rect)
        self.screen.blit(text_surface_limit, text_limit_rect)

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
        points_coeff = 1
        start_ticks = pygame.time.get_ticks()
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
        seconds = 0
        while running:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    next_run = False
            all_sprites.update(game_info, dragon_field, game_info.CELL_SIZE * game_info.AMOUNT_OF_CELLS)
            self.screen.fill((255, 204, 255))
            self.refresh_time(round(seconds, 1), game_info.TIME_LIMITS[lvl.num])
            self.refresh_text(game_info, lvl.num)
            self.refresh_score(game_info)
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
        return next_run, points_coeff - (seconds - game_info.TIME_LIMITS[lvl.num])

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
            self.refresh_score(game_info, 500, 600)
            start_button.update()
            quit_button.update()
            if start_button.counter >= 1:
                game_info.points = 0
                running = False
                next_run = True
            if quit_button.counter >= 1:
                running = False
            pygame.display.flip()
            self.clock.tick(game_info.FPS)
        return next_run