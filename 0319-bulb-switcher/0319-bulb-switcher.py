class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        This problem is similar to good old hazarduari problem
        Bulbs that are visited odd number of times would stay on at the end
        Bulbs that are operated even number of times would stay off at the end
        So, the numbers which have odd number of divisors are visited odd number of times
        Only perfect squares have odd number of visitors
        """
        if n == 0: return 0
        if n == 1: return 1
        squares = 0
        for i in range(1,n+100):
            if i*i<=n:
                squares = squares + 1
            else:
                break
        return squares
            