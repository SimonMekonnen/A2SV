class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        arr1 = []
        arr2 = []
        arr3 = []
        for i in nums:
            if i > pivot:
                arr2.append(i)
            
            elif i == pivot:
                arr3.append(i)
            
            else:
                arr1.append(i)
                
        return arr1 + arr3 + arr2
            
            
        