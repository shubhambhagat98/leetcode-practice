class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        op = [0]*len(temperatures)
        for curr_index, curr_temp in enumerate(temperatures):
            while stack and curr_temp > stack[-1][1]:
                index, element = stack.pop()
                op[index] = curr_index - index
            
            stack.append((curr_index, curr_temp))
            
        
        return op
        