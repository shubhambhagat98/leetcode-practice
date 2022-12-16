class Solution:
    
    def recReverse(self, s, low, high ):
        
        if low > high:
            return
        
        s[low], s[high] = s[high], s[low]
        
        self.recReverse(s, low+1, high-1)
        
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        self.recReverse(s, 0, len(s)-1)