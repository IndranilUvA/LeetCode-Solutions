class Solution:
    """
    We just define a function that calculates the distance between two points and then we add them pairwise in order in the main function.
    """
    def twoptdist(self, p1, p2):
        xmove, ymove = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
        return max(xmove, ymove)
    
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            p1, p2 = points[i-1], points[i]
            ans = ans + self.twoptdist(p1, p2)
        
        return ans