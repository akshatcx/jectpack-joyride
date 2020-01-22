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
        self.__board = self.gen_board()

    @property
    def board(self):
        return self.__board
        
    def gen_board(self):
        new_board = np.zeros((HEIGHT, WIDTH))
        floor = Floor(new_board, [HEIGHT - 1, 0])

        prop_counts = {
            Coin: 15,
            Lazer_H: 10,
            Lazer_V: 10,
            Lazer_D1: 6,
            Lazer_D2: 6,
            Magnet: 1,
            Powerup: 1,
        }

        for prop in prop_counts:
            for i in range(prop_counts[prop]):
                is_valid = False
                while not is_valid:
                    location = [
                        random.randint(8, HEIGHT - F_SIZE[0] - 2),
                        random.randint(PROP_OFFSETL, PROP_OFFSETR),
                    ]
                    obj = prop(new_board, location)
                    print(
                        new_board[
                            obj.location[0] - obj.size[0] + 1 : obj.location[0] + 1,
                            obj.location[1] : obj.location[1] + obj.size[1],
                        ]
                    )
                    if (
                        new_board[
                            obj.location[0] - obj.size[0] + 1 : obj.location[0] + 1,
                            obj.location[1] : obj.location[1] + obj.size[1],
                        ]
                        == np.zeros(obj.size)
                    ).all():
                        print("TRUE")
                        obj.place(new_board, obj.id)
                        is_valid = True

        return new_board

    def render(self, frame):

        color_mappings = {
            0: Back.BLACK + Fore.BLACK + " ",
            2: Back.BLUE + Fore.BLUE + ">",
            1: Back.BLACK + Fore.YELLOW + "\u25CF",
            3: Back.BLUE + Fore.WHITE + "+",
            4: Back.BLACK + Fore.WHITE + "\u254D",
            5: Back.WHITE + Fore.WHITE + " ",
            6: Back.GREEN + Fore.GREEN + " ",
            7: Back.RED + Fore.RED + " ",
            8: Back.RED + Fore.RED + " ",
            9: Back.RED + Fore.RED + " ",
            10: Back.RED + Fore.RED + " ",
            11: Back.MAGENTA + Fore.MAGENTA + " ",
            14: Back.BLUE + Fore.BLUE + " ",
            15: Back.BLACK + Fore.BLUE + "\u2744",
        }
        """
        buff = "\n".join(
            [
                f"{''.join([color_mappings[pixel] for pixel in row[frame:frame + HEIGHT*2 + 1]])}{Style.RESET_ALL}"
                for row in self.board
            ]
        )
        stdout.write(buff + "\n")
        """
        for row in self.board:
            for pixel in row[frame:frame+ (HEIGHT*3)+1]:
                print(color_mappings[pixel], end = '')
            print(Style.RESET_ALL)
