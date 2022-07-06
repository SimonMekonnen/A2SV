class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        length = len(stack)

        for i in tokens:
            positive = i.isdigit()

            negative= i.startswith("-") and i[1:].isdigit()
            if positive or negative:
                stack.append(int(i))


            else:
                if i == "+":
                    x = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(x)

                if i == "-":
                    x = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(x)

                if i == "*":
                    x = stack[-1] * stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(x)

                if i == "/":

                    x = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(x)

        return stack[0]

