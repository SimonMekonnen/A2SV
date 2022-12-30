class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            c = set()
            for j in range(len(board[0])):
                if i[j]!='.' and i[j] in c:
                    return False
                c.add(i[j])
        for i in range(len(board[0])):
            c = set()
            for j in range(len(board)):
                if board[j][i]!='.' and board[j][i]in c:
                    return False
                c.add(board[j][i])
        def ere(s,e):
            co = 0
            seen = set()
            to = [(2,2),(2,5),(2,8),(5,2),(5,5),(5,8),(8,2),(8,5),(8,8)]
            for r in range(9):
                for c in range(s,e):
                    if board[r][c] == ".":
                        co+=1
                    else:
                        seen.add(board[r][c])
                if (r,c) in to:
                    if len(seen) + co != 9:
                        return False
                    seen = set()
                    co = 0 
            return True     
       
        return ere(0,3) == True and ere(3,6) == True and ere(6,9) == True
    
        