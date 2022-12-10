class MyCircularQueue:
    
    

    def __init__(self, k: int):
        self.cq = [None] * k
        self.size = k
        self.length = 0
        self.front = 0
        self.tail = -1
        # print(self.cq)

    def enQueue(self, value: int) -> bool:
        if self.length != self.size:
            if self.tail == self.size-1:
                self.tail = 0
            else:
                
                self.tail+= 1
            self.cq[self.tail] = value
            self.length += 1
            # print(f"enQueue ==> {self.cq}")
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        else:
            self.cq[self.front] = None
            if self.front == self.size-1:
                self.front = 0
            else:
                
                self.front+= 1
            self.length -= 1
            # print(f"deQueue ==> {self.cq}")
            return True

    def Front(self) -> int:
        
        if self.length == 0:
            # print(f"front ==> -1")
            return -1
        else:
            # print(f"front ==> {self.cq[self.front]}")
            return self.cq[self.front]
        
        

    def Rear(self) -> int:
        if self.length == 0:
            # print(f"rear ==> -1")
            return -1
        else:
            # print(f"rear ==> {self.cq[self.tail]}")
            return self.cq[self.tail]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()