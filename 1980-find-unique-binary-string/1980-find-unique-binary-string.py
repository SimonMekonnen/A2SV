class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        def bt(s):
            if len(s) > len(nums):
                return 
            if len(s) == len(nums):
                if s not in nums:
                    ans.append(s)
            
            zero = bt(s + "0")
            one = bt(s + "1")
        
        bt("")
        return ans[0]
        