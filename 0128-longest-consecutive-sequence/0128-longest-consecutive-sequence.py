class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        
        final_count = 0
        
        for x in nums:
            temp = 0
            if x-1 in s:
                continue
            else:
                # start subsequence
                temp+=1
                curr = x+1
                while True:
                    if curr in s:
                        temp+=1
                    else:
                        break
                    curr+=1
                
                final_count = max(final_count, temp)
        
        return final_count
                    
                    