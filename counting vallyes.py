def countingValleys(steps, path):
    # Write your code here
    valley = 0
    up = 0
    down = 0
    flag = 0
    for i in path:
            if i=="D":
                down+=1
            if i=="U":
                up+=1
            if up>down:
                flag = 1
            if up==down and flag == 0:
                print("hey")
                valley+=1
                up=0
                down=0
            if up==down:
                flag = 0
            
    return valley