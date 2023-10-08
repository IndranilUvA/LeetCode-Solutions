class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """
        This problem is similar to lowest common substring
        We create a DP matrix with m+1 rows and n+1 columns
        where m and n are length of nums1 and nums2 respectively.
        Now, we populate the DP matix such that DP[i][j] is the answer till ith index of nums1 and jth indes of nums2
        Note that, it is easier to code with one extra row and column in DP matrix
        After the end of the loop, the first row and column would always have -inf values
        since we start with -inf in all cells of DP matrix.
        The recurssion is simple. dp[i][j] = max(dp[i-1][j-1] + v1*v2, v1*v2, dp[i-1][j], dp[i][j-1])
        The current v1*v2 can also be a candidate, so we keep that. and comapre with the surroundings
        Another candidate is answer till i-1 and j-1 and adding v1*v2
        """
        m, n = len(nums1), len(nums2)
        dp = [[-float("inf")]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                v1, v2 = nums1[i-1], nums2[j-1]
                dp[i][j] = max(dp[i-1][j-1] + v1*v2, v1*v2, dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        
        