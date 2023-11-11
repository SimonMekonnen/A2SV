class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        
        dic = Counter(letters)
        def bt(index):
    
            if index >= len(words):
                return 0
            
            pos = 1
            word = Counter(words[index])
            for i in word:
                if dic[i] < word[i]:
                    pos = 0
        
            if pos:
                t = 0
                for i in word:
                    dic[i] -= word[i]
                    t += score[ord(i) - ord("a")] * word[i]
                pick = t + bt(index + 1)
                for i in word:
                    dic[i] += word[i]
                
                dontpick = bt(index + 1)
                
                return max(pick,dontpick)
            
            return bt(index + 1)
        
        return bt(0)
                
                
                
                
            
            
            