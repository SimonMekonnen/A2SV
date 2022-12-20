class Solution:
    def trap(self, h: List[int]) -> int:
        stk = []
        ans = 0
        for i,n in enumerate(h):
            while stk and h[stk[-1]] < n:
                t = stk.pop()
                if not stk:
                    break
                d = i - stk[-1] - 1
                hi = min(n,h[stk[-1]]) - h[t]
                ans+=d*hi
            stk.append(i)
        return ans
        