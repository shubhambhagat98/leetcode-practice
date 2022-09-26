class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict = set()
        # for n in nums:
        #     if mydict.get(n):
        #         return True
        #     mydict[n] = 1
        # return False
        
        for n in nums:
            if n in mydict:
                return True
            mydict.add(n)
        return False
        