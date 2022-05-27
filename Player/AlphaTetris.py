def copyBoard(board):
    return list(map(list, board))

def reverseBoard(board):
    return [j[::-1] for j in reversed(board)]

def printBoard(board):
    l = [[f"{'o' if i == 0 else 'x'}" for i in line]for line in board]
    
    print('\n'.join([''.join(i) for i in l]))

class AlphaNode:
    def __init__(self, block, board, move, md, isEnemy, emptyNode=False) -> None:
        self.move = move
        self.md = md
        self.board = board
        self.block = block
        self.isEnemy = isEnemy
        
        self.paths = {}

        # Total Score is negative for Enemy, 
        # positive for us
        # Still need to decide how it's calculated.
        self.totalScore = 0

        if not emptyNode:
            self.getScoring()


    def getScoring(self):
        colRange = range(15)
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
                return sum([1 for _ in holes])
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
        
        self.md.putBlock(self.block, self.move, self.board)
        ch = getColumnHeights(self.board)
        self.score = possibleScore(self.board)
    
        self.holes = holesFound(self.board)
        self.bump = bumpiness(ch)
        self.height = sum(ch)

        # Calculate Total Score
        totalScore = 0
        totalScore += self.score   * 1000

        # Might Not have totalScore, instead just have Score
        # and use __lt__(self, other) to determine instead.
        # Will see.
        totalScore -= self.holes   * 100
        totalScore -= self.bump    * 100
        totalScore -= self.height  * 100

        self.totalScore = totalScore


    # recurses through all children to get max score
    def getFinalScore(self):
        current = self.paths
        while current != {}:
            maxChild: self = max(current, key=lambda x: current[x])
            maxChild = current[maxChild]
            if maxChild.isEnemy:
                self.totalScore -= maxChild.totalScore
            else:
                self.totalScore += maxChild.totalScore
            current = maxChild.paths
    
    def addChild(self, child):
        self.paths[child.move] = child

    def getMove(self):
        return self.move

    def __str__(self) -> str:
        return f"AlphaNode<{self.move}, {self.totalScore}, {self.isEnemy}>"

    def __repr__(self) -> str:
        return str(self)
    # Used to Sort Scores
    def __lt__(self, other):
        # TEMPORARY - SUBJECT TO CHANGE
        return self.totalScore < other.totalScore


class AlphaTetris:
    def __init__(self, isFirst, depth) -> None:
        # Key: move: (int, int, int)
        # Val: data: AlphaNode
        self.savedpaths = {}

        self.root = None
        
        self.isFirst = isFirst
        self.md = None
        self.blockList = None
        self.blockNum = None

        self.runDepth = depth
        self.possibleMoves = []

    
    # Setups the Decision Tree
    def setup(self, md):
        self.md = md
        self.blockList = list(self.md.getBlockList())
        self.blockNum = 1 if self.isFirst else 2
    
    # TODO Fix Enemy Move checking
    # Should be able to run recursively with depth and lastMove
    # Calculates all the moves in the currently available moveset
    # Need to check what happens when enemy moveset is empty -> Need to keep checking our moveset
    # So should just ignore enemy move
    def calculate(self, lastMove: AlphaNode, depth: int):
        isEnemy = depth % 2 != 0
        if self.blockNum + depth > len(self.blockList):
            return
        block = self.blockList[self.blockNum + depth]

        # print("depth:", depth, lastMove)
        if lastMove is not None:
            board = copyBoard(lastMove.board)
            board = reverseBoard(board)

        if depth == 1:
            print(lastMove)
        

        validMoves = self.md.getAllValidAction(block, board)
        nextMoves = []
        for move in validMoves:
            if isEnemy and move[0] < (8 if block == 1 else 9):
                continue
            
            tempBoard = copyBoard(board)
            nextMoves.append(AlphaNode(block, tempBoard, move, self.md, isEnemy))
        
        if nextMoves == [] and validMoves != []:
            nextMoves.append(AlphaNode(block, board, validMoves[0], self.md, isEnemy))

        return nextMoves


    # Updates the Decision Tree - Call every Turn
    def update(self, md):
        self.md = md
        la = self.md.getLastAction()


        if self.root and la in self.root.paths:
            print(la, '\n', self.root.paths)
            self.root = self.root.paths[la]
        else:
            board = self.md.getBoard()
            if not self.isFirst:
                board = reverseBoard(board)
            self.root = AlphaNode(0, board, 0, 0, True, emptyNode=True)

        print(self.root.isEnemy)
        self.newMove()
        self.blockNum += 2

        # if la[0] < 8 if self.blockList[self.blockNum - 1] == 1 else 9:
        #     # get next move
        #     return
        # if la in self.savedpaths:
        #     self.calculate(False, self.savedpaths[la], self.runDepth - 2)
        #     return

    # TODO Fix
    # Recurses through the next self.runDepth moves
    def newMove(self):

        current = [AlphaNode(0, self.md.getBoard(), 0, 0, True, emptyNode=True) if self.root is None else self.root]
        for depth in range(self.runDepth):
            # Set proper First Move
            for move in current:
                temp = self.calculate(move, depth)
                if move is not None:
                    for i in temp:
                        move.addChild(i)
            if depth == 0:
                self.possibleMoves = temp
            current = temp
    
        # print(self.possibleMoves
        for move in self.possibleMoves:
            move.getFinalScore()


class Player:
    def __init__(self, isFirst):
        self.isFirst = isFirst

        self.initialized = False
        self.blocks = None
        self.blockNum = None
        self.colRange = range(15)
        self.currentHoles = 0

        self.brain = AlphaTetris(self.isFirst, 2)

    def output(self, matchData):
        # Redo Board with NUMPY
        if not self.initialized:
            self.brain.setup(matchData)

            self.blocks = list(matchData.getBlockList())
            self.blockNum = 1 if self.isFirst else 2
            self.initialized = True

        self.brain.update(matchData)
        
        move = max(self.brain.possibleMoves)
        self.brain.root = move
        print(f"Player {1 if self.isFirst else 2}")
        print(move)
        printBoard(move.board)
        return move.move
