class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        ans = set()
        
        def bt(index,out,count):
            nonlocal ans
            if count > 4:
                return
            if index >= len(s):
                if count == 4:
                    ans.add(out)
                return 
            
            if int(s[index : index + 1]) <= 255 and str(int(s[index : index + 1])) == s[index : index + 1] :
                 bt(index + 1,out + s[index : index + 1] + ".",count + 1)
            if int(s[index : index + 2]) <= 255 and str(int(s[index : index + 2])) == s[index : index + 2]:
                 bt(index + 2,out + s[index : index + 2] + ".",count + 1)
            if int(s[index : index + 3]) <= 255 and str(int(s[index : index + 3])) == s[index : index + 3]:
                 bt(index + 3,out + s[index : index + 3] + ".",count + 1)
            
            return 
        bt(0,'',0)
        res = []
        for i in ans:
            res.append(i[ : len(i) - 1])
        return res
                
                
           
            
            
        