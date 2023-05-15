class Solution:
    def racecar(self, target: int) -> int:
        
        visited  = set([(target,-1)])
        que = deque([[target,-1]])
        level = 0
        while que:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                if cur[0] == 0:
                    return level
                R = [cur[0],-1 if cur[1] > 0 else 1]
                A = [cur[0] + cur[1],cur[1] * 2]
                if tuple(R) not in visited and -target <= R[0] <= target:
                    if R[0] == 0:
                        return level + 1
                    que.append(R)
                    visited.add(tuple(R))
                if tuple(A) not in visited and -target <= A[0] <= target :
                    if A[0] == 0:
                        return level + 1
                    que.append(A)
                    visited.add(tuple(A))
    
            level += 1
        
                
            
        
        