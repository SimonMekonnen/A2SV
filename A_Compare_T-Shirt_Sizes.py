N = int(input())

for _ in range(N):
    
    a,b = input().split()
    
    if ord(a[-1]) > ord(b[-1]):
        print("<")
        
    elif ord(a[-1]) < ord(b[-1]):
        print(">")
    
    else:
        if len(a) == len(b):
            
            print("=")
        
        elif a[-1] == "S":
            
            if (len(a)) > len(b):
                
                print("<")
            else:
                print(">")
        
        else:
            
            if len(a) < len(b):
                
                print("<")
            else:
                print(">")
            
    
    
    
    
