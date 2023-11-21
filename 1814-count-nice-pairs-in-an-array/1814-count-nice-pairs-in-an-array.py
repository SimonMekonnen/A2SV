class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0  
        for i in nums:
            s = list(str(i))
            s.reverse()
            s = "".join(s)
            s = int(s)
            ans += dic[i - s]
            dic[i - s] += 1
        return ans % (10 ** 9 + 7)
        
        
       