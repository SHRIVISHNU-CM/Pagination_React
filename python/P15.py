class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(temp):
    if (not temp):
        return
    inOrder(temp.left)
    print(temp.data , end = " ")
    inOrder(temp.right)

def deleteDeepest (root , d_node):
    q= []
    q.append(root)

    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp  = None
        if temp.right:
            if temp.right is d_node:
                temp.right = None
            else:
                q.append(temp.right)

        if temp.left :
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def deletion(root,key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    q = []
    q.append(root)
    temp = None
    k_node = None

    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            k_node = temp
        if temp.left :
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    
    if k_node:
        x = temp.data
        k_node.data = x
        deleteDeepest(root,temp)
    return root



root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.left.right = Node(12)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

print ("before" , end = " ")
inOrder(root)
key = 11
print()
root = deletion(root,key)
print("after",end=" ")

inOrder(root)