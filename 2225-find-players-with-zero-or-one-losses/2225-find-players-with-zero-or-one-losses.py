class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        ans = [[],[]]
        dic = defaultdict(int)

        for i in matches:
            dic[i[1]]+=1
        
        for i in matches:
            if dic[i[0]] == 0:
                ans[0].append(i[0])
            if dic[i[1]] == 1:
                ans[1].append(i[1]) 
        for i in range(len(ans)):
            ans[i] = list(set(ans[i]))
            ans[i].sort()
        return ans
        