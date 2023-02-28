class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        length = len(stack)
        c = ["+","-","*","/"]
        for i in tokens:
            if i not in c:
                stack.append(int(i))
            else:
                if i == "+":
                    x = stack[-1] + stack[-2]
                if i == "-":
                    x = stack[-2] - stack[-1]
                if i == "*":
                    x = stack[-1] * stack[-2]
                if i == "/":
                    x = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(x)

                  

        return stack[0]

