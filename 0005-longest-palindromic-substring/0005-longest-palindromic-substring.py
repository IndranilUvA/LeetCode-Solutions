class Solution:
    """
    We would chacke the palindroms from the centre and expand in both sides from there
    There are two options, if the palindrome is of odd length, then we just from from centr position i
    If the palindrome is od even length, we start from i and i+1th position
    we create a function palindrome, from the centre: left and right are just the centre positions
    For odd length both would be same, for even they are just i and i+1
    """
    
    def palindrome(self, s, left, right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left, right = left-1, right+1
        
        ## note that, but the time while loop ends, s[left] and s[right] are different, so we take the prev index
        ## or maybe left is -1 or right is len(s), so we move to the prev index
        return s[left+1: right]
    
    
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0; ans = ""
        
        for i in range(len(s)):
            odd_option = self.palindrome(s, i, i)
            even_option = self.palindrome(s, i, i+1)
            
            if len(odd_option)>len(even_option) and len(odd_option)>maxLen:
                ans = odd_option
                maxLen = len(odd_option)
            
            if len(even_option) > len(odd_option) and len(even_option)>maxLen:
                ans = even_option
                maxLen = len(even_option)
        
        return ans
        
        