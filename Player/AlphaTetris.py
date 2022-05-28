DEBUG = False

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
        rowRange = range(10)
        
        def colTransitions(board):
            transitions = 0
            for j in rowRange:
                lastPiece = board[0][j]
                for i in range(1, 15):
                    if board[i][j] != lastPiece:
                        transitions += 1
                        lastPiece = board[i][j]
            return transitions
        def rowTransitions(board):
            transitions = 0
            for j in colRange:
                lastPiece = board[j][0]
                for i in range(1, 10):
                    if board[j][i] != lastPiece:
                        transitions += 1
                        lastPiece = board[j][i]
            return transitions
        def holesFound(board):
            holes = 0
            for j in rowRange:
                cHole = None
                for i in colRange:
                    if cHole is None and board[i][j] == 1:
                        cHole = 0
                    if cHole is not None and board[i][j] == 0:
                        cHole += 1
                if cHole is not None:
                    holes += cHole
            return holes
        def boardWells(board):
            SUM = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
            ws = 0
            for j in rowRange:
                wells = 0
                for i in colRange:
                    try:
                        if (j - 1 < 0 or board[i][j - 1] != 0) and (j + 1 >= 10 or board[i][j + 1] != 0):
                            wells += 1
                    except IndexError:
                        print('h')
                    else:
                        ws += SUM[wells]
                        wells = 0
            return ws
        
        self.md.putBlock(self.block, self.move, self.board)
        # ch = getColumnHeights(self.board)
        lines = self.md.removeLines(self.board)
        
        self.board = lines[0]
        self.score = 2 ** (lines[1] - 2) + 2 ** (lines[2] - 1)
        # self.score = lines[1] * 2 + lines[2]

        self.rTran = rowTransitions(self.board)
        self.cTran = colTransitions(self.board)
        self.holes = holesFound(self.board)

        self.wells = boardWells(self.board)


        # self.bump = bumpiness(ch)
        # self.height = sum(ch)

        # Might Not have totalScore, instead just have Score
        # and use __lt__(self, other) to determine instead.
        # Will see.
        # Calculate Total Score
        totalScore = 0



        # Landing Height
        totalScore -= (15 - self.move[0]) * 45

        # Removed Lines (NOT ERODED PIECES)
        totalScore += self.score   * 34

        # Row Transitions
        totalScore -= self.rTran   * 32

        # Col Transitions
        totalScore -= self.cTran   * 93

        # Buried Holes
        totalScore -= self.holes   * 79

        # Board Wells
        totalScore -= self.wells   * 34


        # totalScore -= self.bump    * 10
        # totalScore -= self.height  * 20

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
        if self.totalScore < other.totalScore:
            return True
        elif self.totalScore > other.totalScore:
            return False
        # Equal, ish
        else:
            scol = 6 - self.move[1]
            ocol = 6 - other.move[1]

            if scol < 0:
                scol *= -1
                scol += 10
            if ocol < 0:
                ocol *= -1
                ocol += 10
            
            return scol < ocol





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
    
    # Should be able to run recursively with depth and lastMove
    # Calculates all the moves in the currently available moveset
    # Need to check what happens when enemy moveset is empty -> Need to keep checking our moveset
    # So should just ignore enemy move
    def calculate(self, lastMove: AlphaNode, depth: int):
        isEnemy = depth % 2 != 0
        if self.blockNum + depth > len(self.blockList):
            return
        block = self.blockList[self.blockNum + depth]
        
        if lastMove is not None:
            board = copyBoard(lastMove.board)
            board = reverseBoard(board)


        if DEBUG and depth == 0:
            # print("depth:", depth, lastMove)
            print("Last Move:", lastMove)
        

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

        if DEBUG:
            print(la)

        if self.root and la in self.root.paths:
            if DEBUG:
                print(la, '\n', self.root.paths)
            self.root = self.root.paths[la]
        else:
            board = self.md.getBoard()
            if la:
                board = reverseBoard(board)
                self.root = AlphaNode(self.blockList[self.blockNum - 1], board, la, md, True)
            else:
                self.root = AlphaNode(0, board, (0, 0, 0), 0, True, emptyNode=True)

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
        tempBoard = self.md.getBoard()
        if not self.isFirst:
            tempBoard = reverseBoard(tempBoard)
        current = [AlphaNode(0, tempBoard, (0, 0, 0), 0, True, emptyNode=True) if self.root is None else self.root]
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

        if DEBUG:
            print(f"Player {1 if self.isFirst else 2}")
            print(move)
            printBoard(move.board)
        return move.move
