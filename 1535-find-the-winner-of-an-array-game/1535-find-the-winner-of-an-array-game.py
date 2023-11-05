class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        
        if k >= len(arr):
            return max(arr)
    
        que = deque(arr)
        dic = defaultdict(int)
        while True:
            first = que.popleft()
            second = que.popleft()
            
            if first > second:
                dic[first] += 1
                que.appendleft(first)
                que.append(second)
                dic[second] = 0
            if second > first:
                dic[second] += 1
                que.appendleft(second)
                que.append(first)
                dic[first] = 0
            
            if dic[first] == k:
                return first
            if dic[second] == k:
                return second
            
            
            
  