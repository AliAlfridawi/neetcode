# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        val = float("-infinity")
        self.count = 0 

        def helper(root, val):
            if not root:
                return 
            else:
                if val <= root.val:
                    self.count += 1
                    val = root.val
                helper(root.left,val)
                helper(root.right,val)
            
        helper(root, val)
        return self.count