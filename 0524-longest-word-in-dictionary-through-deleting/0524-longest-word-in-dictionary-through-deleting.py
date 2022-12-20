class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort()
        d.sort(key=lambda x: len(x),reverse=True)
        for word in d:
            small , long = 0, 0
            while small  < len(word) and long < len(s):
                if word[small] == s[long]:
                    small+=1
                long+=1
            if small == len(word):
                return word
       
        return ""
            
        
        