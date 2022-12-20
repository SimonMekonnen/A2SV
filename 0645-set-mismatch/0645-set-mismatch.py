class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0] * (len(nums)+1)
        for i in nums:
            count[i]+=1
        ans = []
        for i in range(1,len(count)):
            if len(ans) == 2:
                break
            if count[i] == 2:
                ans.append(i)
            if count[i] == 0:
                ans.append(i)
        if count[ans[0]] != 2:
            ans[0],ans[1] = ans[1],ans[0]
        return ans
    
            
        