class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        ans = []
        def printf(i,target,a):
            if i >= len(c):
                if target == 0:
                    ans.append(a.copy())
                return 
            if target >= c[i]:
                a.append(c[i])
                target -= c[i]
                printf(i,target,a)
                a.pop()
                target += c[i]
            printf(i + 1,target,a)
            
        printf(0,target,[])
        return ans
        