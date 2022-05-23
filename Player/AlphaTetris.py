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

Time Limit: 9999

First Thoughts: just put piece in lowest place possible
"""


class Player:
    def __init__(self, isFirst):
        self.isFirst = isFirst

        self.initialized = False
        self.blocks = None
        self.blockNum = None

    def output(self, matchData):
        # Redo Board with NUMPY
        if not self.initialized:
            self.blocks = list(matchData.getBlockList())
            self.blockNum = 1 if self.isFirst else 2
            self.initialized = True

        def copyBoard(board):
            return list(map(list, board))

        def linesFull(board):
            full = 0
            for line in board:
                if 0 not in line:
                    full += 1
            return full

        def holesFound(board):
            holes = 0

            return holes

        def aggregateHeight(board):
            if self.isFirst:
                base = 15
                colRange = range(15)
                getHeight = lambda x: base - x
                pass
            else:
                base = 10
                colRange = range(24, 9, -1)
                getHeight = lambda x: x - base
                pass

            def getColumnHeight(col):
                for i in colRange:
                    if board[i][col]:
                        return getHeight(i)
                return 0

            height = 0
            for i in range(10):
                height += getColumnHeight(i)

            return height

        def bumpiness(board):
            bumpiness = 0
            return bumpiness

        def villainScore(board):
            vScore = 0
            return vScore

        board = matchData.getBoard()
        if self.blockNum < len(self.blocks):
            block = self.blocks[self.blockNum]

        validMoves = matchData.getAllValidAction(block, board)

        scores = []
        for move in validMoves:
            testBoard = copyBoard(board)

            # Can use Numpy to reimplement
            matchData.putBlock(block, move, testBoard)
            scores.append(
                0
                + 750 * linesFull(testBoard)
                - 300 * holesFound(testBoard)
                - 500 * aggregateHeight(testBoard)
                - 200 * bumpiness(testBoard)
                - 300 * villainScore(testBoard)
            )
        self.blockNum += 2
        if validMoves == []:
            return (0, 0, 0)
        return validMoves[scores.index(max(scores))]
