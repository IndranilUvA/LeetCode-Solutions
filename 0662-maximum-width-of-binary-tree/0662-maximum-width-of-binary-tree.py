# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Will try BFS on this, for every node, we create an x-axis value
        when adding left, position would be 2*x and for rightm the position would be 2*x+1
        """
        if not root: return 0
        q = [(root,0)]
        ans = []
        level = []
        dist = 0
        
        while q:
            for r,x in q:
                ans.append(x)
                if r.left:
                    level.append((r.left, 2*x))
                if r.right:
                    level.append((r.right, 2*x+1))
            level_dist = 0
            
            if len(ans)>1:
                level_dist = ans[-1] - ans[0]
            dist = max(dist, level_dist)
            q = level
            level = []
            ans = []
            
        return dist+1