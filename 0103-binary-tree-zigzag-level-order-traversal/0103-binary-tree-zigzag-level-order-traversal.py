# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def reverse(self, nums):
        return nums[::-1]
        
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        levels = []
        ans = []

        while q:
            for node in q:
                q=q[1:]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                levels.append(node.val)
            print(levels)
            ans.append(levels)
            levels = []
            
        ans2 = []
        for i,j in enumerate(ans):
            if i%2 == 1:
                ans2.append(j[::-1])
            else:
                ans2.append(j)
        return ans2
        
        