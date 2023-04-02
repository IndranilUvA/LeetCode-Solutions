import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Sort the potions
        for each element in spells, find index in potion
        such that all elements after that index is more than success/i
        That would be the number we append in ans array
        """
        potions.sort()
        ans = []
        for i in spells:
            target = success/i
            index = bisect.bisect_left(potions, target)
            ## all numbers right to index should be considered
            ans.append(len(potions) - index)
        return ans
            
        