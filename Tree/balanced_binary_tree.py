# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Explanation:
# 1. We first find the height of the tree using a recursive function sol.
# 2. We then check if the height of the left and right subtree is not greater than 1.
# 3. If it is greater than 1, we return False.
# 4. If it is not greater than 1, we return True.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def sol(node):
            if node==None:
                return 0
            l = 1+sol(node.left)
            r = 1+sol(node.right)
            return max(l,r)
        
        ans = sol(root)
        def trav(node):
            if node==None:
                return True
            if node.val>1:
                return False
            return trav(node.left) and trav(node.right)
        
        return trav(root)
        