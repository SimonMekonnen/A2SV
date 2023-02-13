class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        right = 0
        now = []
        while right  < len(num1):
            
            if num1[right] == "+":
                now.append(num1[:right])
                now.append(num1[right + 1: len(num1) - 1])
                break
            right += 1
        n2 = []
        right = 0
        while right  < len(num2):
            
            if num2[right] == "+":
                n2.append(num2[:right])
                n2.append(num2[right + 1: len(num2) - 1])
                break
            right += 1
        
        ans = []
        for i in now:
            
            for j in n2:
                
                ans.append(int(i) * int(j))
                
        return (f"{ans[0] - ans[-1]}+{ans[1] + ans[2]}i")
                
        