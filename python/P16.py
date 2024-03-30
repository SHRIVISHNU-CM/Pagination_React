class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def diagonalSum(root, diagonal , d):
    if root is None:
        return
    d[diagonal] = d.get(diagonal,0) + root.data
    diagonalSum(root.left,diagonal+1, d)
    diagonalSum(root.right, diagonal,d)


def printDiagonalSum(root):
    d = {}
    diagonalSum(root, 0 , d)
    print(list(d.values()))




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

printDiagonalSum(root)