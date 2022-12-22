class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for i in range(len(num1)):
            n1+=((ord(num1[i])) - 48) * 10**(len(num1) - 1 - i)
        for i in range(len(num2)):
            n2+=((ord(num2[i])) - 48) * 10**(len(num2) - 1 - i)
        return str(n1 * n2)
        
            
        
        