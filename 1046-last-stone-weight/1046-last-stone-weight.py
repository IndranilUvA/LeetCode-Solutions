import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        ans = 0
        while len(stones)>1:
            x = heappop(stones)
            heapq.heapify(stones)
            y = heappop(stones)
            x,y = -x, -y
            if x == y:
                continue
            else:
                z = x-y
                z = -z
                heappush(stones, z)
            ans=ans+1
        
        return -stones[0] if stones else 0