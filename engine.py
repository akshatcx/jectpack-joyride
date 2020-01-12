from arena import Arena
from characters import Mando
from utils import NBInput, clear
import time

class Engine:
    '''Generating the backend of the game
    Each game will be an instance of the Engine
    '''

    def __init__(self):
        self.arena = Arena()
        self.player = Mando()
        self.player.init_location(self.arena.board)
        
    def transition(self, key):
        self.player.check_proximity(self.arena.board)
        self.player.move(self.arena.board, key)

    def repaint(self):
        clear()
        self.arena.render()
    
    def play(self):
        KEYS = NBInput()
        KEYS.nb_term()
        clear()
        while True:
            self.repaint()
            INPUT = ''
            if KEYS.kb_hit():
                INPUT = KEYS.get_ch()
            self.transition(INPUT)
            KEYS.flush()
            time.sleep(0.1)
