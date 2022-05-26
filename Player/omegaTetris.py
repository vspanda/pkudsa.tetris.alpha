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
            else:
                return [j[::-1] for j in reversed(board)]

        def linesFull(board, enemy=False):
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
                hole = 0
                head = False
                for i in self.colRange:
                    if board[i][col]:
                        head = True
                    if head and board[i][col] == 0:
                        hole += 1
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
            vScore = []
            if self.blockNum + 1 < len(self.blocks):
                vblock = self.blocks[self.blockNum + 1]
            vBoard = copyBoard(board)
            vMoves = matchData.getAllValidAction(vblock, vBoard)

            for vmove in vMoves:
                if vmove[0] < (8 if vblock == 1 else 9):
                    continue

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
        heights = []
        for move in validMoves:
            testBoard = copyBoard(board)

            # Can use Numpy to reimplement
            matchData.putBlock(block, move, testBoard)
            columnHeights = getColumnHeights(testBoard)

            # 这些儿让调试组去调吧
            scores.append(
                0
                + 850 * linesFull(testBoard)
                - 300 * (holesFound(testBoard) - self.currentHoles)
                - 650 * sum(columnHeights)
                - 100 * bumpiness(columnHeights)
                - 500 * villainScore(testBoard)
            )
            holes.append(holesFound(testBoard))
            heights.append(sum(columnHeights))

        self.blockNum += 2
        idx = []
        if scores != []:
            idx = [i for i, v in enumerate(scores) if v == max(scores)]

            idx = idx[0]
            self.currentHoles = holes[idx]

            # Debugging purposes
            if 0:
                print()
                print(validMoves)
                print("Heights", heights)
                print("Holes", holes)
                print(idx, validMoves[idx])
                print("Chosen Holes: ", holes[idx])
                print("Chosen Height: ", heights[idx])
        return validMoves[idx]
