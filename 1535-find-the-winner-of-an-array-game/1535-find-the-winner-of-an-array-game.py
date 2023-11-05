class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        cur = arr[0]
        count = 0
        t = max(arr)
        for i in range(1,len(arr)):
            opp = arr[i]
            if cur > opp:
                count += 1
            else:
                count = 1
                cur = opp
            
            if count == k or cur == t:
                return cur
        