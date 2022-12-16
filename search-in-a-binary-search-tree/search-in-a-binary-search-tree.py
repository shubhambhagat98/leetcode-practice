# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # def __init__(self):
    #     self.answer = []
    
#     def levelOrderTraversal(self,root):
        
#         op = [root]
#         queue = [root]
#         while queue:
            
#             # length = len(queue)
#             for x in range(len(queue)):
#                 current = queue.pop(0)
#                 if current.left:
#                     print(current.left.val)
#                     op.append(current.left)
#                     queue.append(current.left)
#                 if current.right:
#                     print(current.right.val)
#                     op.append(current.right)
#                     queue.append(current.right)
#         print( [ x.val for x in op ])
#         return op
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        result = []
        
        
        
        if not root:
            print("not root")
            return None
        
        if root.val == val:
            return root
        
        elif val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        
        