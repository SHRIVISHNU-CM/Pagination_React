class TreeNode:
    def __init__(self,val =0,left= None,right = None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def diameter(self,root):
        self.maximum_diameter = 0
        self.calculator(root)
        return self.maximum_diameter
    def calculator(self,node):
        if not node:
            return 0
        left_height = self.calculator(node.left)
        right_height = self.calculator(node.right)

        self.maximum_diameter = max(self.maximum_diameter,left_height+right_height)

        return max(left_height,right_height) +1

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)


Solution = Solution()
diameter = Solution.diameter(root)

print(diameter)
