class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp=int("".join([str(i) for i in num]))
        temp=temp+k 
        temp=str(temp)
        return [int(i) for i in temp]