class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        count = Counter(nums)
        def bt(arr,dic):
            if len(arr) == len(nums):
                ans.add(tuple(arr.copy()))
                return
            
            for i in range(len(nums)):
                if dic[nums[i]] != count[nums[i]]:
                    dic[nums[i]] += 1
                    bt(arr + [nums[i]],dic)
                    dic[nums[i]] -= 1
                    
        bt([],defaultdict(int))
        return ans