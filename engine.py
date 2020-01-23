import sys
from arena import Arena
from characters import Mando, Enemy
from utils import NBInput
import os
import time
from config import *


class Engine:
    """Generating the backend of the game
    Each game will be an instance of the Engine
    """

    def __init__(self):
        self.__arena = Arena()
        self.__player = Mando(self.__arena.board)
        self.__enemy = Enemy(self.__arena.board)
        self.__score = 0
        self.__start = time.time()
        self.__frame = 0
        self.__framerate = 2

    def transition(self, key):
        status = 0
        self.__framerate = self.__player.frate()
        if self.__frame < WIDTH - ENEMY_OFFSET:
            for i in range(self.__framerate):
                self.__frame += 1
                status += self.__player.move_relative(self.__arena.board, self.__frame)
        self.__player.checkmag(self.__arena.board, self.__frame)
        status += self.__player.move(self.__arena.board, key, self.__frame)
        self.__player.upd_att(self.__arena.board, key, self.__frame)
        self.__enemy.move(self.__arena.board, self.__player.location)
        if int(time.time() - self.__start) % 3 == 0:
            self.__enemy.shoot(self.__arena.board)
        self.__enemy.move_ice(self.__arena.board)
        self.__score += status
        if self.__score > 10:
            self.__player.activate_dragon()
        self.__player.render_tail(self.__arena.board)

    def repaint(self):
        # sys.stdout.flush()
        # sys.stdout.write("\x1bc")
        print("\x1bc")
        self.__arena.render(self.__frame, self.__enemy.location)
        print(
            f"Score: {self.__score}\t Lives: {self.__player.lives}\t Time Left: {int(GAME_TIME - (time.time() - self.__start))}secs\t Enemy Lives: {self.__enemy.lives}\n"
        )

    def game_over(self):
        # sys.stdout.write("\x1bc")
        print("GAME OVER!!")
        print(f"Final Score: {self.__score}")

    def win(self):
        print(f"You Win!\nFinal Score: {self.__score}")

    def play(self):
        KEYS = NBInput()
        KEYS.nb_term()
        while time.time() - self.__start < GAME_TIME:
            self.repaint()
            time.sleep(0.08)
            INPUT = ""
            if KEYS.kb_hit():
                INPUT = KEYS.get_ch()
            self.transition(INPUT)
            KEYS.flush()
            if self.__enemy.lives <= 0:
                self.win()
                break
            if self.__player.lives <= 0:
                self.game_over()
                break
