import GameTree


class HeurTreeNode(GameTree.TreeNode):
	def __init__(self, startingNumber, depth=0):
		super().__init__(startingNumber, depth)
		self.bestmove = None

	def __init__(self, startingNumber, turnCount, p1Points, p2Points):
		super().__init__(startingNumber, turnCount,p1Points,p2Points)
		self.bestmove = None

	def bestMove(self):
		 return round((3 * (self.p1points - self.p2points) + ((1200 - self.gameNum) * (self.p1points - self.p2points))) / 20, 2)  # Fromula, kura dod koeficentu. (uzlabota versija)

	def printTree(self):
		for node in self.children:
			print("--" * node.turnCount + ">" + str(node.gameNum) + f" (P1: {node.p1points}, P2: {node.p2points}), Bestmove: {node.bestmove}")
			node.printTree()

	def addPoints(self):
		super().addPoints()
		self.bestmove = self.bestMove()


"""
Viss īsākais ceļš priekš P1. Nedzēsu arā, vien karši sakomentēju

def ShortWinP1(node, path=[]):
    path.append((node.data, node.p1points, node.p2points, node.bestmove))
    if node.data >= 1200 and node.p1points > node.p2points:
        return path
    
    best_path = None
    for child in sorted(node.children, key=lambda x: x.p1points - x.p2points, reverse=True):
        new_path = ShortWinP1(child, path[:])
        if new_path and (best_path is None or len(new_path) < len(best_path)):
            best_path = new_path
    
    return best_path
"""

if __name__ == '__main__':
	Tree = HeurTreeNode(8)
	Tree.generateLevel(5)
	Tree.printTree()
