class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if (val <= self.min): # if current val is minimum
            self.stack.append(self.min) # append previous min
            self.min = val # update current min
        self.stack.append(val)
        
    def pop(self) -> None:
        
        if self.min == self.stack.pop(): # top is min
            self.min = self.stack.pop() # store previous min as current minimum  

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()