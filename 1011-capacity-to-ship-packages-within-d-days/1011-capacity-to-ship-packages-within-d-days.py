class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low<high:
            mid = (low+high)//2
            total = 0
            result = 1
            
            for i in weights:
                if total + i > mid:
                    result = result + 1
                    total = i
                else:
                    total = total + i
                    
            if result <= days:
                high = mid
            else:
                low = mid + 1
                
        return low

        
        
        