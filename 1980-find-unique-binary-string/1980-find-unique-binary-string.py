class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        def bt(s):
            if len(s) > len(nums):
                return ""
            if len(s) == len(nums):
                if s not in nums:
                    return s
                
            zero = bt(s + "0")
            one = bt(s + "1")
            if zero:
                return zero
            if one:
                return one
        return bt("")
       
        