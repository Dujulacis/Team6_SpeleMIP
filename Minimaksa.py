from Heuristic import HeurTreeNode

"""
Minimax algoritms tiek izmantots spēles koka ģenerēšanai un optimālā gājiena izvēlei.
Rekursīvi tiek aprēķināti visi iespējamie gājieni, un, balstoties uz heiristisku novērtējumu, 
tiek izvēlēts labākais risinājums (gājiens), pieņemot, ka pretinieks arī spēlē optimāli.
"""

class MiniMaxTree(HeurTreeNode):

	# Inicializē spēles koka mezglu, izmantojot HeurTreeNode klasi
	def __init__(self, startingNumber, p1Points, p2Points, turnCount, maximize = True):
		super().__init__(startingNumber, p1Points, p2Points, turnCount)
		self.maximize = maximize 	# Nosaka vai mezgls ir maksimizējošs
		self.minMaxScore = None 	# Saglabā maninmax aprēķināto rezultātu

	def minMax(self):
		# Ja skaitlis pārsniedz 1200, spēle beidzas
			if self.gameNum >= 1200:
				if self.maximize:
					self.minMaxScore = -1
				else:
					self.minMaxScore = 1
				return
			if self.children: # Ja ir bērni, aprēķina minimax vērtības rekursīvi
				for child in self.children:
					child.maximize = not self.maximize # Pārslēdz Max/Min lomu 
					child.minMax() 
			else:
				if self.bestmove >= 0: # Ja nav pēcteču, novērtē pašreizējo stāvokli
					self.minMaxScore = 1
				else:
					self.minMaxScore = -1
				return
				
			# Izvēlas labāko Min/Max vērtību starp bērniem 
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
	# Generē spēles koku līdz noteiktam dziļumam un aprēķina Minimax vērtības
	def generateLevel(self, depth):
		super().generateLevel(depth)
		self.minMax()
# Izveido saknes mezglu ar sākotnējiem parametriem 
if __name__ == "__main__":
	miniMaxTree = MiniMaxTree(99, 1, 1, 4, maximize = True)
	miniMaxTree.generateLevel(4) # Generē 4 līmeņu dziļu koku.

	# Paņem daļu no koka un paplašina to vēl par 4 līmeņiem
	kokaDala = miniMaxTree.children[0].children[0].children[0].children[0]
	kokaDala.generateLevel(4)
	kokaDala.minMax() # Aprēķina Minimax vērtības jaunajam koka apgabalam
