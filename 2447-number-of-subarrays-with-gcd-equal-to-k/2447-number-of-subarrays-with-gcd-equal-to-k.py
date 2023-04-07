class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        ans = 0
        for i in range(len(nums)):
            now = nums[i]
            for j in range(i,len(nums)):
                now = gcd(now,nums[j])
                if now == k:
                    ans += 1
                if now < k:
                    break
    
        return ans
                
        