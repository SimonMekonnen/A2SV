class Solution:
    def sortColors(self, nums: List[int]) -> None:
      i = 0
      j = 1
      while i < len(nums):
        while j < len(nums):
            if nums[j]<=nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
                j+=1
            else:
                j+=1
        j=1
        i+=1
            