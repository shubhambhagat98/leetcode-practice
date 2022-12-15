class Solution:
    
    def __init__(self):
        self.visited = set()
    
    def isValid(self, row, col, m, n):
        if 0 <= row < m and 0<= col < n:
            return True
        return False
    
    
    
    def successors(self,curr_row, curr_col, image):
        temp_succ = [(curr_row-1, curr_col), (curr_row+1, curr_col), (curr_row, curr_col-1), (curr_row, curr_col+1)]
        
        op = []
        
        for (cr,cc) in temp_succ:
            if self.isValid(cr, cc, len(image), len(image[0])) and image[curr_row][curr_col] == image[cr][cc]:
                op.append((cr,cc))
        
        return op
        
        
    
    def floodFillRec(self, current, color, image):
        
        for succ in self.successors(*current, image):
            if succ not in self.visited:
                self.visited.add(succ)
                self.floodFillRec(succ, color, image)
        
        image[current[0]][current[1]] = color
        
    
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        op_image = image
        self.visited.add((sr,sc))
        self.floodFillRec((sr,sc), color, op_image)
        
        return op_image
        