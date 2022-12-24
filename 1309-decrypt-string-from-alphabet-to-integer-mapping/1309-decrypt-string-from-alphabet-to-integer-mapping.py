class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        left = 0
        right = 2
        ans = ""
        while left < len(s):
            if right < len(s) and s[right] == "#":
                ans+=chr(int(s[left:right]) + 96)
                right+=3
                left+=3
                
            else:
                ans+=chr(int((s[left])) + 96)
                left+=1
                right+=1

        return ans
                
                
        