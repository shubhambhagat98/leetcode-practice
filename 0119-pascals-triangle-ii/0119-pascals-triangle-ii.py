class Solution:
    
    def getRowRec(self, current_row, current_index, rowIndex):
        
        # print(f"curr row: {current_row}, curr index: {current_index}")
        
        if current_index - 1 == rowIndex:
            return current_row
        
        new_row = [1]
        
        if (current_index+1) > 2:
            for i in range(1, current_index):
                new_row.append(current_row[i-1]+current_row[i])
        # print(f"new row: {new_row}\n")
        new_row.append(1)
        return self.getRowRec(new_row, current_index+1, rowIndex)
        
        
    
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        
        
        
        return self.getRowRec([1], 1, rowIndex)
        