from sys import stdout
import numpy as np
from colorama import Fore, Back, Style 
from props import *
from config import *
import random

class Arena:
    """Represents a single screen
    """

    def __init__(self):
        self.board = self.gen_board()

    def gen_board(self):
        new_board = np.zeros((HEIGHT, WIDTH))
        floor = Floor(new_board, [HEIGHT-1, 0])

        prop_counts = {
            Coin: 8,
            Lazer_H: 4,
            Lazer_V: 4,
            Lazer_D1: 2,
            Lazer_D2: 2,
            Magnet: 2
        }
        
        for prop in prop_counts:
            for i in range(prop_counts[prop]):
                is_valid = False
                while not is_valid:
                    location = [random.randint(8, HEIGHT-F_SIZE[0]-2),random.randint(PROP_OFFSETL, PROP_OFFSETR)]
                    obj = prop(new_board, location)
                    print(new_board[obj.location[0] - obj.size[0]+1:obj.location[0]+1,obj.location[1]:obj.location[1] + obj.size[1]])
                    if (new_board[obj.location[0] - obj.size[0]+1:obj.location[0]+1,obj.location[1]:obj.location[1] + obj.size[1]] == np.zeros(obj.size)).all():
                        print("TRUE")
                        obj.place(new_board, obj.id)
                        is_valid = True
            
        return new_board

    def render(self):
        
        color_mappings = {
            0: Back.BLACK + Fore.BLACK + ' ',
            1: Back.BLACK + Fore.YELLOW + u'\u25CF',
            5: Back.WHITE + Fore.WHITE + ' ',
            6: Back.GREEN + Fore.GREEN + ' ',
            7: Back.RED + Fore.RED + ' ',
            8: Back.RED + Fore.RED + ' ',
            9: Back.RED + Fore.RED + ' ',
            10: Back.RED + Fore.RED + ' ',
            3: Back.BLUE + Fore.WHITE + '+'
        }
        buff = "\n".join([f"{''.join([color_mappings[pixel] for pixel in row])}{Style.RESET_ALL}" for row in self.board])
        stdout.write(buff + '\n')

    
