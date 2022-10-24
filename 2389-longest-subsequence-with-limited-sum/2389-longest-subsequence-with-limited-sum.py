class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in queries:
            total = 0
            j = 0
            while total <= i and j < len(nums):
                total+=nums[j]
                j+=total<= i
            ans.append(j)
        return ans
                    
                    
        
        