class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre = [nums[0]]
        post = [nums[-1]]
        for i in range(1,len(nums)):
            pre.append(nums[i]+pre[-1])
        for i in range(len(nums)-2,-1,-1):
            post.append(nums[i]+post[-1])
        ans = []
        for i in queries:
            b = -1
            c = -1
            for j in range(len(nums)):
                if pre[j] <= i:
                    b = j
                else:
                    break
            for k in range(len(nums)):
                if post[k] <= i:
                    c = k
                else:
                    break
            ans.append(max(b+1,c+1))
        return ans
                    
                    
        
        