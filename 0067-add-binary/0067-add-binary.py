class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = [0] * (max(len(a),len(b)) + 1)
        c = max(len(a),len(b))
        a = [0]*(c-len(a)) + list(a)
        b = [0]*(c-len(b))+list(b)
        carry = 0
        for i in range(len(a)-1,-1,-1):
            ans[i+1] = (int(a[i])+int(b[i])+carry)%2
            if (int(a[i])+int(b[i])+carry)>=2:
                carry = 1
            else:
                carry = 0
        ans[0] = carry 
        
        for i,n in enumerate(ans):
            if n == 1:
                break
        ans = "".join(str(i) for i in ans[i:])
        return ans 
            
        