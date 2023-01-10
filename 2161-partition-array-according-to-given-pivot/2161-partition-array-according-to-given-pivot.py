class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        arr1 = []
        count = 0 
        for i in nums:
            if i < pivot:
                arr1.append(i)
            
            elif i == pivot:
                count += 1
                
        arr1 += ([pivot] * count)  
        
        for i in nums:  
            if i > pivot:
                arr1.append(i)
                
        return arr1
            
            
        