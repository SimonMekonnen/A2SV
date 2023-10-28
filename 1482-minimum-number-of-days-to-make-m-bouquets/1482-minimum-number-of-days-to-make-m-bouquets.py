class Solution:
    def minDays(self, bloom: List[int], m: int, k: int) -> int:
        
        left = min(bloom)
        right = max(bloom)
        ans = -1
        while left <= right:
            
            mid = (right + left) // 2
            count = 0
            total = 0
            for i in range(len(bloom)):
                if bloom[i] > mid:
                    count = 0
                else:
                    count += 1
                
                if count == k:
                    total += 1
                    count = 0
            if total >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans 
        