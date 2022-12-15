class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited  = {0}
        
        queue = []
        
        for x in rooms[0]:
            queue.append(x)
            visited.add(x)
            
        while queue:
            index = queue.pop(0)
            
            for lock in rooms[index]:
                if lock not in visited:
                    visited.add(lock)
                    queue.append(lock)
        
        print(visited)
        
        return len(visited) == len(rooms)