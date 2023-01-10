class Solution:
    def arrayChange(self, nums: List[int], op: List[List[int]]) -> List[int]:
        
        dic = {}
        
        for i in range(len(nums)):
            dic[nums[i]] = i
            
        for i in op:
            dic[i[1]] = dic[i[0]]
            nums[dic[i[0]]] = i[1]
    
        return nums
            
            
        
       
        
        
        
        
        
        