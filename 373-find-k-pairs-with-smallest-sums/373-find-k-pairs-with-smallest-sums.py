class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        ans = []
        heap = [(nums1[0] + nums2[0],0,0)]
        visited = set()
        visited.add((0,0))
        while heap and len(ans) != k:
            cur = heappop(heap)
            ans.append([nums1[cur[1]],nums2[cur[2]]])
            
            if  cur[1] + 1 < len(nums1) and (cur[1] + 1,cur[2]) not in visited:
                heappush(heap,(nums1[cur[1] + 1] + nums2[cur[2]],cur[1] + 1, cur[2]))
                visited.add((cur[1] + 1,cur[2]))
            if cur[2] + 1 < len(nums2) and (cur[1],cur[2] + 1) not in visited:
                heappush(heap,(nums1[cur[1]] + nums2[cur[2] + 1],cur[1], cur[2] + 1))
                visited.add((cur[1],cur[2] + 1))
        return ans
                
            
            
        
        
        
        
   