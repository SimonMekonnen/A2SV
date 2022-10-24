class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(nums[i]+pre[-1])
        ans = []
        for i in queries:
            b = -1
            for j in range(len(nums)):
                if pre[j] <= i:
                    b = j
                else:
                    break
            ans.append(b+1)
        return ans
                    
                    
        
        