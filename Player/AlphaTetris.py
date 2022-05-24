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

Time Limit: 9999 （总共用时）

First Thoughts: just put piece in lowest place possible

TODO
- IMPORTANT:
    - Height wrong for Team 2
    - Holes wrong for Team 2

- Finish VillainScore
    - Enemy Repeated Moves
- Make decision Tree
    - Save Decision Paths?
- Be Conscious of Time
- Combine Scoring to be more efficient?

OPTIONAL TODO:
- Find way to improve winChance of going second
    - Currently around 9% (n = 100) against self
    - 48% (n = 100) against pickFirst
- Board redone with numpy
- Redo Functions with Numpy if they need to be faster
"""


class Player:
    def __init__(self, isFirst):
        self.isFirst = isFirst

        self.initialized = False
        self.blocks = None
        self.blockNum = None
        self.colRange = range(15)
        self.currentHoles = 0

    def output(self, matchData):
        # Redo Board with NUMPY
        if not self.initialized:
            self.blocks = list(matchData.getBlockList())
            self.blockNum = 1 if self.isFirst else 2
            self.initialized = True

        def copyBoard(board):
            if self.isFirst:
                return list(map(list, board))
            if not self.isFirst:
                return [j[::-1] for j in reversed(board)]

        def linesFull(board):
            full = 0
            for line in board:
                if 0 in line:
                    continue
                full += 1
            return full

        def holesFound(board):
            def checkColForHoles(col):
                hole = 0
                head = False
                for i in self.colRange:
                    if board[i][col] == 1:
                        head = True
                    elif head and board[i][col] == 0:
                        hole += 1
                    else:
                        head = False
                return hole

            return sum([checkColForHoles(i) for i in range(10)])

        def getColumnHeights(board) -> list:
            def getColumnHeight(col):
                for i in self.colRange:
                    if board[i][col]:
                        return 15 - i
                return 0
        
            return [getColumnHeight(i) for i in range(10)]

        def bumpiness(ch):
            bumpiness = 0

            for i in range(len(ch) - 1):
                bumpiness += abs(ch[i] - ch[i + 1])
            return bumpiness

        def villainScore(board):
            vScore = 0
            return vScore

        if self.blockNum < len(self.blocks):
            block = self.blocks[self.blockNum]

        board = matchData.getBoard()
        validMoves = matchData.getAllValidAction(block, board)

        scores = []
        holes = []
        for move in validMoves:
            testBoard = copyBoard(board)

            # Can use Numpy to reimplement
            matchData.putBlock(block, move, testBoard)
            columnHeights = getColumnHeights(testBoard)

            # 这些儿让调试组去调吧
            scores.append(
                0
                + 850 * linesFull(testBoard)
                - 900 * (holesFound(testBoard) - self.currentHoles)
                - 650 * sum(columnHeights)
                - 100 * bumpiness(columnHeights)
                - 300 * villainScore(testBoard)
            )
            holes.append(holesFound(testBoard))
        
        self.blockNum += 2
        idx = 0
        if scores != []:
            idx = scores.index(max(scores))
            self.currentHoles = holes[idx]

            if 0:
                print()
                print(validMoves)
                # print("Heights", heights)
                print("Holes", holes)
                print(f"New Holes: ", self.currentHoles, holes[idx])
                print(idx, validMoves[idx])
                print("Chosen Holes: ", holes[idx])
                # print("Chosen Height: ", heights[idx])
        return validMoves[idx]
