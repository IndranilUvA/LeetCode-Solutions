class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1), len(word2)
        index1, index2 = 0,0
        ans = ""
        while index1<=m-1 or index2<=n-1:
            if index1 == m and index2<=n-1:
                ans = ans + word2[index2]
                index2 = index2+1
            elif index1<=m-1 and index2 == n:
                ans = ans + word1[index1]
                index1 = index1+1
            else:
                ans = ans + word1[index1] + word2[index2]
                index1, index2 = index1+1, index2+1
        return ans
    
        
