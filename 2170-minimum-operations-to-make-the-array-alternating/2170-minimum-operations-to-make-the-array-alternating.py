class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        odd = defaultdict(int)
        even = defaultdict(int)
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)):
            if i % 2:
                odd[nums[i]] += 1
            else:
                even[nums[i]] += 1
        
        odd = [(value,key) for key,value in odd.items()]
        even = [(value,key) for key,value in even.items()]
        
        odd.sort(reverse  = True)
        even.sort(reverse = True)
        n = len(nums)
        o = n // 2
        e = -(-n // 2)
        if odd[0][1] != even[0][1]:
            return o - odd[0][0] + e - even[0][0]
        else:
            if len(odd) > 1 and len(even) > 1:
                return min(o - odd[0][0] + e - even[1][0] , o - odd[1][0] + e - even[0][0])
            elif len(odd) == 1 and len(even) == 1:
                return min(odd[0][0] , even[0][0])
            elif len(odd) == 1:
                return min(odd[0][0] + e - even[0][0], e - even[1][0])
            else:
                return min(even[0][0] + o - odd[0][0], o - odd[1][0])
                
        