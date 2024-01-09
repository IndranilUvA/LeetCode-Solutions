# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Given a tree, we first creat e function that produces the list with leaf nodes
    Then we just check if these two lists are ientical or not
    """
    def leaves(self, root):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        return self.leaves(root.left) + self.leaves(root.right)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leaves(root1) == self.leaves(root2)