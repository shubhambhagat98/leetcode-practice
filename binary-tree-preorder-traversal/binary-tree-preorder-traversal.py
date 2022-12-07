# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         result = []
#         if root:
#             result.append(root.val)
#             result += self.preorderTraversal(root.left)
#             result += self.preorderTraversal(root.right)
    
#         return result
        
        if not root:
            return []

        stack = [root]
        op = []
        
        while stack:
            current = stack.pop()
            
            op.append(current.val)
            # append RIGHT child first, so while popping, we process LEFT child first
            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)
        
        return op
        
        