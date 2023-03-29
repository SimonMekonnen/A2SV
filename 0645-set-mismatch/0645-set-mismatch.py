class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] > len(nums) or nums[nums[i] - 1] == nums[i]:
                    if nums[nums[i] - 1] == nums[i] and  not ans:
                        ans.append(nums[i])
                    break
                nums[nums[i] - 1] ,nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i + 1)
                
    
        return ans
            
        