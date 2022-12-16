class Solution:
    
    def recReverse(self, s, index,):
        
        if index >= len(s):
            return
        
        current_char = s[index]
        dest_index = (index+1) * -1
        
        self.recReverse(s, index+1)
        
        s[dest_index] = current_char
        
        
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        self.recReverse(s, 0)