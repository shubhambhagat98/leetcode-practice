"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val, [])
        
        self.visited[node] = new_node
        
        for n in node.neighbors:
            new_neighbor = self.cloneGraph(n)
            new_node.neighbors.append(new_neighbor)
        
        return new_node
        
        
        
            