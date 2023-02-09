class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        left = 0
        ans = 0
        i = 0
        for right in range(len(nums)): 
            table[nums[right]]+=1
            while len(table) > k:
                table[nums[left]]-=1
                if table[nums[left]] == 0:
                    del table[nums[left]]
                    i = left + 1
                left+=1
            ans += right - left + 1
        anss = 0
        left = 0
        table = defaultdict(int)
        for right in range(len(nums)): 
            table[nums[right]]+=1
            while len(table) >= k:
                table[nums[left]]-=1
                if table[nums[left]] == 0:
                    del table[nums[left]]
                    i = left + 1
                left+=1
            anss += right - left + 1
   
        return ans - anss

        