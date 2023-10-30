class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        arr.sort()
        dp = defaultdict(int)
        for i in arr:
            dp[i] = 1
    
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    dp[arr[i]] += dp[arr[i] // arr[j]] * dp[arr[j]]
                
        ans = 0
        for i in dp:
            ans += dp[i]
        return ans % (10 ** 9 + 7)
      