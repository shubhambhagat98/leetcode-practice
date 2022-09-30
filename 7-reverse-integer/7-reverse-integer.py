class Solution:
    def reverse(self, x: int) -> int:

        is_negative = False

        if x<0:
            is_negative = True
        
        x = abs(x)

        rem = 0
        num = x

        count = len(str(x)) -1
        temp = 0
        while count >=0:
            rem = num %10
            temp += rem*(10**count)
            num = num//10
            count -=1

            
        
        if is_negative:
            temp *= -1
        
        if temp < -1*(2**31) or temp > 2**31:
            return 0
        
        return temp

