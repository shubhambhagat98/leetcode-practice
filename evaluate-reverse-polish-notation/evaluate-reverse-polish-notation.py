import math
class Solution:
    
    
    def __init__(self):
        self.op = {"*","+","-","/"}
    
    
    def cal(self, left, right, operation):
        
        if operation == "+":
            return left + right
        elif operation == "-":
            return left - right
        elif operation == "*":
            return left*(right)
        elif operation == "/":
            return int(left/right)
    
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        stack = []
        
        
        
        for x in tokens:
            if x in self.op:
                
                right = stack.pop()
                left = stack.pop()
                # print(f"left: {left} | right: {right} | op: {x}")
                ans = self.cal(left, right, x)
                # print(f"ans: {ans}")
                stack.append(ans)
            else:
                stack.append(int(x))
        
        return stack[-1]
                