class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        total = 0
        for i in nums:
            if i%2 == 0:
                total += i

        ans = []
        for v,i in queries:
            
            total -= nums[i] if nums[i]%2 == 0 else 0
            
            total += (nums[i] + v) if (nums[i] + v)%2 == 0 else 0
            
            nums[i]+=v
            
            ans.append(total)
            
        return ans
            
            
        