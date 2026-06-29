# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(root1, root2):
            if not root1 and not root2:
                return 0
            elif (root1 and not root2) or (not root1 and root2):
                return 1 
            else:
                if root1.val != root2.val:
                    return 1
                else:
                    return 0 + helper(root1.left,root2.left) + helper(root1.right, root2.right)
            
        return helper(p, q) == 0 
