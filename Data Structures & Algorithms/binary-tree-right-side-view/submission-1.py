# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levels = []

        def dfs(root, depth):
            if not root:
                return
            else:
                if len(self.levels) < depth:
                    self.levels.append(root.val)
                else:
                    self.levels[depth-1] = root.val
                dfs(root.left,depth+1)
                dfs(root.right,depth+1)
        
        dfs(root, 1) 

        return self.levels