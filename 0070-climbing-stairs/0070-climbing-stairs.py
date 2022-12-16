class Solution:
    
    
    def climb_stairs_rec(self, current, n, level, memo):
        
        if current > n:
            return 0
        
        if current == n:
            return 1
        
        
        if (level,current) in memo:
            return memo[(level,current)]
        
        
        memo[(level,current)] = self.climb_stairs_rec(current+1, n, level+1, memo) + self.climb_stairs_rec(current+2,n, level+1, memo)
        
        return memo[(level,current)]
        
        
    
    
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        return self.climb_stairs_rec(0, n, 0, memo)