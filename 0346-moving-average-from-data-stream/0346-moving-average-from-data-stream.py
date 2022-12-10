class MovingAverage:

    def __init__(self, size: int):
        self.cq = [0]*size
        self.length = 0
        self.sum = 0
        self.tail = -1
        self.size = size
        
    def updateSum(self, val: int, prev:int):
        self.sum -= prev
        self.sum += val
        print(f"sum ==> {self.sum}")
        
    
    def getAverage(self):
        print(f"length==> {self.length}")
        print(f"avg==> {self.sum/self.length}\n")
        return self.sum/self.length

    def next(self, val: int) -> float:
        
        #check if tail is at last index
        if self.tail == self.size -1:
            self.tail = 0
        else:
            self.tail += 1
        
        prev = self.cq[self.tail]
        self.cq[self.tail] = val
        self.updateSum(val, prev)
        
        
        if self.length <= self.size -1:
            self.length+= 1
        
        
        return self.getAverage()
        
        
        
        
        
        
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)