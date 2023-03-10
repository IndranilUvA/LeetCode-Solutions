# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums, level = [] , []
        next_level = []
        q = [root]
        while q:
            for node in q:
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            q = next_level
            next_level = []
            level_sums.append(sum(level))
            level = []
        
        if len(level_sums) < k:
            return -1
        level_sums.sort(reverse = True)
        return level_sums[k-1]
        
                
        