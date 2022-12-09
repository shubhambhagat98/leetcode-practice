"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = [root]
        while queue:
            
            prev = None
            for i in range(len(queue)):
                curr = queue.pop(0)
                curr.next = prev
                
                # append right child first
                if curr.right:
                    queue.append(curr.right)
                
                if curr.left:
                    queue.append(curr.left)
                    
                prev = curr
        return root