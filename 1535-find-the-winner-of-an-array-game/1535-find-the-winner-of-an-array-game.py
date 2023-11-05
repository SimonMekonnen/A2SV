class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        
        if k >= len(arr):
            return max(arr)
    
        que = deque(arr)
        val = max(arr[0],arr[1])
        count = 0
        while True:
            first = que.popleft()
            second = que.popleft()
            if first > second:
                if val == first:
                    count += 1
                else:
                    count = 1
                val = first
                que.appendleft(first)
                que.append(second)
                
            else:
                if val == second:
                    count += 1
                else:
                    count = 1
                val = second
                que.appendleft(second)
                que.append(first)
                
            if count == k:
                return val
            
  