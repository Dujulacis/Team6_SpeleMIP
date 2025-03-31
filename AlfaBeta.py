from Heuristic import HeurTreeNode

class AlphaBetaTree(HeurTreeNode):
    def __init__(self, startingNumber, p1Points, p2Points, turnCount, maximize=True):
        super().__init__(startingNumber, p1Points, p2Points, turnCount)
        self.maximize = maximize
        self.alphaBetaScore = None

    def alphaBeta(self, alpha, beta):
        if not self.children:
            if self.bestmove >= 0:
                self.alphaBetaScore = 1
            else:
                self.alphaBetaScore = -1
            return self.alphaBetaScore

        if self.maximize:
            value = float('-inf')
            for child in self.children:
                child.maximize = False
                value = max(value, child.alphaBeta(alpha, beta))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # Beta cut-off
            self.alphaBetaScore = value
        else:
            value = float('inf')
            for child in self.children:
                child.maximize = True
                value = min(value, child.alphaBeta(alpha, beta))
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Alpha cut-off
            self.alphaBetaScore = value
        
        return self.alphaBetaScore

    def generateLevel(self, depth):
        super().generateLevel(depth)
        self.alphaBeta(float('-inf'), float('inf'))

if __name__ == "__main__":
    alphaBetaTree = AlphaBetaTree(8, 0, 0, 0, maximize=True)
    alphaBetaTree.generateLevel(4)
    
    kokaDala = alphaBetaTree.children[0].children[0].children[0].children[0]
    kokaDala.generateLevel(4)
    kokaDala.alphaBeta(float('-inf'), float('inf'))
