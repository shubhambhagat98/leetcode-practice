# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def getCount(self, root):
        final_count = 0
        final_flag = False
        
        if not root:
            return (0, True)
        
        if not root.left and not root.right:
            return (1, True)
        
        
        left_sub_count, left_flag = self.getCount(root.left)
        right_sub_count, right_flag = self.getCount(root.right)
        
        final_count = left_sub_count + right_sub_count
        
        if root.left and root.right:
            if left_flag and right_flag and root.val == root.left.val and root.val== root.right.val:
                final_count +=  1
                final_flag = True
        elif left_flag and root.left and not root.right:
            if root.val == root.left.val:
                final_count +=  1
                final_flag = True
        elif right_flag and not root.left and root.right:
            if root.val == root.right.val:
                final_count += 1
                final_flag = True
                
        return (final_count, final_flag)
    
    
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        answer, flag = self.getCount(root)
        
        return answer
        
        
        
            
        
        