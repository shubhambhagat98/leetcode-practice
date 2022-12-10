class Solution:
    
    
    def isValid(self, row, col, m, n, rooms):
        
        if 0 <= row < m and 0<= col < n and rooms[row][col] > 0:
            return True
        
        return False
    
    def successors(self, row, col, rooms):
        successors = [(row+1, col), (row-1,col), (row, col+1), (row, col-1)]
        
        return [succ for succ in successors if self.isValid(succ[0], succ[1], len(rooms), len(rooms[0]), rooms)    ]
    
    
    
    def bfs(self, start_row, start_col, rooms):
        
        queue = [((start_row, start_col), 0)]
        
        visited = set(((start_row, start_col), 0))
        
        while queue:
            current, dist = queue.pop(0)
            for succ in self.successors(*current, rooms):
                if succ not in visited:
                    queue.append((succ, dist + 1))
                    if rooms[succ[0]][succ[1]] > dist + 1:
                        rooms[succ[0]][succ[1]] = dist + 1
                    visited.add(succ)
                    
            
    
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    self.bfs(row, col, rooms)
        