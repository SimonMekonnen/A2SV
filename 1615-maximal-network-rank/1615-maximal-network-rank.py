class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        if roads == []:
            return 0
        for i in roads:
            graph[i[0]].add(i[1])
            graph[i[1]].add(i[0])
        ans = 0
        for i in graph:
            now = len(graph[i])
            for j in graph:
                b = len(graph[j])
                if i != j and now + b - (i in graph[j]) > ans:
                    ans = (now + b - (i in graph[j]))
        return ans
                    
     
        