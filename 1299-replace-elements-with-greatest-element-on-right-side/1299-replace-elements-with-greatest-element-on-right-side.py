class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stk = []
        for i in range(1, len(arr)):
            
            while stk and arr[i] > arr[stk[-1]]:
                stk.pop()
                
            stk.append(i)
        k = 0    
        for i in range(len(arr) - 1):
            if i >= stk[k]:
                k+=1
            arr[i] = arr[stk[k]] 
        arr[-1] = -1 
        return arr
        