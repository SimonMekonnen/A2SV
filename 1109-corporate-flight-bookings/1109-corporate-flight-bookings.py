class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre = [0] * n
        for first,last,re in bookings:
            pre[first-1]+=re
            if last < len(pre):
                pre[last]-=re
        for i in range(1,len(pre)):
            pre[i]+=pre[i-1]
        return pre
        
        