from Heuristic import HeurTreeNode

class MiniMaxTree(HeurTreeNode):
	def __init__(self, startingNumber, depth=0, maximize = True):
		super().__init__(startingNumber, depth)
		self.maximize = maximize
		self.minMaxScore = None

	def __init__(self, startingNumber, turnCount, p1Points, p2Points, maximize = True):
		super().__init__(startingNumber, turnCount, p1Points, p2Points)
		self.maximize = maximize
		self.minMaxScore = None

	def minMax(self):
			if self.children:
				for child in self.children:
					child.maximize = not self.maximize
					child.minMax()
			else:
				if self.bestmove >= 0:
					self.minMaxScore = 1
				else:
					self.minMaxScore = -1
				return

			self.minMaxScore = self.children[0].minMaxScore
			for child in self.children:
				if self.maximize and child.minMaxScore == 1:
					self.minMaxScore = 1
				elif self.maximize and child.minMaxScore == -1:
					self.minMaxScore = max(child.minMaxScore, self.minMaxScore)
				elif not self.maximize and child.minMaxScore == -1:
					self.minMaxScore = -1
				else:
					self.minMaxScore = min(child.minMaxScore, self.minMaxScore)

	def generateLevel(self, depth):
		super().generateLevel(depth)
		self.minMax()

if __name__ == "__main__":
	miniMaxTree = MiniMaxTree(8, maximize = True)
	miniMaxTree.generateLevel(4)

	kokaDala = miniMaxTree.children[0].children[0].children[0].children[0]
	kokaDala.generateLevel(4)
	kokaDala.minMax()
