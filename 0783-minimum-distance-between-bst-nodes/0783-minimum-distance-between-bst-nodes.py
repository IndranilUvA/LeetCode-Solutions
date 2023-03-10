# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    
    ### inorder traversal would return the sorted array as the tree is a BST ###
    ### Next, we just check the differences between two consecutive numbers in the array ###
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        temp = self.inorder(root)
        ans = float("inf")
        for i in range(len(temp) - 1):
            ans = min(ans, abs(temp[i+1] - temp[i]))
        return ans
        
        
        