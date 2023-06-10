class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        def bt(arr,visited):
            nonlocal count
            if len(arr) == n:
                count += 1
                return 
            
            for i in range(1,n + 1):
                if i not in visited and\
                (i % (len(arr) + 1) == 0 or (len(arr) + 1) % i == 0) :
                    visited.add(i)
                    bt(arr + [i],visited)
                    visited.remove(i)
        bt([],set())
        return count
    