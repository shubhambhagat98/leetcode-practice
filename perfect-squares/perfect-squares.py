class Solution:
    def numSquares(self, n: int) -> int:
        
        if n < 2:
            return n
        
        # list of perfect squares less than equal to n
        squares = []
        i = 1
        while (i*i) <= n:
            squares.append(i*i)
            i+= 1
        
        count = 0
        queue = [n]
        visited = {n}
        while queue:
            count += 1 
            
            for i in range(len(queue)):
                remainder = queue.pop(0)    
                # print(f"remainder : {remainder}, path: {path}")
                
                for sqr in squares:
                    if remainder == sqr:
                        # print(f"remainder ==> {remainder} path==> {path}")
                        return count
                    if remainder < sqr:
                        break
                    else:
                        if (remainder - sqr) not in visited:
                            queue.append(remainder-sqr)
                            visited.add(remainder-sqr)
            # print(f"queue: {queue}\n")
        return count
                    