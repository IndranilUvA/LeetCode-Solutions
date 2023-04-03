class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        people.sort()
        ans = 0
        first, last = 0, len(people)-1
        while first<=last:
            if people[first] + people[last]<=limit:
                ans = ans + 1
                first = first + 1
                last = last-1
            else:
                ans = ans + 1
                last = last-1
        return ans
        
        