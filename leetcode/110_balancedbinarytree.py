class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            leftTree = dfs(root.left)
            rightTree = dfs(root.right)
            
            isBalanced = (leftTree[0] and rightTree[0] and abs(leftTree[1] - rightTree[1]) <= 1)
            
            return[isBalanced, 1 + max(leftTree[1],rightTree[1])]
        return dfs(root)[0]