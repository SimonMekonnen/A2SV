class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        dif = 0
        pos = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                dif += 1
                pos.append([s[i],goal[i]])
    
        if (dif == 2 and pos[0][0] == pos[1][1] and pos[0][1] == pos[1][0]) or (dif == 0 and len(set(s)) != len(s)):
            return True
        return False
        