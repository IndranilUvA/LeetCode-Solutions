class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for index, scores in enumerate(grid):
            if sum(scores) == n-1:
                return index
        