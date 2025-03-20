class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        self.p1points = 0
        self.p2points = 0
        self.turnCount = 0

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
    root = TreeNode(startNumb)
    createdNodes = set()
    createLevel(root, createdNodes) 
    return root

def createLevel(parentNode, createdNodes):
    number = parentNode.data
    if number >= 1200:
        return
    
    nodes = [TreeNode(number * 2), TreeNode(number * 3), TreeNode(number * 4)]

    for node in nodes:
        node.p1points = parentNode.p1points
        node.p2points = parentNode.p2points
        node.turnCount = parentNode.turnCount + 1

        addPoints(node)
        
        print(f"Mezgls {node.data} (P1: {node.p1points}, P2: {node.p2points}) ID: {id(node)}")

        if node not in createdNodes:
            parentNode.addChild(node)
            createdNodes.add(node)
            createLevel(node, createdNodes)
        else:
            print(f"Mezgls {node.data} (P1: {node.p1points}, P2: {node.p2points}) jau eksistē")

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
        print("--"*node.turnCount + ">" + str(node.data)+ f" (P1: {node.p1points}, P2: {node.p2points})")
        printTree(node)

def printFinalNodes(root):
    def traverse(node, visited):
        if node in visited:
            return
        visited.add(node)
        
        if not node.children:
            print("--" * node.turnCount + ">" + str(node.data) + f" (P1: {node.p1points}, P2: {node.p2points})")
        
        for child in node.children:
            traverse(child, visited)
    
    traverse(root, set())

if __name__ == '__main__':
    Tree = buildTree(8)
    printTree(Tree)
    print("\nFinal Nodes:")
    printFinalNodes(Tree)

