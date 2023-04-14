class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        """
        This problem is similar to LC 1143
        Finding longest common substring
        We find the longest common substring between s and rev_s
        That way we also make sure that the common string is a palindrome
        Mind == Blown
        """
        
        if len(s) == 1:
            return 1
        rev_s = s[::-1]
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if s[i] == rev_s[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]
        