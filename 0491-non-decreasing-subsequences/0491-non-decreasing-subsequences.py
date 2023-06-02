class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def bt(index,arr):
            if index >= len(nums):
                return 
            if len(arr) >= 2 and sorted(arr) == arr:
                ans.add(tuple(arr))
            bt(index + 1,arr + [nums[index]])
            bt(index + 1,arr)
        nums.append(nums[-1])
        bt(0,[]) 
        return ans
        