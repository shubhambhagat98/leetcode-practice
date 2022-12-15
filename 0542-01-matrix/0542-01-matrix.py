class Solution:
    
    
    def isValid(self, row, col, m, n):
        if 0 <= row < m and 0 <= col < n:
            return True
        return False
    
    def successors(self, curr_row, curr_col, mat):
        
        temp_succ = [(curr_row-1, curr_col), (curr_row+1, curr_col), (curr_row, curr_col-1), (curr_row, curr_col+1)] 
        op = []       
        for (cr,cc) in temp_succ:
            if self.isValid(cr,cc, len(mat), len(mat[0])):
                op.append((cr,cc))        
        return op
    
    
    def bfs(self, initial_queue, mat, dist_mat):
        
        queue = initial_queue
        
        while queue:
            row, col = queue.pop(0)
            for sr,sc in self.successors(row, col, mat):
                if dist_mat[sr][sc] > dist_mat[row][col] + 1:
                    dist_mat[sr][sc] = dist_mat[row][col] + 1
                    queue.append((sr,sc))
                    
                
                
    
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist_mat = [ [ float('inf') for j in range(len(mat[0]))] for i in range(len(mat))]
        # print(dist_mat)
        # print(mat)
        initial_queue = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    # print(row, col, dist_mat)
                    dist_mat[row][col] = 0
                    # print(row, col, dist_mat)
                    initial_queue.append((row, col))
                
        
            
                
        self.bfs(initial_queue, mat, dist_mat)
        
        
        return dist_mat
        
        
        
        
        