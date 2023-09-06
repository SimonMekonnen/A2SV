class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int: 
        arr = [[ages[i],scores[i]] for i in range(len(ages))]
        arr.sort()
        for i in range(len(ages)):
            scores[i] = arr[i][1]
            ages[i] = arr[i][0]
        dp = [scores[i] for i in range(len(ages))]
        m = [i for i in range(len(ages))]
        for i in range(len(ages)):
            for j in range(i):
                if ages[i] == ages[m[j]] or scores[m[j]] <= scores[i]:
                    dp[i] = max(dp[i],dp[j] + scores[i])
                    if scores[i] > scores[m[j]]:
                        m[i] = i
                    else:
                        m[i] = m[j]
   
        return max(dp)