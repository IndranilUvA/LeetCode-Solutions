class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        This is a mind blowing solution:
        let's say the function is f
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        now, f(matrix) = matrix[0] + f[[6,9], [5,8], [4,7]]
        so, we fist traverse the first row, then next we transpose and reverse it
        Motivation from: https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
        
        """
        if len(matrix) == 1:
            return matrix[0]
        temp = [list(i) for i in zip(*matrix[1:])]
        temp.reverse()
        return matrix[0] + self.spiralOrder(temp)
        