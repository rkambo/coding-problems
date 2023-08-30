class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p) == self.dfs(q)
    def dfs(self, root):
        if not root:
            return ['X']

        leftTree = self.dfs(root.left)
        rightTree = self.dfs(root.right)
        
        return [root.val, *leftTree, *rightTree]