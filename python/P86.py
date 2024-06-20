class TreeNode:
    def __init__(self,val = 0,left=None ,right=None):
        self.val = val
        self.right = right
        self.left = left

def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height,right_height) 

root  = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)

print(height(root))
