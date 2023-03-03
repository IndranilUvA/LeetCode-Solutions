class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        First non-nine digit to 9 for making it maximum
        First non-zero digit to 0 for making it minimum
        """
        num_list = [int(i) for i in str(num)]
        first_non_zero_index = 0
        for i,j in enumerate(num_list):
            if j!=0:
                first_non_zero_index = i
                break
                
        first_non_nine_index = 0
        for i,j in enumerate(num_list):
            if j!=9:
                first_non_nine_index = i
                break
        
        remap_max = {num_list[first_non_nine_index]:9}
        remap_min = {num_list[first_non_zero_index]:0}
        
        num_max = int("".join([str(remap_max[i]) if i in remap_max else str(i) for i in num_list]))
        num_min = int("".join([str(remap_min[i]) if i in remap_min else str(i) for i in num_list]))
        
        return num_max-num_min
                