class TreeNode:
    def __init__(self, startingNumber, depth=0):
        # Koka sākotnējais cipars, ar ko sākas spēle
        self.gameNum = startingNumber
        # Mezgla priekšteči
        self.parent = None
        # Mezgla pēcteči
        self.children = []
        # Spēlētāju punkti
        self.p1points = 0
        self.p2points = 0
        # Esošais dziļuma līmenis, jeb gājienu skaits
        self.turnCount = depth

    # Pievieno klāt pēcteča mezglu
    def addChild(self, node):
        self.children.append(node)

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented
        return (
                self.gameNum == other.gameNum and
                self.p1points == other.p1points and
                self.p2points == other.p2points and
                self.turnCount == other.turnCount
        )

    def __hash__(self):
        return hash((self.gameNum, self.p1points, self.p2points, self.turnCount))

#  Sāk izveidot koku
def buildTree(startNumb, depth=3):
    root = TreeNode(startNumb, 0)
    createdNodes = set()
    createLevel(root, createdNodes, depth) # uzstādīts dzīļums - 3 līmeņi
    return root
"""
    Galvenā fukcija, kura ģenerē koku, pēc nosacījumiem noteiktiem nosacījumiem.
    Tiek izveidots pēcteča mezgls, kuram ir pievienoti spēlētāju iegūtie punkti visos gadījumos
    Mezgls netiek ģenerēts, ja ir sasniegts maksimālais dotais dziļums vai, ja esošais skaitlis pārsniedz 1200.
    Pirms jauna mezgla piešķires tiek pārbaudīts vai jau identisks mezgls eksistē, ja
    eksistē tad piešķir jau eksistējošo mezglu, ja nē tad kokam tiek pievienots jaunais mezgls
"""
def createLevel(parentNode, createdNodes, maxDepth):
    # Pārbaude vai dziļums ir sasniegts
    if parentNode.turnCount >= maxDepth:
        return

    number = parentNode.gameNum
    # Vai esošais skaitlis ir jau lielāks par 1200
    if number >= 1200:
        return

    # Ģenerē 3 dažādos variantus
    nodes = []
    for i in range(2,5):
        nodes.append(TreeNode(number * i, parentNode.turnCount + 1))

    # Iziet cauri veidotajiem mezgliem
    for node in nodes:
        node.p1points = parentNode.p1points
        node.p2points = parentNode.p2points
        
        addPoints(node)
        
        print(f"Mezgls {node.gameNum} (P1: {node.p1points}, P2: {node.p2points}) ID: {id(node)}") # to var nokomentēt, tas tikai priekš self pārbaudei

        # Pārbaude vai jau pirmstam ir veidots tāds mezgls, ja nav tad veido jaunu
        if node not in createdNodes:
            parentNode.addChild(node)
            createdNodes.add(node)
            createLevel(node, createdNodes, maxDepth)
        # Ja ir tad atrod to un pievieno eksistējošo un nav nepieciešam ģenerēt
        else:
            for existing_node in createdNodes:
                if existing_node == node:
                    parentNode.addChild(existing_node)
                    print(f"Mezgls {node.gameNum} (P1: {node.p1points}, P2: {node.p2points}) jau eksistē, ID: {id(existing_node)}") # tas arī
                    break

# Sistēma kā pievieno punktus vai atņem spēlētājiem spēles laikā.
def addPoints(node):
    if node.turnCount % 2 == 1:
        if node.gameNum % 2 == 0:
            node.p2points -= 1
        else:
            node.p1points += 1
    else:
        if node.gameNum % 2 == 0:
            node.p1points -= 1
        else:
            node.p2points += 1

# ģenerē no dota node noteiktā dziļumā tālāk koku
def generateLevel(node, depth):
    createLevel(node, set(), node.turnCount+depth)


def printTree(root):
    for node in root.children:
        print("--" * node.turnCount + ">" + str(node.gameNum) + f" (P1: {node.p1points}, P2: {node.p2points})")
        printTree(node)


if __name__ == '__main__':
    # Izveido koku ar sākotnējo skaitli
    Tree = buildTree(8)
    # īslaicīgi, lai ģenerētu citā līmenī tālāk
    izveletais = Tree.children[0].children[0].children[0]
    generateLevel(izveletais, 3)

    printTree(Tree)
