class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []  
        temp_num = ""
        for c in s:
            
            if c =="[":
                stack.append(temp_num)   
                temp_num = ""
            elif c == "]":
                
                # get sub string
                temp = ""
                while not stack[-1].isdigit():
                    temp = stack.pop() + temp
                
                # get count
                c = stack.pop()
                
                temp = int(c)*temp
                stack.append(temp)
                print(temp)
            
            elif c.isdigit():
                temp_num += c
            else:
                stack.append(c)
        
        print("".join(stack))
            
        
        return "".join(stack)
                