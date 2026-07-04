# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
            cnt, val = k, 0

            def dfs(root):
                nonlocal cnt, val

                if not root:
                    return
                else:
                    dfs(root.left)
                    if cnt == 0:
                        return
                    cnt -= 1
                    if cnt == 0: 
                        val = root.val
                    dfs(root.right)
            
            dfs(root)
            return val
                    