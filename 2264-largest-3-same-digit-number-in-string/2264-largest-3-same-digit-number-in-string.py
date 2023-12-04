class Solution:
    """
    We start with 000 and check every three length subsequence and keep comparing.
    We also keep track of ever, if there is no subsequqnce then ever is going to be False and we return ""
    """
    def largestGoodInteger(self, num: str) -> str:
        ans = "000"; ever = False
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                temp = num[i]*3
                ever = True
                if int(temp)>int(ans):
                    ans = temp
                    
        return ans if ever else ""
        