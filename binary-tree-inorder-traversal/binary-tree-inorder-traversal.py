# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#         if root:
#             result += self.inorderTraversal(root.left)
#             result.append(root.val)
#             result += self.inorderTraversal(root.right)
    
#         return result
        
        if not root:
            return []

        stack = []
        op = []
        current = root
        
        while True:
            
            if current:
                stack.append(current)
                current= current.left
            
            elif stack:
                current = stack.pop()
                op.append(current.val)
                current = current.right
            
            else:
                break
        
        return op