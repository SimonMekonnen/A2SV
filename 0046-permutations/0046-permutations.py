class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = set()
        def bt(arr):
            if len(arr) == len(nums):
                ans.add(tuple(arr))
                return 
            
            for i in range(len(nums)):
                if nums[i] not in arr:
                    bt(arr + [nums[i]]) 
            
        bt([])
        return ans
                
        