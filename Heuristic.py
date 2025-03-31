from GameTree import TreeNode


class HeurTreeNode(TreeNode):
    def __init__(self, startingNumber, p1Points=0, p2Points=0, depth=0):
        super().__init__(startingNumber, p1Points, p2Points, depth)
        self.bestmove = None

    def bestMove(self):
        return round((self.p1points - self.p2points) + ((1200 - self.gameNum))/50, 2) # Uzlabojam formulu un uztaisījam vieglāg. Tagad neizvada 0, bet izvada tikai normalus skaitļus

    def printTree(self):
        for node in self.children:
            if node.gameNum <= 1200: # Neizvada skaitļus vairak par 1200 lai nepiesarņot, jo tur iet viss mīnusā tālāk
                print("--" * node.turnCount + ">" + str(node.gameNum) +
                      f" (P1: {node.p1points}, P2: {node.p2points}), Bestmove: {node.bestmove}")
                node.printTree()

    def addPoints(self):
        super().addPoints()
        self.bestmove = self.bestMove()


if __name__ == '__main__':
    Tree = HeurTreeNode(8, 0, 0)
    Tree.generateLevel(5)
    Tree.printTree()

