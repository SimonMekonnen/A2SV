class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
          i = len(arr) - 1
          m = -1
          while i >= 0:
                c = arr[i]
                arr[i] = m
                if c > m:
                    m = c
                i-=1
          return arr
            