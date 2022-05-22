"""
PKUDSA Tetris ALPHA Team AI
2022.5.22

"""

import math, random, copy, time, collections, itertools, functools, operator, numpy


class Player:
    def __init__(self, isFirst: bool) -> None:
        self.isFirst = isFirst

    def output(self, matchData) -> tuple(int, int, int):
        return
