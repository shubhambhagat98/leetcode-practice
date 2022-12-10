class Solution:

    def __init__(self):
        self.visited = set()
        self.count = 0
    
    def isValid(self, row, col, m, n, grid):
        
        if 0 <= row < m and 0<= col < n and grid[row][col] == "1":
            return True
        
        return False
    
    def successors(self, row, col, grid):
        successors = [(row+1, col), (row-1,col), (row, col+1), (row, col-1)]
        
        return [succ for succ in successors if self.isValid(succ[0], succ[1], len(grid), len(grid[0]), grid)    ]
    
    
    
    def bfs(self, start_row, start_col, grid):
        
        queue = [(start_row, start_col)]
        self.visited.add((start_row, start_col))
        current_island = [(start_row, start_col)]
        
        while queue:
            curr_row, curr_col = queue.pop(0)
            
            for succ in self.successors(curr_row, curr_col, grid):
                if succ not in self.visited:
                    queue.append(succ)
                    self.visited.add(succ)
                    current_island.append(succ)
        print(f"current Island ==> {current_island}")
                
    def numIslands(self, grid: List[List[str]]) -> int:
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.count += 1
                    self.bfs(row, col, grid)
                    
        
        return self.count 