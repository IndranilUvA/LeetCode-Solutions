# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def symmetric(self, left, right):
        """
        Given two tree nodes, it return True if they are symmetric
        """
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val and self.symmetric(left.right, right.left) and self.symmetric(right.right, left.left):
            return True
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric(root.left, root.right)
        
        
        