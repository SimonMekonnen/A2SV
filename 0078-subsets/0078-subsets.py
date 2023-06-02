class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def bt(index,arr):
            ans.add(tuple(arr))
            if index >= len(nums):
                return
            bt(index + 1 , arr)
            bt(index + 1,arr + [nums[index]])
        bt(0,[])
        return ans
        