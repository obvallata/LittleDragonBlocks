from dragon import Dragon


class Border(Dragon):
    def __init__(self, name, height, width, form):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        Dragon.__init__(self, name, height, width, form)
