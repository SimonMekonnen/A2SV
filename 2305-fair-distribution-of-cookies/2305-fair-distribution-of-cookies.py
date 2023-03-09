class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        result = float('inf')
        score = [0] * k
        
        def minscore(index):
            nonlocal result
            if index >= len(cookies):
                result = min(result,max(score))
                return
            if max(score) >= result:
                return 
            
            for i in range(k):
                if score[i] + cookies[index] < result:
                    score[i] += cookies[index]
                    minscore(index + 1)
                    score[i] -= cookies[index]
                
        cookies.sort(reverse = True)
        minscore(0)
        return result