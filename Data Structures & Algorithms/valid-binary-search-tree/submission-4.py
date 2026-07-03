# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, interval):
            if not root:
                return True
            else:
                if interval[0] >= root.val or interval[1] <= root.val:
                    return False
                return helper(root.left, [interval[0],root.val])and helper(root.right, [root.val, interval[1]])

        return helper(root, [float('-infinity'), float('infinity')])
            