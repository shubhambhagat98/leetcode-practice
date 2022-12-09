# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    answer = 0
    
    def maxDepthRec(self, root, depth):
        if not root:
            return;
        
        #leaf node --> update the depth
        if not root.left and not root.right:
            self.answer = max(self.answer, depth)
        
        self.maxDepthRec(root.left, depth+1)
        self.maxDepthRec(root.right, depth+1)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
        
#         return max(left_depth, right_depth) + 1
        
    
        self.maxDepthRec(root, 1)
        
        return self.answer