class Solution:
    def minInsertions(self, s: str) -> int:
        """
        This problem can be seen as a follow-up of two other problems
        LC 1143: Finding longest common sub-sequence of two strings a and b
        LC 516: Longest Palindromic subsequence
        Trick is that if we consider s and revers_s and find the longest common substring
        between these two, we find the subsequnce in s that is longest palindrome.
        Now, the other characters can be just inserted in the required place to make the 
        full string palindrome, so the count of rest of the characters would be the answer
        """
        
        rev_s, n = s[::-1], len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if s[i] == rev_s[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        temp = dp[-1][-1] ## This gives the longest palindromic subsequence in s
        return n - temp