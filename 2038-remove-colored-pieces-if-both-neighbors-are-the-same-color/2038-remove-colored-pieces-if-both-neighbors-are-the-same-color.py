class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        We count number of AAAs ans number of BBBs in the string
        If AAAs are more then A wins, else B wins
        example: AAAAAAAA: has 8 As, hence 6 AAAs
        """
        
        num_AAAs, num_BBBs = 0, 0
        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i] == colors[i+1] and colors[i] == "A":
                num_AAAs = num_AAAs+1
            if colors[i-1] == colors[i] == colors[i+1] and colors[i] == "B":
                num_BBBs = num_BBBs+1
        
        return num_AAAs>num_BBBs
        