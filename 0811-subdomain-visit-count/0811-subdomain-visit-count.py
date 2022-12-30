class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        for i in cpdomains:
            c = i.split()
            b = c[1].split(".")
          
            for j in range(0,len(b)):
                dic[".".join(b[j:])]+=int(c[0])
    
        return [f"{val} {key}" for key,val in dic.items()]
                
                
                
            
        