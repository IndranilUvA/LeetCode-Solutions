class Solution:
    
    def sumofseven_cons(self, start):
        """
        Computes the sum of 7 consecutive integers starts with start
        """
        
        return 7*(start + start+6)//2
        
    def totalMoney(self, n: int) -> int:
        if n<=7:
            return n*(n+1)//2
        
        q,r = n//7, n%7
        
        ans = 0
        
        ## IN last r days. the amount will start from q+1
        
        for i in range(q+1, q+1+r):
            ans = ans + i
            
        print(ans)
            
        ## For every q weeks, it start with 1, 2, ..., q amount
        
        week = 1
        
        while week<=q:
            ans = ans + self.sumofseven_cons(week)
            week = week + 1
        return ans
        
        
        