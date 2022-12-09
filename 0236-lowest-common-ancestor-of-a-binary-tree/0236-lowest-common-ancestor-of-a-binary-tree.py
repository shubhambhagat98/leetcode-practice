# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    lowest_ancestor = (None, float('-inf'))
    
    def getLCA(self,root, p, q, depth):
        
        # print(f"LCA ==> {self.lowest_ancestor}")
        
        if not root:
            return set()
        
        
        union_set = set()
        
        if not self.lowest_ancestor[0]:
            left_set = self.getLCA(root.left, p, q, depth+1)
            right_set = self.getLCA(root.right, p, q, depth +1)

            union_set = left_set | right_set

            if not union_set:
                if root.val == p.val or root.val == q.val: 
                    return {root.val}
                else:
                    return set()
            elif len(union_set) == 2:
                if depth > self.lowest_ancestor[1] :
                    print(f"curr LCA ==> {root.val} | depth => {depth}")
                    self.lowest_ancestor = (root, depth)
            elif len(union_set) == 1:
                if (root.val == p.val or root.val == q.val) and (root.val not in union_set):
                    union_set.add(root.val)
                    if depth > self.lowest_ancestor[1] :
                        print(f"curr LCA ==> {root.val} | depth => {depth}")
                        self.lowest_ancestor = (root, depth)       
        return union_set
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.getLCA(root, p, q, 1)
        return self.lowest_ancestor[0]
        