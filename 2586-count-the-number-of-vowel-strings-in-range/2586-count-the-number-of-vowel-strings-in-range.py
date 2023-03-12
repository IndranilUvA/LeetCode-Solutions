class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        for i in range(left, right+1):
            word = words[i]
            if word[0] in set("aeiou") and word[-1] in set("aeiou"):
                ans = ans + 1
        return ans
        