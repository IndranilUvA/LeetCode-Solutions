class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        This is equivalent to finding maximum number of non-overlapping intervals
        We sort the intervals with respect to end times.
        Then if we have two intervals with end time a and b where a>b, we keep a and discard b
        So that we maximize the number of non-overlapping intervals
        """
        
        intervals.sort(key = lambda x:x[1])
        ans, cutoff = 0, -float("inf")
        for x,y in intervals:
            if x>=cutoff:
                cutoff = y
            else:
                ans = ans + 1
        return ans