class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, col = set(), set()
        
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    col.add(c)
                    
        
        print(f"rows ==>  {rows}")
        print(f"col ==> {col}")
        
        
        for r in rows:
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    matrix[r][c] = 0
        
        for c in col:
            for r in range(len(matrix)):
                if matrix[r][c] != 0:
                    matrix[r][c] = 0
                    