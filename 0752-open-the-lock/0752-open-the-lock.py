class Solution:
    
    
    def __init__(self):
        self.deadends = set()
        self.count = float('inf')
    
    def isValid(self, succ):
        if succ not in self.deadends:
            return True
        return False
        
    def successors(self, current):
        
        succ_list = []
        
        for i in range(4):
            temp_succ1  = current[0:i] + str((int(current[i]) + 9) %10) + current[i+1:]
            # print(f"t1 : {temp_succ1}", end=" ")
            temp_succ2 = current[0:i] + str((int(current[i] ) + 1) %10) + current[i+1:]
            # print(f"t2 : {temp_succ2}", end= " ")
            if self.isValid(temp_succ1):
                succ_list.append(temp_succ1)
            if self.isValid(temp_succ2):
                succ_list.append(temp_succ2)
        
        
        return succ_list
            
    
    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        
        self.deadends = set(deadends)
        
        if "0000" in self.deadends:
            return -1
        
        
        queue = [("0000", 0)]
        visited = set("0000")
        
        while queue:
            
            # print(f"\n\ncurrent : {queue[0]}")
            
            curr, t_count = queue.pop(0)
            
            if curr == target:
                return t_count
            
            for succ in self.successors(curr):
                if succ not in visited:
                    queue.append((succ, t_count+1))
                    visited.add(succ)
            # print(f"queue : {queue}\n")
            
        return -1
                
        