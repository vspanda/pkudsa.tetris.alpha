class Tuple:
    pass
class MatchData:
    pass

import math, random, copy, time, collections, itertools, functools, operator, numpy


class Player:
    def __init__(self, isFirst: bool) -> None:
        self.isFirst = isFirst

    def output(self, matchData: MatchData) -> Tuple[int, int, int]:
        return