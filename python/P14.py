class Node:
    def __init__(self , key):
        self.key = key
        self.left = None
        self.right = None

def insert (root,key):

    #if tree is empty
    if root is None:
        return Node(key)
    
    if key < root.key:
        root.left = insert(root.left,key)

    elif key > root.key:
        root.right = insert(root.right,key)

    return root

def search(node , key):
    if node is None or node.key == key:
        return node
    
    if node.key < key:
        return search(node.right , key)
    
    return search(node.left , key)


root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)


key = 60

if search(root,key) is None:
    print("Not found")

else:
    print("found", key)