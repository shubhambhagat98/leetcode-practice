import heapq

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        if amount <= 0:
            return 0
        
        coins = sorted(coins)
        print(coins)
        
        #set of coins
        coin_dict = dict.fromkeys(coins, 1)
        print(coin_dict)
        count = 0
        
        queue = [amount]
        visited = {amount}
        
        while queue:
            
            count += 1
            
            for i in range(len(queue)):
                remainder = queue.pop(0)
                
                # if remainder in coin_dict ==> goal state
                if remainder in coin_dict:
                    return count
                
                for coin in coin_dict:
                    if remainder < coin:
                        break
                    else:
                        if remainder-coin not in visited:
                            queue.append(remainder-coin)
                            visited.add(remainder-coin)
        
        return -1
                
                
            
        
        