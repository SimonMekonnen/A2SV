class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =  0
        right = 0
        c = set()
        long = 0
        while right < len(s):
            if s[right] not in c:
                c.add(s[right])
                right+=1
            else:
                c.remove(s[left])
                left+=1
            long = max(long,right-left)
        return long
            
    