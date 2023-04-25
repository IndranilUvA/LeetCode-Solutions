class Solution:
    def rank_list(self, nums):
        """
        Idea: given a list, it gives rank from max to min
        [10,3,8,9,4] --> [1,5,3,2,4]
        sort the list
        [10,9,8,4,3]
        [1,2,3,4,5]
        [1,5,3,2,4]
        
        create a dict = {10:1, ..., 3:5}
        """
        sorted_nums = sorted(nums, reverse = True)
        dict_rank = {}
        for index, j in enumerate(sorted_nums):
            dict_rank[j] = index+1
        
        ranks = []
        for i in nums:
            ranks.append(dict_rank[i])
        return ranks
    
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = self.rank_list(score)
        ans = [str(i) for i in ans]
        for i in range(len(ans)):
            if ans[i] == "1":
                ans[i] = "Gold Medal"
            if ans[i] == "2":
                ans[i] = "Silver Medal"
            if ans[i] == "3":
                ans[i] = "Bronze Medal"
        return ans