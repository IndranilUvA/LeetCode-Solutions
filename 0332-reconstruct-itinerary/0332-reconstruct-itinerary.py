class Solution:
    
    """
    This is a classic DFS problem. We first create the graph dictionary
    Next, we sort the valu lists of dictionary in reverse lexicography, as eventually we reverse the ans
    Now, we start with JFK in stack
    Now, from JFK we go to the next node (worst lexical one) and the next one and so on and 
    every time we append into stack and remove the element from the graph dictionary values
    Now, once we are done and can not go further (depth), we append the last element from stack.
    We do that untill the stack is empty
    Note that the JFK would be inserted at the last in the answer.
    We finally return the reversed ans
    """
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        
        for i,j in tickets:
            if i in graph:
                graph[i].append(j)
            if i not in graph:
                graph[i] = [j]
                
        for source, destinations in graph.items():
            graph[source].sort(reverse = True)
            
        stack = ["JFK"]
        ans = []
        
        while stack:
            curr = stack[-1]
            if curr in graph and len(graph[curr])>0:
                next_node = graph[curr].pop()
                stack.append(next_node)
            else:
                ans.append(stack.pop())
                
        return ans[::-1]
        