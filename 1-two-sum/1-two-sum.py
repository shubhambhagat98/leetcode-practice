class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        op = []
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if d.get(diff) is None:
                d[nums[i]] = i
            else:
                op = [d[diff], i ]
        
        return op
        