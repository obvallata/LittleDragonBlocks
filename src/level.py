class Level:
    def __init__(self):
        self.num = 0
        self.field_top = 0
        self.field_left = 0
        self.amount_of_dragons = 0
        self.amount_of_borders = 0
        self.dragon_sizes = []
        self.info_amount_lines = 0
        self.shapes = []
        self.images = []
        self.borders_places = []

    def set_num(self, num):
        self.num = num

    def run_lvl(self, interface, game_info):
        return interface.create(game_info, self, True)

    def __call__(self, interface, game_info, running):
        self.field_top = game_info.get_field_top(self.num)
        self.field_left = game_info.get_field_left(self.num)
        self.amount_of_dragons = game_info.get_amount_of_dragons(self.num)
        self.amount_of_borders = game_info.get_amount_of_borders(self.num)
        self.dragon_sizes = game_info.get_dragon_sizes(self.num)
        self.info_amount_lines = game_info.get_amount_of_lines(self.num)
        self.shapes = game_info.get_shapes(self.num)
        self.images = game_info.get_image(self.num)
        self.borders_places = game_info.get_border_places(self.num)
        if running:
            return self.run_lvl(interface, game_info)
        return False
