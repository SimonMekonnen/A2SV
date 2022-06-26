class Solution: 
    def selectionSort(self, arr,n):
        i = 0
        while i < n:
             minimum = i
             j=i
             while j<len(arr):
                if arr[j]< arr[minimum]:
                    minimum = j
                j+=1
             small = arr[minimum]
             arr[minimum]= arr[i]
             arr[i] = small
             i+=1