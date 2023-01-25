class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        ans = 0
        b = skill[0] + skill[-1]
        while left < right:
            
            ans+=(skill[left] * skill[right])
            if b != skill[left] + skill[right]:
                return -1
            left+=1
            right-=1
        
        return ans
        