class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        temp = []
        top = 0 
        bottom  = ROWS-1
        left = 0
        right = COLS-1
        
        while True:
            
            # first row - top
            for col in range(left, right+1):
                temp.append(matrix[top][col])
            
            top += 1
            if len(temp) == ROWS * COLS:
                break
            
            # last_col - right
            for row in range(top, bottom+1):
                temp.append(matrix[row][right])
            
            right -= 1
            if len(temp) == ROWS * COLS:
                break
                
            # last row - bottom
            for col in range(right, left-1, -1):
                temp.append(matrix[bottom][col])
            
            bottom -= 1
            if len(temp) == ROWS * COLS:
                break
            
             # first col - left
            for row in range(bottom, top-1, -1):
                temp.append(matrix[row][left])
            
            left += 1
            if len(temp) == ROWS * COLS:
                break
        
        return temp