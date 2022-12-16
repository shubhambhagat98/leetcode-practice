class Solution:
    
    
    def climb_stairs_rec(self, current, n,memo):
        
        if current > n:
            return 0
        
        if current == n:
            return 1
        
        
        if current in memo:
            return memo[current]
        
        
        memo[current] = self.climb_stairs_rec(current+1, n, memo) + self.climb_stairs_rec(current+2,n,memo)
        
        return memo[current]
        
        
    
    
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        return self.climb_stairs_rec(0, n, memo)