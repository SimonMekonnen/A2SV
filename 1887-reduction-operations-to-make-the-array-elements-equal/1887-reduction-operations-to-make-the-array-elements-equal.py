class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        
        ans = [0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                ans.append(ans[-1])
            else:
                ans.append(ans[-1] + 1)
                
        return sum(ans)