class Solution:
    
    def cal_power(self, num):
        ans = 0
        while num>1:
            if num%2 == 0:
                num = num//2
                ans = ans + 1
            else:
                num = 3*num + 1
                ans = ans + 1
        return ans
        
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        temp = [[num, self.cal_power(num)] for num in range(lo,hi+1)]
        temp.sort(key = lambda x: x[1]) 
        return temp[k-1][0]
        