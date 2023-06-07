class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        ans =  0
        def bt(index,s):
            nonlocal ans
            ans = max(ans,len(s))
            if index >= len(arr):
                return 
            flag = False
            for i in arr[index]:
                if i in s:
                    flag = True
                    break 
            if not flag and len(set(arr[index])) == len(arr[index]):
                bt(index + 1,s + arr[index])
            bt(index + 1,s)
        bt(0,"")
        return ans
        
        