if __name__ == '__main__':
    N = int(input())
    ans = []
    while N > 0:
        command =  list(input().split())
        
        if command[0] == 'append':
            ans.append(int(command[1]))
            
        elif command[0] == 'remove':
            ans.remove(int(command[1]))
            
        elif command[0] == 'sort':
            ans.sort()
            
        elif command[0] == 'pop':
            ans.pop()
            
        elif command[0] == 'reverse':
            ans.reverse()
            
        elif command[0] == 'print':
            print(ans)
            
        else:
            ans.insert(int(command[1]),int(command[2]))
        N-=1
