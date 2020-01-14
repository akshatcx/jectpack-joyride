#!/usr/bin/env python3
# coding: utf-8
from engine import Engine
from config import *
import colorama


def main():
    colorama.init()
    engine = Engine()
    engine.play()


if "__name__" == "__main__":
    main()
