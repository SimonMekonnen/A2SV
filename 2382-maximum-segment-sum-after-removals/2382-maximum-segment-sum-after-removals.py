class Solution:
    def maximumSegmentSum(self, nums: List[int], r: List[int]) -> List[int]:
        ans = []
        bestsum = 0
        parent = [-1 for i in range(len(nums))]
        size = [0 for i in range(len(nums))]
        def find(x):
            if parent[x] == -1:
                return x
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]
            while x != parent[x]:
                v = parent[x]
                parent[x] = cur
                x = v
            return cur
        def union(x,y):
            xparent = find(x)
            yparent = find(y)
            parent[xparent] = yparent
            size[yparent] += size[xparent]
        for i in range(len(nums) - 1, -1,-1):
            ans.append(bestsum)
            parent[r[i]] = r[i]
            size[r[i]] = nums[r[i]]
            if r[i] != len(nums) - 1:
                right = parent[find(r[i] + 1)]
                if right != -1:
                    union(r[i],r[i] + 1)         
                       
            if r[i] != 0:
                left = parent[find(r[i] - 1)]
                if left != -1:
                    union(r[i],r[i] - 1)
                       
            bestsum = max(size[parent[find(r[i])]],bestsum)
        ans.reverse()
        return ans
                    
                    
                    
                    
            
            
        
        
        