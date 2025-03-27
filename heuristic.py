import GameTree


class HeurTreeNode(GameTree.TreeNode):

    def heuristic(self):
        return (self.p1points - self.p2points) + (
                    1200 - self.gameNum) * 0.01  # Fromula, kura dod koeficentu. (Vel būs uzalbota)

    def ShortWinP1(node, path=[]):
        path.append((node.gameNum, node.p1points, node.p2points, node.turnCount))
        if node.gameNum >= 1200 and node.p1points > node.p2points:
            return path

        best_path = None
        for child in sorted(node.children, key=lambda x: x.p1points - x.p2points, reverse=True):
            new_path = HeurTreeNode.ShortWinP1(child, path[:])
            if new_path and (best_path is None or len(new_path) < len(best_path)):
                best_path = new_path

        return best_path

    def printPath(path):
        for data, p1, p2, turn in path:
            print(f"{data} (P1: {p1}, P2: {p2}), Move: {turn}")

    def printTree(self):
        for node in self.children:
            # Labakais Gājiens priekš P1. Ja ir mīnusā skaitlis, tad ir slikts gājiens.
            print("--" * node.turnCount + ">" + str(node.gameNum) +
                  f" (P1: {node.p1points}, P2: {node.p2points}), Bestmove: {node.heuristic()}")
            node.printTree()

    def buildTree(startNumb, depth=3):
        root = HeurTreeNode(startNumb, 0)
        createdNodes = set()
        GameTree.createLevel(root, createdNodes, depth)  # uzstādīts dzīļums - 3 līmeņi
        return root


if __name__ == '__main__':
    Tree = HeurTreeNode(8)
    Tree.generateLevel(3)
    Tree.printTree()
    short_path = HeurTreeNode.ShortWinP1(Tree)

    HeurTreeNode.printTree(Tree)

if short_path:
    print("\nShort win for P1:")
    HeurTreeNode.printPath(short_path)
