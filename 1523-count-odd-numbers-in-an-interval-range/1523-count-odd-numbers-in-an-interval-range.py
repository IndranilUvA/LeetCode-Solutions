class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Number of odds before n(excluding) is n//2
        """
        return (high+1)//2 - low//2