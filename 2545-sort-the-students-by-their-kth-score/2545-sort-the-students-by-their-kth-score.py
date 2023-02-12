class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        """
        Find the indeces by which the score matrix can be sorted later
        """
        helper_dict = {}
        for index, row in enumerate(score):
            helper_dict[index] = row[k]
        helper_dict = {k:v for k,v in sorted(helper_dict.items(), key = lambda x:x[1], reverse = True)}
        ans = []
        for i in helper_dict.keys():
            ans.append(score[i])
        return ans
        