class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        arr = [[growTime[i],plantTime[i]] for i in range(len(growTime))]
        arr.sort(reverse = True)
        ans = 0
        curtime = 0     
        for i in range(len(arr)):
            curtime += arr[i][1]
            ans = max(curtime + arr[i][0],ans)
        
        return ans