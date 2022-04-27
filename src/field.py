class Field:
    def __init__(self, game_info, width=-1, height=-1):
        width = max(width, game_info.AMOUNT_OF_CELLS)
        height = max(height, game_info.AMOUNT_OF_CELLS)
        self.width = width
        self.height = height
        self.field = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = game_info.CELL_SIZE

    def set_view(self, left, top):
        self.left = left
        self.top = top

    def get_cell_pos(self, cell_number):
        return [self.cell_size[0] * cell_number, self.cell_size[1] * cell_number]

    def set_borders(self, game_info, positions):
        for i in range(game_info.AMOUNT_OF_CELLS):
            for j in range(game_info.AMOUNT_OF_CELLS):
                if positions[i][j] == 1:
                    self.field[i][j] = 2
