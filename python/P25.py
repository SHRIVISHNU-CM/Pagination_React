class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left  = None

def mirror(root):
    if(root == None):
        return
    
    q = []
    q.append(root)

    while (len(q)):
        curr = q[0]
        q.pop(0)

        curr.left, curr.right = curr.right , curr.left

        if (curr.left):
            q.append(curr.left)
        if (curr.right):
            q.append(curr.right)
def  inorder(root):
    if(root == None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


root = Node(1)
root.left  = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("original")
inorder(root)

mirror(root)
print("Mirror")
inorder(root)


