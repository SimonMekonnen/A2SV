class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def bs(n,left):
            return bisect_right(left,2*n)
        def merge(l,r):
            nonlocal ans
            if l == r:
                return [nums[l]]
            
            mid = (l + r)//2
            left = merge(l,mid)
            right = merge(mid + 1,r)
            result = []
            lp = 0
            rp = 0
            for i in right:
                ans += len(left) - bs(i,left)
            while lp < len(left) and rp < len(right):
                if left[lp] < right[rp]:
                    result.append(left[lp])
                    lp += 1
                else:
                    result.append(right[rp])
                    rp += 1
            result.extend(left[lp :])
            result.extend(right[rp : ])
            return result
        merge(0,len(nums) - 1)
        return ans
       
        
        
            
            