class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            cut=nums[l[i]:r[i]+1]
            cut.sort()
            k=cut[1]-cut[0]
            val = True
            for i in range(len(cut)-1):
                if cut[i+1]-cut[i]!=k:
                    val=False
                    break
            ans.append(val)
        return ans
        
            

            
            
            
            
        