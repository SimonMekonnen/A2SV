class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        count = 0
        for c in range(len(s[0])):
            temp = s[0][c]

            for r in range(len(s)):
                if s[r][c] < temp:
                    count+=1
                    break
                temp = s[r][c]
    
        return count


        