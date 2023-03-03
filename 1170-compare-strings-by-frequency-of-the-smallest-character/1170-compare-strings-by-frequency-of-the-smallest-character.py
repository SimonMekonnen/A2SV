class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        for i in range(len(words)):
            c = Counter(words[i])
            
            words[i] = c[min(words[i])]
        
        ans = []
        words.sort()
        for i in queries:
            c = Counter(i)
            now = bisect_right(words,c[min(i)])
            ans.append(len(words) - now)
            
        return ans
        
        