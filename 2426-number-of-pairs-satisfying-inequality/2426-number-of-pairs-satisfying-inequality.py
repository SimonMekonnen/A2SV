class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        new =[]
        ans = 0
        for i in range(len(nums1)):
            new.append(nums1[i] - nums2[i])
        def helper(arr,l , r):
            nonlocal ans
            nonlocal diff
            if l >= r:
                return [arr[l]]
            mid = (l + r) // 2
            left = helper(arr,l,mid)
            right = helper(arr,mid + 1,r)
            
            for i in right:
                
                ans += bisect_right(left,i + diff)
            
         
            merged = []
            p1 = 0
            p2 = 0
            while p1 < len(left) and p2 < len(right):
                if left[p1] < right[p2]:
                    merged.append(left[p1])
                    p1 += 1
                else:
                    merged.append(right[p2])
                    p2 += 1
            merged.extend(left[p1:])
            merged.extend(right[p2:])
            return merged
        helper(new,0,len(new) - 1)
        return ans
            
            
