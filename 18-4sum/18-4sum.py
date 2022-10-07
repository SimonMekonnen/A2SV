class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    tsum = nums[i] + nums[j] + nums[left] + nums[right]
                    if tsum > target:
                        right -= 1
                    elif tsum < target:
                        left += 1
                    else:
                        ans.add((nums[i], nums[j], nums[left],nums[right]))
                        left+=1
                        right-=1

        return ans
        