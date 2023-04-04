class Solution:
    def partitionString(self, s: str) -> int:
        ans= 0
        temp_set = set()
        for i in range(len(s)):
            if s[i] not in temp_set:
                temp_set.add(s[i])
            else:
                temp_set = set()
                temp_set.add(s[i])
                ans = ans + 1
        ans = ans + 1
        return ans
        