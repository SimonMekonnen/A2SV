class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        arr = [1000000000,1000000,1000,100,10,1]
        hey = [0] * 6
        
        i = 0
        while num:
            
            hey[i] = num//arr[i]
            num%=arr[i]
            i+=1
        
        another = [100,10,1]
        now = []
        for n in hey:
            t = [0,0,0]
            i = 0
            while n:

                t[i] = n//another[i]
                n%=another[i]
                i+=1
            now.append(t)
        
        table1 = {
            1 : 'One',
                2 : 'Two',
                3 : 'Three',
                4 : 'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'
                }
        table2 = {1 : 'One',
                2 : 'Twenty',
                3 : 'Thirty',
                4 : 'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'
                }
        table3 = {10 : 'Ten',11 : "Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        ans = ""
        name = ["Billion","Million","Thousand","Hundred"]
  
        for i in range(len(now) - 2):
            n = ""
            num = now[i]
            for j in range(len(num)):
                
                if num[j] != 0:
                    
                    if j == 0:
                        
                        n += table1[num[j]] + " " +  "Hundred" + " "
                    
                    if j == 1:
                        if num[j] != 1:
                            n += table2[num[j]] + " "
                        else:
                            n += table3[int(str(num[-2]) + str(num[-1]))] + " "
                        
                    if j == 2:
                        if num[1] != 1: 
                             n += table1[num[j]]+ " "
        
            n = n.strip()  
    
            if n!= "":
                ans += (n + " " + name[i]) + " "
            
            c = str(hey[-2]) + str(hey[-1])
        if int(c) != 0:
            if len(str(int(c))) == 2:
                if int(c[0]) != 1:
                        ans += table2[int(c[0])] + " "
                        if int(c[1]) != 0:
                            ans += table1[int(c[1])]+ " "
                else:
                        ans += table3[int(c)] + " "  
            elif len(str(int(c))) == 1:
                ans += table1[int(c[1])]+ " "
            
        return ans.strip()
            
            
            
            
            
            
        