class Node:
    def __init__(self,val=0):
        self.val = val
        self.right = None
        self.left = None


def Kth_smallest(root ,k):
    stack = []
    node = root
    count = 0

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        count +=1

        if count == k:
            return node.val
        
        node = node.right
    return None

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right =Node(4)
root.left.left.left =Node(1)

res= Kth_smallest(root , 1)
print(res)
