import sys
from arena import Arena
from characters import Mando
from utils import NBInput
import time


class Engine:
    """Generating the backend of the game
    Each game will be an instance of the Engine
    """

    def __init__(self):
        self.arena = Arena()
        self.player = Mando(self.arena.board)
        self.score = 0

    def transition(self, key):
        self.player.check_proximity(self.arena.board)
        status = self.player.move(self.arena.board, key)
        if status == -1:
            return -1
        else:
            self.score += status
            return 0

    def repaint(self):
        sys.stdout.flush()
        sys.stdout.write("\x1bc")
        self.arena.render()
        sys.stdout.write(f"Score: {self.score}\n")

    def game_over(self):
        # sys.stdout.write("\x1bc")
        print("GAME OVER!!")
        print(f"Final Score: {self.score}")

    def play(self):
        KEYS = NBInput()
        KEYS.nb_term()
        while True:
            self.repaint()
            INPUT = ""
            if KEYS.kb_hit():
                INPUT = KEYS.get_ch()
            status = self.transition(INPUT)
            if status == -1:
                self.game_over()
                break
            KEYS.flush()
            time.sleep(0.07)
