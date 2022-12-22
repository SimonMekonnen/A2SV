class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        for i in range(len(command)):
            if command[i]== 'G':
                ans+="G"
            if command[i]== ')':
                ans+='o' if command[i-1] == '(' else 'al'
        return ans
        
            
        