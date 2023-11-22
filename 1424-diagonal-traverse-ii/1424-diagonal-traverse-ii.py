class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        arr  = []
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                arr.append((i + j , -i,nums[i][j]))
        
        arr.sort()
        return [i[2] for i in arr]
                