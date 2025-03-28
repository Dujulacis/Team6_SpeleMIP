import GameTree


class HeurTreeNode(GameTree.TreeNode):

    def bestmove(self):
        return round((self.p1points - self.p2points) + (1200 - self.gameNum) * 0.02,2)  # Fromula, kura dod koeficentu. (Vel būs uzalbota)

    def printTree(self):
        for node in self.children:
            print("--" * node.turnCount + ">" + str(
                node.gameNum) + f" (P1: {node.p1points}, P2: {node.p2points}), Bestmove: {node.bestmove()}")
            node.printTree()


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
