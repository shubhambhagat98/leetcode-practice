class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         mydict = {}
#         for i in range(1, len(nums)+1):
#             mydict[i] = 0
            
#         for x in nums:
#             mydict[x] = 1
            
#         l = []
        
#         for j in mydict:
#             if mydict[j] == 0:
#                 l.append(j)
#         return l
        
#         l = []

#         temp = [0]*len(nums)
#         for x in nums:
#             temp[x-1]=1
        
#         for i in range(len(temp)):
#             if temp[i]==0:
#                 l.append(i+1)
#         return l

        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]*= -1
        l=[]
        for i in range(len(nums)):
            if nums[i]>0:
                l.append(i+1)
        return l      
                
            