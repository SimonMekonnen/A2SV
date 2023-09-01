class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        def bt(index,arr):
            if len(arr) > k:
                return 
            if len(arr) == k:
                if sum(arr) == n:
                    ans.append(arr.copy())
                return 
            if index <= 9:
                bt(index + 1,arr + [index])
                bt(index + 1,arr)
        bt(1,[])
        return ans
            