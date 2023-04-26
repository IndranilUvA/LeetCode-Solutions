class Solution:
    def addDigits(self, num: int) -> int:
        """
        Tricky: if number is divisible by 9 answer is always 9
        else answer is remainder when num is divided by 9
        """
        if num == 0: return 0
        return 9 if num%9 == 0 else num%9
        