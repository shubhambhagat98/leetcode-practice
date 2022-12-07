class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        num = x
        rev_num = 0
        while num != 0:
            rem = num%10
            num = num//10 
            rev_num = rev_num*(10) + rem
        return x==rev_num
            