from arena import Arena
from characters import Mando

class Engine:
    '''Generating the backend of the game
    Each game will be an instance of the Engine
    '''

    def __init__(self):
        self.arena = Arena(self)
        self.player = Mando(self)
