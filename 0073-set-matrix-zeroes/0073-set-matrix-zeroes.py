class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        rowZeroFlag = False
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZeroFlag = True
                    
                    
        for r in range(1,ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(1, ROWS):
                matrix[r][0] = 0
        
        if rowZeroFlag == True:
            for c in range(0, COLS):
                matrix[0][c] = 0
                
                
                    