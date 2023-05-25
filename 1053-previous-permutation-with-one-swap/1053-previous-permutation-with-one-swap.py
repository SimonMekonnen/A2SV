class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        toswap = None
        while i >= 0:  
            if arr[i] > arr[i + 1]:
                toswap = i 
                break
            i -= 1
        if toswap == None:
            return arr
        
        j = len(arr) - 1
        ans = -float("inf")
        another = -1
        while j > toswap:  
            if arr[j] >= ans and arr[j] < arr[toswap]:
                ans = arr[j]
                another = j
            j -= 1
        if another != -1:
            arr[toswap],arr[another] = arr[another],arr[toswap]  
        return arr
        
        