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
- Change Hole to 4 Sides
- Make decision Tree
    - Save Decision Paths?
- Be Conscious of Time
- Combine Scoring to be more efficient?
    - Scoring Graph? Save Heuristics instead of scores?
- Enemy Repeated Moves?

OPTIONAL TODO:
- Find way to improve winChance of going second
    - Currently around 9% (n = 100) against self
    - 48% (n = 100) against pickFirst
- Board redone with numpy
- Redo Functions with Numpy if they need to be faster
"""

def copyBoard(board, first):
    if first:
        return list(map(list, board))
    if not first:
        return [j[::-1] for j in reversed(board)]

class Player:
    class DecisionNode:
        def __init__(self, block, board, move, md) -> None:
            self.move = move

            self.children = []
            self.totalScore = 0

            colRange = range(15)
            # Points Scored
            def possibleScore(board, enemy = False):
                score = 0
                if not enemy:
                    full = 0
                    for line in range(10):
                        if 0 in board[line]:
                            continue
                        full += 1
                    score += 2 ** (full - 2)

                full = 0
                for line in range(10, 15):
                    if 0 in board[line]:
                        continue
                    full += 1
                score += 2 ** (full - 1)

                return score

            def holesFound(board):
                def checkColForHoles(col):
                    holes = []
                    head = False
                    for i in colRange:
                        if board[i][col] == 0:
                            if board[i - 1][col] == 1:
                                head = True
                            if head:
                                # keep hole (x, y) coord
                                holes.append((i, col))
                    # for each hole, check if true hole or false hole
                    for hole in holes:
                        hole[0], hole[1] # (x, y)

                    return holes

                return sum([checkColForHoles(i) for i in range(10)])

            def getColumnHeights(board) -> list:
                def getColumnHeight(col):
                    for i in colRange:
                        if board[i][col]:
                            return 15 - i
                    return 0        
                return [getColumnHeight(i) for i in range(10)]

            def bumpiness(ch):
                bumpiness = 0

                for i in range(len(ch) - 1):
                    bumpiness += abs(ch[i] - ch[i + 1])
                return bumpiness
            
            md.putBlock(block, board)

            ch = getColumnHeights(board)
            self.score = possibleScore(board)
            self.holes = holesFound(board)
            self.bump = bumpiness(ch)
            self.height = sum(ch)           

        
        
            
        
        




    class AlphaTetris:
        def __init__(self, isFirst) -> None:
            self.savedpaths = []
            
            self.isFirst = isFirst

            self.md = None
            self.blockList = None
            self.blockNum = None
        
        # Setups the Decision Tree
        def setup(self):
            self.blockList = list(self.md.getBlockList())
            self.blockNum = 1 if self.isFirst else 2
        
        # Updates the Decision Tree - Call every Turn
        def update(self, md):
            self.md = md

        
        
        
        def newMove(self, board):
            test = self.copyBoard(board, self.isFirst)

    
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

        # Points Scored
        def linesFull(board, enemy = False):
            score1 = 0
            if not enemy:
                full = 0
                for line in range(10):
                    if 0 in board[line]:
                        continue
                    full += 1
                score1 = 2 ** (full - 2)

            full = 0
            for line in range(10, 15):
                if 0 in board[line]:
                    continue
                full += 1
            score2 = 2 ** (full - 1)

            return score1 + score2

        def holesFound(board):
            def checkColForHoles(col):
                holes = []
                head = False
                for i in self.colRange:
                    if board[i][col] == 0:
                        if board[i - 1][col] == 1:
                            head = True
                        if head:
                            # keep hole (x, y) coord
                            holes.append((i, col))
                # for each hole, check if true hole or false hole
                for hole in holes:
                    hole[0], hole[1] # (x, y)

                return holes

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
            vScore = []
            if self.blockNum + 1 < len(self.blocks):
                vblock = self.blocks[self.blockNum + 1]
            vBoard = copyBoard(board)
            vMoves = matchData.getAllValidAction(vblock, vBoard)
            
            for vmove in vMoves:
                vboard = vBoard
                matchData.putBlock(vblock, vmove, vboard)

                vScore.append(linesFull(vboard))

            if vScore == []:
                return 0
            return max(vScore)

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
