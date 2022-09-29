class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        total_1 = n*(n+1)/2
        
        total_2 = sum(nums)
        
        return int(total_1 - total_2)
        
        
        