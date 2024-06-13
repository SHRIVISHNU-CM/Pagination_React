class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def maxdepth (root):
    if root is None:
        return 0 
    else:
        ldepth = maxdepth(root.left)
        rdepth = maxdepth (root.right)
        if (ldepth>rdepth):
            return ldepth+1
        else:
            return rdepth+1


root = Node(10)
root.left =Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right =Node(5)

print("height of tree" , maxdepth(root))