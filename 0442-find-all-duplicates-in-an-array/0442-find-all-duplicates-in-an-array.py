class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(0,len(nums)):
            # print(nums)
            new_index = abs(nums[i])-1
            if nums[new_index] < 0:
                output.append(abs(nums[i]))
            else:
                nums[new_index]*= -1
        return output