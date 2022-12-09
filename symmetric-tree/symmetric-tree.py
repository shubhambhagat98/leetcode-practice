# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isPalindrome(self,l1):
        
        i = 0
        j = len(l1) -1
        
        while i<=j:
            if l1[i] != l1[j]:
                return False
            i+=1
            j-=1
        
        return True
        
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = [root]
        
        while queue:
            count  = len(queue)
            temp = []
            for i in range(count):
                current = queue.pop(0)
                
                if current!= "$":
                    temp.append(str(current.val))
                    if current.left:
                        queue.append(current.left)
                    else:
                        queue.append("$")
                    if current.right:
                        queue.append(current.right)
                    else:
                        queue.append("$")       
                elif current == "$":
                    temp.append("$")
                
            if not self.isPalindrome(temp):
                return False
        
        return True
                    
                
                
                    
        
        
        
        