class Solution:
    
    empty = 2147483647
    
    
    def isValid(self, row, col, m, n, rooms):
        
        if 0 <= row < m and 0<= col < n and rooms[row][col] == self.empty:
            return True
        
        return False
    
    def successors(self, row, col, rooms):
        successors = [(row+1, col), (row-1,col), (row, col+1), (row, col-1)]
        
        return [succ for succ in successors if self.isValid(succ[0], succ[1], len(rooms), len(rooms[0]), rooms)    ]
    
    
    
    def bfs(self, gates, rooms):
        
        queue = gates      
        while queue:
            row, col = queue.pop(0)
            for succ in self.successors(row, col, rooms):
                queue.append(succ)
                rooms[succ[0]][succ[1]] = rooms[row][col] + 1
            
                    
            
    
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        gates = []
        
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    gates.append((row,col))
        
        self.bfs(gates, rooms)
                    
                    
                    
                    
                    
                    
                    
        