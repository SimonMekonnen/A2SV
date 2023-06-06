class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = set()
        def bt(index,arr):
            if len(arr) == len(nums):
                ans.add(tuple(arr))
                return 
            
            for i in range(len(nums)):
                if i!= index and nums[index] not in arr:
                    bt(i,arr + [nums[index]]) 
            
        for i in range(len(nums)):
            bt(i,[])
        return ans
                
        