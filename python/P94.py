class TreeNode:
    def __init__(self,val = 0, left =None,right = None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    
    left = max_depth(root.left)
    right = max_depth(root.right)

    return 1+max(left,right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

print(max_depth(root))
