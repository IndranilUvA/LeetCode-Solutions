class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        """
        If there is a champion then the champion has no parent. So, we just check if there is one unique node in the graph or not which do not have parent. That's it.
        """
                
        non_champions = set([v for u,v in edges])
        
        if len(non_champions) < n-1: return -1 ## This means there are two nodes with no parent
        
        for i in range(n):
            if i not in non_champions:
                return i