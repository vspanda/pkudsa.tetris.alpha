"""
PKUDSA Tetris ALPHA Team AI
2022.5.22

Allowed Libraries:
- math
- random
- copy
- time
- collections
- itertools
- functools
- operator
- numpy

Time Limit per Turn: 9999

First Thoughts: just put piece in lowest place possible
"""

class Player:
    def __init__(self, isFirst):
        self.isFirst = isFirst

        self.comp = max

        self.initialized = False

        self.blocks = None
        self.blockNum = None

    def linesFull(self, board):
        f = 0
        for line in board:
            if 0 not in line:
                f += 1
        return f   

    def output(self, matchData):
        if not self.initialized:
            self.blocks = list(matchData.getBlockList())
            self.blockNum = 1 if self.isFirst else 2
            self.initialized = True

        board = matchData.getBoard()
        block = self.blocks[self.blockNum]

        validMoves = matchData.getAllValidAction(block, board)

        scores = []
        for move in validMoves:
            testBoard = board[:]
            matchData.putBlock(block, move, testBoard)
            scores.append(self.linesFull(testBoard))

        self.blockNum += 2
        return validMoves[max(scores)]
