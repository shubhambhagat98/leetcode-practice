class Solution:
    def arrangeCoins(self, n: int) -> int:
        prev = 0
        i = 1
        
        while prev+i <= n:
            prev += i
            i+=1
        
        return i-1
        