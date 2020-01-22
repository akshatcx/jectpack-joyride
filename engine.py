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
        self.arena = Arena()
        self.player = Mando(self.arena.board)
        self.enemy = Enemy(self.arena.board)
        self.score = 0
        self.start = time.time()
        self.frame = 0

    def transition(self, key):
        status = 0
        if self.frame < WIDTH - ENEMY_OFFSET:
            self.frame += 1
            status += self.player.move_relative(self.arena.board, self.frame)            
        status += self.player.move(self.arena.board, key, self.frame)
        self.player.upd_att(self.arena.board, key, self.frame)
        self.enemy.move(self.arena.board,self.player.location)
        if int(time.time() - self.start) % 3 == 0:
            self.enemy.shoot(self.arena.board)
        self.enemy.move_ice(self.arena.board)
        self.score += status

    def repaint(self):
        #sys.stdout.flush()
        #sys.stdout.write("\x1bc")
        print("\x1bc")
        self.arena.render(self.frame)
        print(f"Score: {self.score}\t Lives: {self.player.lives}\t Time Left: {int(GAME_TIME - (time.time() - self.start))}secs\t Enemy Lives: {self.enemy.lives}\n")

    def game_over(self):
        # sys.stdout.write("\x1bc")
        print("GAME OVER!!")
        print(f"Final Score: {self.score}")

    def play(self):
        KEYS = NBInput()
        KEYS.nb_term()
        while self.player.lives > 0 and time.time() - self.start < GAME_TIME and self.enemy.lives > 0:
            self.repaint()
            time.sleep(0.08)
            INPUT = ""
            if KEYS.kb_hit():
                INPUT = KEYS.get_ch()
            self.transition(INPUT)
            KEYS.flush()
        self.game_over()
