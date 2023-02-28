class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        j = 0
        b = []
        for i in range(len(nums)):
            s+=nums[i]
            if abs(j-i) == k -1:
                b.append(s)
            if abs(j - i) == k:
                s-=nums[j]
                b.append(s)
                j+=1
        return max(b)/k

            
            
        