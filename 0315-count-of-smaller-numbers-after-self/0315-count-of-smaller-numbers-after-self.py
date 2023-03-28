class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums))]
        b = [i for i in range(len(nums))]
        def helper(l,r,arr):
            nonlocal ans
            if l >= r:
                return [arr[l]]
            mid = (l + r)//2
            right = helper(mid + 1,r,arr)
            left = helper(l,mid,arr)
            p1 = 0
            p2 = 0
            new = []
            t = [nums[i] for i in right]
            for i in left:
                n = nums[i]
                ans[i] += bisect_left(t,n)
            while p1 < len(left) and p2 < len(right):
                if nums[right[p2]] > nums[left[p1]]:
                    new.append(left[p1])
                    p1+=1
                else:
                    new.append(right[p2])
                    p2+=1
            new.extend(right[p2:])
            new.extend(left[p1:])
            return new
        helper(0,len(nums) - 1 , b)
        return ans
                    
                        
        