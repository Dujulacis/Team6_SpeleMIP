def alphaBeta(self, alpha, beta):
    if not self.children:
        if self.p1points > self.p2points:
            self.alphaBetaScore = 1
        elif self.p1points < self.p2points:
            self.alphaBetaScore = -1
        else:
            self.alphaBetaScore = 0
        print(f"Leaf node {self.gameNum}, P1: {self.p1points}, P2: {self.p2points}, Score: {self.alphaBetaScore}")
        return self.alphaBetaScore

    if self.maximize:
        value = float('-inf')
        for child in self.children:
            child.maximize = False
            value = max(value, child.alphaBeta(alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        self.alphaBetaScore = value
        print(f"Max node {self.gameNum}, P1: {self.p1points}, P2: {self.p2points}, Score: {self.alphaBetaScore}")
        return value
    else:
        value = float('inf')
        for child in self.children:
            child.maximize = True
            value = min(value, child.alphaBeta(alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break 
        self.alphaBetaScore = value
        print(f"Min node {self.gameNum}, P1: {self.p1points}, P2: {self.p2points}, Score: {self.alphaBetaScore}")
        return value

