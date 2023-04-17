class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index_ans, count = 0, 0
        for index, row in enumerate(mat):
            tot = sum(row)
            if tot>count:
                index_ans, count = index, tot
        return [index_ans, count]
                
        