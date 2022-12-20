class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dic = {'W': 0,'B':0}
        left = 0
        ans = len(blocks)
        for right in range(len(blocks)):
            if right - left + 1 <= k:
                dic[blocks[right]]+=1
            else:
                ans = min(ans,dic['W'])
                dic[blocks[right]]+=1
                dic[blocks[left]]-=1
                left+=1
        return min(ans,dic['W'])
                
        