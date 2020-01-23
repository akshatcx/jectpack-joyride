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
            Coin: 20,
            Lazer_H: 10,
            Lazer_V: 10,
            Lazer_D1: 8,
            Lazer_D2: 8,
            Magnet: 1,
            Powerup: 5,
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

    def render(self, frame, dloc):

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
            21: Back.BLACK + Fore.BLUE + " ",
            22: Back.BLACK + Fore.RED + "/",
            23: Back.BLACK + Fore.RED + ",",
            24: Back.BLACK + Fore.RED + ";",
            25: Back.BLACK + Fore.RED + "'",
            26: Back.BLACK + Fore.RED + ".",
            27: Back.BLACK + Fore.RED + ":",
            28: Back.BLACK + Fore.RED + "`",
            30: Back.BLACK + Fore.RED + "\U0001F525"
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

        dragon = "  /,,;';;.  ,;;;..  ,,;.    '\n.',''   `::;:' ``;;;;'  `..' \n`      ,,/'     ,,//         "
        dnp = np.zeros(E_SIZE)

        m = {
            " ": 21,
            "/": 22,
            ",": 23,
            ";": 24,
            "'": 25,
            ".": 26,
            ":": 27,
            "`": 28,
        }

        for i, line in zip(range(3), dragon.split("\n")):
            for j, l in zip(range(29), line):
                dnp[i, j] = m[l]

        self.board[
            dloc[0] - 2 : dloc[0] - 2 + E_SIZE[0], dloc[1] : dloc[1] + E_SIZE[1]
        ] = dnp

        for row in self.board:
            for pixel in row[frame : frame + (HEIGHT * 3) + 1]:
                print(color_mappings[pixel], end="")
            print(Style.RESET_ALL)

        self.board[
            dloc[0] - 2 : dloc[0] + E_SIZE[0] - 2, dloc[1] : dloc[1] + E_SIZE[1]
        ] = np.full(E_SIZE, 14)
