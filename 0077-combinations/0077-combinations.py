class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        def bt(num,arr):
            if num > n + 1:
                return
            if len(arr) >= k:
                if len(arr) == k:
                    ans.append(arr)
                return 
            bt(num + 1,arr + [num])
            bt(num + 1,arr)
        bt(1,[])
        return ans
        