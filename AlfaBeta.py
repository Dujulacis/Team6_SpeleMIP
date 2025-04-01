from Heuristic import HeurTreeNode

"""
Alpha-beta atzarošanas algoritms ir būtībā Minimax uzlabota versija.
Tas izmanto alpha un beta robežvērtības, lai atsijātu nevajadzīgus spēles koka zarus, 
kas ļauj būtiski paātrināt aprēķinu procesu, saglabājot to pašu optimālo rezultātu.
"""

class AlphaBetaTree(HeurTreeNode):
    def __init__(self, startingNumber, p1Points, p2Points, turnCount, maximize=True):
        super().__init__(startingNumber, p1Points, p2Points, turnCount)
        self.maximize = maximize           # Nosaka vai mezgls ir maksimizējošs
        self.alphaBetaScore = None         # Saglabā AlfaBeta aprēķināto rezultātu

    # Ja nav bērnu, esam sasnieguši strupceļu, tika novērtēts rezultāts
    def alphaBeta(self, alpha, beta):
        if not self.children:
            if self.bestmove >= 0:
                self.alphaBetaScore = 1
            else:
                self.alphaBetaScore = -1
            return self.alphaBetaScore

        if self.maximize:
            value = float('-inf')            # Uzstāda sākotnējo vērtību, kuru jāmaksimizē
            for child in self.children:
                child.maximize = False       #Pārslēdz uz min spēlētāju
                value = max(value, child.alphaBeta(alpha, beta)) # Salīdzina vērtības
                alpha = max(alpha, value)    # Atjaunina alpha robežu
                if alpha >= beta:            # Ja alpha ir lielāks vai vienāds ar beta, pārtrauc meklēšanu
                    break
            self.alphaBetaScore = value      # Saglabā labāko rezultātu
        else:
            value = float('inf')             # Uzstāda sākotnējo vērtību, kuru jāminimizē
            for child in self.children:
                child.maximize = True        # Pārslēdz uz max spēlētāju
                value = min(value, child.alphaBeta(alpha, beta)) # Salīdzina vērtības
                beta = min(beta, value)      # Atjaunina beta robežu
                if beta <= alpha:            # Ja beta ir mazāks vai vienāds ar alpha, pārtrauc meklēšanu
                    break
            self.alphaBetaScore = value
        
        return self.alphaBetaScore
    
    def generateLevel(self, depth): #Ģenerē koku līdz 4. līmenim un aprēķina AlphaBeta vērtības
        super().generateLevel(depth)          # Ģenerē nākamo līmeni
        self.alphaBeta(float('-inf'), float('inf')) # Sākotnējās robežas ir bezgalības

if __name__ == "__main__":
    alphaBetaTree = AlphaBetaTree(8, 0, 0, 0, maximize=True)
    alphaBetaTree.generateLevel(4)
    
    kokaDala = alphaBetaTree.children[0].children[0].children[0].children[0]
    kokaDala.generateLevel(4)
