class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        for i in range(len(words)):
            words[i] = words[i].count(min(words[i]))
        ans = []
        words.sort()
        for i in queries:
            ans.append(len(words) - bisect_right(words,i.count(min(i))))    
        return ans
        
        