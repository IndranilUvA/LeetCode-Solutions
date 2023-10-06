class Solution:
    def integerBreak(self, n: int) -> int:
        """
        We use DP. We know the answer is 1 for n=1 and 1 for n=2
        Create a DP dictionary. We know that for any n, we can atleast have n.
        Meaning, when 17 = 10+7, we know the contribution from 10 is atleast 10. 
        So, we initiate DP dictionary with the corresponsing number, for 
        Now, for every element from 2,3,...,n, we traverse
        We traverse again from 1 to that number to find that maximum product distribution. 
        It is important for the DP dictionary to keep value 0 or 1 for the question input: n
        For example, when n=3, the answer is 2 (1+2), but when 3 is contributed in some other big sum,
        it should contribute atleast 3.
        """
        
        if n == 1 or n == 2: return 1
        
        dp = {i:i for i in range(1, n+1)}
        dp[n] = 0
        
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[j]*dp[i-j], dp[i])
        
        return dp[n]
                
        