class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ans = []
        def helper(arr):
            nonlocal ans
            if len(arr) == 1:
                return 
            ans.append(arr.index(len(arr)) + 1)
            ans.append(len(arr))
            c = arr[arr.index(len(arr)) + 1:]
            c.reverse()
            newarr = c + arr[0 :arr.index(len(arr)) ]
            helper(newarr)
        helper(arr)
        return ans
    
            
        
        
        
      
        