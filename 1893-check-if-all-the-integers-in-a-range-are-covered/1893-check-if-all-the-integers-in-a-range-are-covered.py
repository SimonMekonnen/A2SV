class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        i = left
        while i <= right:
            flag = False
            for j in ranges:
                if i >= j[0] and i <= j[1]:
                    flag = True
                    break
            if flag == False:
                return False
            i+=1
        return True
                
                
        