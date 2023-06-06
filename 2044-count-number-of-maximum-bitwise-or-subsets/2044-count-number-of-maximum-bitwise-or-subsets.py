class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        bit = 0
        for i in nums:
            bit |= i
        count = 0
        def bt(index, o):
            nonlocal count
            if index >= len(nums):
                return
            c = o | nums[index]
            if c == bit:
                count += 1
            bt(index + 1,c)
            bt(index + 1,o)
        bt(0,0)
        return count
        