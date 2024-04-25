# class Node: ###Height of tree
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
# def maxdepth(node):
#         if node is None:
#             return 0
#         else:
#             ldepth = maxdepth(node.left)
#             rdepth = maxdepth(node.right)

#             if(ldepth>rdepth):
#                 return ldepth +1
#             else :
#                 return rdepth +1
            
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left =Node(4)
# root.left.right = Node(5)
# root.left.left.left =Node(6)
# root.left.left.right = Node(7)

# res = maxdepth(root)

# print("heigth of tree", res)


# Python3 program to find closest 
# value in Binary search Tree



# Helper function that allocates a new 
# node with the given data and None 
# left and right pointers.									 
# class newnode: 

# 	# Constructor to create a new node 
# 	def __init__(self, data): 
# 		self.data = data 
# 		self.left = None
# 		self.right = None

# # utility function to return level 
# # of given node
# def getDeepestRightLeafNode(root) :

# 	if (not root):
# 		return None

# 	# create a queue for level 
# 	# order traversal 
# 	q = [] 
# 	q.append(root) 

# 	result = None

# 	# traverse until the queue is empty 
# 	while (len(q)): 
# 		temp = q[0] 
# 		q.pop(0) 

# 		if (temp.left):
# 			q.append(temp.left) 
		
# 		# Since we go level by level, the last 
# 		# stored right leaf node is deepest one 
# 		if (temp.right): 
# 			q.append(temp.right) 
# 			if (not temp.right.left and
# 				not temp.right.right): 
# 				result = temp.right 

# 	return result

# # Driver Code 
# if __name__ == '__main__':
	
# 	# create a binary tree 
# 	root = newnode(1) 
# 	root.left = newnode(2) 
# 	root.right = newnode(3) 
# 	root.left.right = newnode(4)
# 	root.right.left = newnode(5) 
# 	root.right.right = newnode(6)
# 	root.right.left.right = newnode(7)
# 	root.right.right.right = newnode(8)
# 	root.right.left.right.left = newnode(9)
# 	root.right.right.right.right = newnode(10) 

# 	result = getDeepestRightLeafNode(root)
# 	if result:
# 		print("Deepest Right Leaf Node ::",
# 							result.data)
# 	else:
# 		print("No result, right leaf not found")
		
# # This code is contributed by
# # Shubham Singh(SHUBHAMSINGH10)


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def leaf_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val
    return leaf_sum(root.left) + leaf_sum(root.right)

# Example usage:
# Constructing a binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

print("Sum of leaf nodes:", leaf_sum(root))  # Output: 33 (3 + 7 + 18)
