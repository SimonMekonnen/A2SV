class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for i in range(len(ops)):
            c = ops[i]
            if c[-1].isdigit():
                score.append(int(c))
            elif c == "C":
                score.pop()
            elif c == "D":
                score.append(score[-1]*2)
            elif c == "+":
                score.append(score[-1]+score[-2])
        return sum(score)
            
        