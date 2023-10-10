class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        dic = set(['a','b','c','d','e','f','A','B','C','D','E','F'])
        def ip4(num):
            if not num:
                return False
            for i in num:
                if not i.isdigit():
                    return False
            if len(str(int(num))) !=  len(num) or len(num) > 3:
                return False
          
            if int(num) > 255:
                return False
            
            return True
        
        def ip6(num):
            if not num:
                return False
            for i in num:
                if not i.isdigit() and i not in dic:
                    return False
    
            if len(num) > 4:
                return False
                
            return True
        
        forip4 = queryIP.split(".")
        forip6 = queryIP.split(':')
        if len(forip4) == 4:
            pos = 1
            for i in forip4:
                pos &= ip4(i)
            
            if pos:
                return "IPv4"
       
        if len(forip6) == 8:
            pos = 1
            for i in forip6:
                pos &= ip6(i)
            if pos:
                return "IPv6"
        return "Neither"
        
                    