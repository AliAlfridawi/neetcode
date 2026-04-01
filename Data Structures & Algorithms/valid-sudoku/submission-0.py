class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowVector = [0] * 9

        for row in board:
            rowVector = [0] * 9
            for i in row:
                if i != ".":
                    rowVector[int(i)-1]+=1
                    if rowVector[int(i)-1]>1:
                        return False
        
        for col in range(9):
            rowVector = [0] * 9
            column = [row[col] for row in board]
            for i in column:
                if i != ".":
                    rowVector[int(i)-1]+=1
                    if rowVector[int(i)-1]>1:
                        return False
            
        for i in range(0,9,3):
            for j in range(0,9,3):
                rowVector = [0] * 9
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y]!='.':
                            rowVector[int(board[i+x][j+y])-1]+=1
                for w in rowVector:
                    if w > 1:
                        return False
            
        return True