from collections import deque
class Solution:
    def ifsimilar(self, s1, s2):
        n, count = len(s1), 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count = count + 1
                if count >2 :
                    return False
        if count == 2 or count == 0:
            return True
        else:
            return False
    
    def graph(self,strs):
        graph_dict = {}
        for i in range(len(strs)):
            if strs[i] in graph_dict:
                continue
            else:
                graph_dict[strs[i]] = []
                for j in range(len(strs)):
                    if j!=i:
                        if self.ifsimilar(strs[i],strs[j]):
                            graph_dict[strs[i]].append(strs[j])
                        
        return graph_dict
    
    def numSimilarGroups(self, strs: List[str]) -> int:
        graph_dict = self.graph(strs)
        ans = 0
        visited = set()
        for i in strs:
            if i not in visited:
                q = deque([i])
                while q:
                    curr_node = q.popleft()
                    for ne in graph_dict[curr_node]:
                        if ne not in visited:
                            q.append(ne)
                            visited.add(ne)
                ans = ans+1
        return ans
        