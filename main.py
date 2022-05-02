from src.game import Game
from src.interface import Interface


if __name__ == "__main__":
    interface = Interface()
    game = Game(interface)
    game.start()
