# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    answer = False
    
    def findPathSum(self, root, prevSum, targetSum):
        
        if not root:
            return;
        
        if not root.left and not root.right:
            self.answer = self.answer or ((root.val + prevSum) == targetSum)
            
        self.findPathSum(root.left, root.val+prevSum, targetSum )
        self.findPathSum(root.right, root.val+prevSum, targetSum )
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.findPathSum(root, 0, targetSum)
        
        return self.answer
        