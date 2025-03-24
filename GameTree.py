class TreeNode:
    def __init__(self, data, depth=0):
        self.data = data
        self.parent = None
        self.children = []
        self.p1points = 0
        self.p2points = 0
        self.turnCount = depth

    def addChild(self, node):
        self.children.append(node)

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented
        return (
            self.data == other.data and
            self.p1points == other.p1points and
            self.p2points == other.p2points and
            self.turnCount == other.turnCount
        )

    def __hash__(self):
        return hash((self.data, self.p1points, self.p2points, self.turnCount))


def buildTree(startNumb):
    root = TreeNode(startNumb, 0)
    createdNodes = set()
    createLevel(root, createdNodes, 3) # uzstādīts dzīļums - 3 līmeņi 
    return root


def createLevel(parentNode, createdNodes, maxDepth):
    if parentNode.turnCount >= maxDepth:
        return
    
    number = parentNode.data
    if number >= 1200:
        return
    
    nodes = [TreeNode(number * 2, parentNode.turnCount + 1),
             TreeNode(number * 3, parentNode.turnCount + 1),
             TreeNode(number * 4, parentNode.turnCount + 1)]

    for node in nodes:
        node.p1points = parentNode.p1points
        node.p2points = parentNode.p2points
        
        addPoints(node)
        
        print(f"Mezgls {node.data} (P1: {node.p1points}, P2: {node.p2points}) ID: {id(node)}") # to var nokomentēt, tas tikai priekš self pārbaudei

        if node not in createdNodes:
            parentNode.addChild(node)
            createdNodes.add(node)
            createLevel(node, createdNodes, maxDepth)
        else:
            for existing_node in createdNodes:
                if existing_node == node:
                    parentNode.addChild(existing_node)
                    print(f"Mezgls {node.data} (P1: {node.p1points}, P2: {node.p2points}) jau eksistē, ID: {id(existing_node)}") # tas arī
                    break


def addPoints(node):
    if node.turnCount % 2 == 1:
        if node.data % 2 == 0:
            node.p2points -= 1
        else:
            node.p1points += 1
    else:
        if node.data % 2 == 0:
            node.p1points -= 1
        else:
            node.p2points += 1


def printTree(root):
    for node in root.children:
        print("--" * node.turnCount + ">" + str(node.data) + f" (P1: {node.p1points}, P2: {node.p2points})")
        printTree(node)


if __name__ == '__main__':
    Tree = buildTree(8)
    # īslaicīgi, lai ģenerētu citā līmenī tālāk
    # TODO pievienot normālu risinājumu
    Tree.children[0].children[0].children[0].turnCount = 0
    createLevel(Tree.children[0].children[0].children[0], set(), 3)

    printTree(Tree)
