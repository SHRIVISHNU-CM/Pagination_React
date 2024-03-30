# class Node:
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.data = data

# ##insertion
        
# def inserBST(self,key):
#     if root is None:
#         return Node(key)
#     else: 
#         if root.data == key:
#             return root
        
#         elif root.data <key:
#             root.right = inserBST(root.right, key)
#         else:
#             root.left  =inserBST(root.left,key)

#     return root

# #inorder traversel 

# def inorder(root):
#     if root:
#         ## recursice call
#         inorder(root.left)
#         print(root.data)
#         ## recursive right
#         inorder(root.right)


# ##driver code
# root  =Node(100)
# root = inserBST(root,80)
# root  = inserBST(root,110)
# root = inserBST(root,50)
# root = inserBST(root,90)

# print("inorder traversal")


## Method Definition
def finduniqueBST(n):
    n1, n2, sum_Val = 0, 0, 0
    ## Base case condition
    if n == 0 or n == 1:
        return 1
    
    ## Catalan number series
    for i in range(1,n+1):
        n1 = finduniqueBST(i-1)
        n2 = finduniqueBST(n-i)
        sum_Val += n1*n2
    return sum_Val

## Driver code
## n indicates the number of nodes in the BST(unique)
n = 8
result = finduniqueBST(n)
print("Number of unique possible BST", result)