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

        self.comp = min if isFirst else max
        
        self.initialized = False

        self.blocks = None
        self.blockNum = None
        

    def output(self, matchData):
        if not self.initialized:
            self.blocks = list(matchData.getBlockList())
            self.blockNum = 1 if self.isFirst else 2
            self.initialized = True
        
        board = matchData.getBoard()
        block = self.blocks[self.blockNum]

        validMoves = matchData.getAllValidAction(block, board)
        

        move = self.comp(validMoves, key=lambda x:x[0])
        self.blockNum += 2
        return move
