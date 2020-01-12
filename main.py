from engine import Engine
from config import *
import colorama
from utils import NBInput, clear

def init():
    colorama.init()

def main():
    init()
    
    engine = Engine()
    engine.play()
