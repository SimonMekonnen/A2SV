class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = Counter(nums)
        arr = [0 for i in range(max(nums) + 1)]
        arr[1] = nums[1]
        for i in range(2,len(arr)):
            arr[i] += max(nums[i] * i + arr[i - 2],arr[i - 1])
        return max(arr)
        
        