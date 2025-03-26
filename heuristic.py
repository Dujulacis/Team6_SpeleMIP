class TreeNode:
    def __init__(self, data, depth=0):
        self.data = data
        self.parent = None
        self.children = []
        self.p1points = 0
        self.p2points = 0
        self.bestmove = depth

    def addChild(self, node):
        self.children.append(node)

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented
        return (
            self.data == other.data and
            self.p1points == other.p1points and
            self.p2points == other.p2points and
            self.bestmove == other.bestmove
        )

    def __hash__(self):
        return hash((self.data, self.p1points, self.p2points, self.bestmove))
    
    def heuristic(self):
        return (self.p1points - self.p2points) + (1200 - self.data) * 0.01 # Fromula, kura dod koeficentu. (Vel būs uzalbota)


def buildTree(startNumb):
    root = TreeNode(startNumb, 0)
    createdNodes = set()
    createLevel(root, createdNodes, 5)  # Uzstādīts dzīļums - 5 līmeņi, lai varētu dabūt viss atrāko uzvaru priekš P1.
    return root


def createLevel(parentNode, createdNodes, maxDepth):
    if parentNode.bestmove >= maxDepth:
        return
    
    number = parentNode.data
    if number >= 1200:
        return
    
    nodes = [TreeNode(number * 2, parentNode.bestmove + 1),
             TreeNode(number * 3, parentNode.bestmove + 1),
             TreeNode(number * 4, parentNode.bestmove + 1)]

    for node in nodes:
        node.p1points = parentNode.p1points
        node.p2points = parentNode.p2points
        
        addPoints(node)
        
        if node not in createdNodes:
            parentNode.addChild(node)
            createdNodes.add(node)
            createLevel(node, createdNodes, maxDepth)
        else:
            for existing_node in createdNodes:
                if existing_node == node:
                    parentNode.addChild(existing_node)
                    break


def addPoints(node):
    if node.bestmove % 2 == 1:
        if node.data % 2 == 0:
            node.p2points -= 1
        else:
            node.p1points += 1
    else:
        if node.data % 2 == 0:
            node.p1points -= 1
        else:
            node.p2points += 1


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


def printPath(path):
    for data, p1, p2, turn in path:
        print(f"{data} (P1: {p1}, P2: {p2}), Move: {turn}")


def printTree(root):
    for node in root.children:
        # Labakais Gājiens priekš P1. Ja ir mīnusā skaitlis, tad ir slikts gājiens. 
        print("--" * node.bestmove + ">" + str(node.data) + 
              f" (P1: {node.p1points}, P2: {node.p2points}), Bestmove: {node.heuristic()}")
        printTree(node)


if __name__ == '__main__':
    Tree = buildTree(8)
    short_path = ShortWinP1(Tree)

    printTree(Tree)

if short_path:
    print("\nShort win for P1:")
    printPath(short_path)
