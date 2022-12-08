# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if not root:
            return []
        
#         result += self.postorderTraversal(root.left)
#         result += self.postorderTraversal(root.right)
#         result.append(root.val)
    
#         return result

        stack = [root]
        rev_stack = []
        current = ""
        while stack:
            current = stack.pop()
            rev_stack.append(current.val)
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        
        while rev_stack:
            result.append(rev_stack.pop())
        
        return result
                
        