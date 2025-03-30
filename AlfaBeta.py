class HeurTreeNode:
    def __init__(self, startingNumber, depth=0):
        self.gameNum = startingNumber
        self.depth = depth
        self.children = []
        self.p1points = 0
        self.p2points = 0
        self.bestmove = None
        self.turnCount = depth
        self.node_id = id(self)  # Unikāls mezgla identifikators

    def addChild(self, node):
        if node.node_id not in [child.node_id for child in self.children]:
            self.children.append(node)
        else:
            print(f"Mezgls {node.gameNum} jau eksistē, ID: {node.node_id}")

    def generateLevel(self, depth):
        if depth > 0:  # ja ir ko ģenerēt
            new_game_num = self.gameNum * 2  # Loģiskā noteikuma piemērs jaunam mezglam
            child_node = HeurTreeNode(new_game_num, self.depth + 1)
            self.addChild(child_node)
            child_node.generateLevel(depth - 1)

    def evaluate(self):
        # Minimax izmantotās aplēses piemērs
        return self.p1points - self.p2points  # starpība starp 1. un 2. spēlētāja punktiem.

    def alphaBeta(self, alpha, beta, maximizingPlayer):
        """
        Alfa-Beta griešanas algoritms minimax noteikšanai
        """
        if self.depth == 0 or not self.children:  # Galīgais mezgls vai sasniegtais maksimālais dziļums
            return self.evaluate()

        if maximizingPlayer:  # Maksimizētāja gājiens (P1)
            maxEval = float('-inf')
            for child in self.children:
                eval = child.alphaBeta(alpha, beta, False) 
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else:  # Minimizētāja gājiens (P2)
            minEval = float('inf')
            for child in self.children:
                eval = child.alphaBeta(alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval

root = HeurTreeNode(8)
root.generateLevel(4)

# Alfa-Beta algoritms saknei ar maksimizētāju (P1)
alpha = float('-inf')
beta = float('inf')
result = root.alphaBeta(alpha, beta, True)

print(f"Alpha Beta result: {result}")
